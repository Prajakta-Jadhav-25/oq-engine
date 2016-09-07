# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2015-2016 GEM Foundation
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake. If not, see <http://www.gnu.org/licenses/>.

"""
Here there are some real functional tests starting an engine server and
running computations.
"""
from __future__ import print_function
import os
import sys
import json
import time
import unittest
import subprocess
import tempfile
import django
import requests
from openquake.baselib.general import writetmp


if requests.__version__ < '1.0.0':
    requests.Response.text = property(lambda self: self.content)


class EngineServerTestCase(unittest.TestCase):
    hostport = 'localhost:8761'
    datadir = os.path.join(os.path.dirname(__file__), 'data')

    # general utilities

    @classmethod
    def post(cls, path, data=None, **params):
        return requests.post('http://%s/v1/calc/%s' % (cls.hostport, path),
                             data, **params)

    @classmethod
    def post_nrml(cls, data=None, **params):
        return requests.post(
            'http://%s/v1/valid/' % cls.hostport,
            data, **params)

    @classmethod
    def get(cls, path, **params):
        resp = requests.get('http://%s/v1/calc/%s' % (cls.hostport, path),
                            params=params)
        if not resp.text:
            sys.stderr.write(open(cls.errfname).read())
            return {}
        try:
            return json.loads(resp.text)
        except:
            print('Invalid JSON, see %s' % writetmp(resp.text),
                  file=sys.stderr)
            return {}

    @classmethod
    def get_text(cls, path, **params):
        resp = requests.get('http://%s/v1/calc/%s' % (cls.hostport, path),
                            params=params)
        return resp.text

    @classmethod
    def wait(cls):
        # wait until all calculations stop
        while True:
            running_calcs = cls.get('list', is_running='true')
            if not running_calcs:
                break
            time.sleep(1)

    def postzip(self, archive):
        with open(os.path.join(self.datadir, archive), 'rb') as a:
            resp = self.post('run', {}, files=dict(archive=a))
        try:
            js = json.loads(resp.text)
        except:
            raise ValueError('Invalid JSON response: %r' % resp.text)
        if resp.status_code == 200:  # ok case
            job_id = js['job_id']
            self.job_ids.append(job_id)
            time.sleep(1)  # wait a bit for the calc to start
            return job_id
        else:  # error case
            return ''.join(js)  # traceback string

    # start/stop server utilities

    @classmethod
    def setUpClass(cls):
        if django.get_version() < '1.5':
            # Django too old
            raise unittest.SkipTest('webui tests do not run with Diango < 1.5')

        cls.job_ids = []
        env = os.environ.copy()
        env['OQ_DISTRIBUTE'] = 'no'
        # let's impersonate the user openquake, the one running the WebUI:
        # we need to set LOGNAME on Linux and USERNAME on Windows
        env['LOGNAME'] = env['USERNAME'] = 'openquake'
        cls.fd, cls.errfname = tempfile.mkstemp(prefix='webui')
        print('Errors saved in %s' % cls.errfname, file=sys.stderr)
        cls.proc = subprocess.Popen(
            [sys.executable, '-m', 'openquake.server.manage', 'runserver',
             cls.hostport, '--noreload', '--nothreading'],
            env=env, stderr=cls.fd)  # redirect the server logs
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.wait()
        cls.proc.kill()
        os.close(cls.fd)

    # tests

    def test_404(self):
        # looking for a missing calc_id
        resp = requests.get('http://%s/v1/calc/0' % self.hostport)
        assert resp.status_code == 404, resp

    def test_ok(self):
        job_id = self.postzip('archive_ok.zip')
        self.wait()
        log = self.get('%s/log/:' % job_id)
        self.assertGreater(len(log), 0)
        results = self.get('%s/results' % job_id)
        self.assertGreater(len(results), 0)
        for res in results:
            if res['type'] == 'gmfs':
                continue  # exporting the GMFs would be too slow
            etype = res['outtypes'][0]  # get the first export type
            text = self.get_text(
                'result/%s' % res['id'], export_type=etype)
            self.assertGreater(len(text), 0)

        # test no filtering in actions.get_calcs
        #all_jobs = self.get('list')
        #self.assertGreater(len(all_jobs), 1)

    def test_err_1(self):
        # the rupture XML file has a syntax error
        job_id = self.postzip('archive_err_1.zip')
        self.wait()
        tb = self.get('%s/traceback' % job_id)
        if not tb:
            sys.stderr.write('Empty traceback, please check!\n')

        self.post('%s/remove' % job_id)
        # make sure job_id is no more in the list of relevant jobs
        job_ids = [job['id'] for job in self.get('list', relevant=True)]
        self.assertFalse(job_id in job_ids)

    def test_err_2(self):
        # the file logic-tree-source-model.xml is missing
        tb_str = self.postzip('archive_err_2.zip')
        self.assertIn('No such file', tb_str)

    def test_err_3(self):
        # there is no file job.ini, job_hazard.ini or job_risk.ini
        tb_str = self.postzip('archive_err_3.zip')
        self.assertIn('Could not find any file of the form', tb_str)

    # tests for nrml validation

    def test_validate_nrml_valid(self):
        valid_file = os.path.join(self.datadir, 'vulnerability_model.xml')
        with open(valid_file, 'rb') as vf:
            valid_content = vf.read()
        data = dict(xml_text=valid_content)
        resp = self.post_nrml(data)
        self.assertEqual(resp.status_code, 200)
        resp_text_dict = json.loads(resp.text)
        self.assertTrue(resp_text_dict['valid'])
        self.assertIsNone(resp_text_dict['error_msg'])
        self.assertIsNone(resp_text_dict['error_line'])

    def test_validate_nrml_invalid(self):
        invalid_file = os.path.join(self.datadir,
                                    'vulnerability_model_invalid.xml')
        with open(invalid_file, 'rb') as vf:
            invalid_content = vf.read()
        data = dict(xml_text=invalid_content)
        resp = self.post_nrml(data)
        self.assertEqual(resp.status_code, 200)
        resp_text_dict = json.loads(resp.text)
        self.assertFalse(resp_text_dict['valid'])
        self.assertIn(u'Could not convert lossRatio->positivefloats:'
                      ' float -0.018800826 < 0',
                      resp_text_dict['error_msg'])
        self.assertEqual(resp_text_dict['error_line'], 7)

    def test_validate_nrml_unclosed_tag(self):
        invalid_file = os.path.join(self.datadir,
                                    'vulnerability_model_unclosed_tag.xml')
        with open(invalid_file, 'rb') as vf:
            invalid_content = vf.read()
        data = dict(xml_text=invalid_content)
        resp = self.post_nrml(data)
        self.assertEqual(resp.status_code, 200)
        resp_text_dict = json.loads(resp.text)
        self.assertFalse(resp_text_dict['valid'])
        self.assertIn(u'mismatched tag', resp_text_dict['error_msg'])
        self.assertEqual(resp_text_dict['error_line'], 9)

    def test_validate_nrml_missing_parameter(self):
        # passing a wrong parameter, instead of the required 'xml_text'
        data = dict(foo="bar")
        resp = self.post_nrml(data)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(resp.text, 'Please provide the "xml_text" parameter')

    # TODO: add more tests for error situations
