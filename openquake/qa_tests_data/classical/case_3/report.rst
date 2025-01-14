Classical Hazard QA Test, Case 3
================================

+----------------+----------------------+
| checksum32     | 1_696_514_331        |
+----------------+----------------------+
| date           | 2022-03-17T11:22:45  |
+----------------+----------------------+
| engine_version | 3.14.0-gitaed816bf7b |
+----------------+----------------------+
| input_size     | 7_430                |
+----------------+----------------------+

num_sites = 1, num_levels = 3, num_rlzs = 1

Parameters
----------
+---------------------------------+--------------------------------------------+
| parameter                       | value                                      |
+---------------------------------+--------------------------------------------+
| calculation_mode                | 'preclassical'                             |
+---------------------------------+--------------------------------------------+
| number_of_logic_tree_samples    | 0                                          |
+---------------------------------+--------------------------------------------+
| maximum_distance                | {'default': [[2.5, 200.0], [10.2, 200.0]]} |
+---------------------------------+--------------------------------------------+
| investigation_time              | 1.0                                        |
+---------------------------------+--------------------------------------------+
| ses_per_logic_tree_path         | 1                                          |
+---------------------------------+--------------------------------------------+
| truncation_level                | 0.0                                        |
+---------------------------------+--------------------------------------------+
| rupture_mesh_spacing            | 1.0                                        |
+---------------------------------+--------------------------------------------+
| complex_fault_mesh_spacing      | 1.0                                        |
+---------------------------------+--------------------------------------------+
| width_of_mfd_bin                | 1.0                                        |
+---------------------------------+--------------------------------------------+
| area_source_discretization      | 0.5                                        |
+---------------------------------+--------------------------------------------+
| pointsource_distance            | {'default': '1000'}                        |
+---------------------------------+--------------------------------------------+
| ground_motion_correlation_model | None                                       |
+---------------------------------+--------------------------------------------+
| minimum_intensity               | {}                                         |
+---------------------------------+--------------------------------------------+
| random_seed                     | 1066                                       |
+---------------------------------+--------------------------------------------+
| master_seed                     | 123456789                                  |
+---------------------------------+--------------------------------------------+
| ses_seed                        | 42                                         |
+---------------------------------+--------------------------------------------+

Input files
-----------
+-------------------------+--------------------------------------------------------------+
| Name                    | File                                                         |
+-------------------------+--------------------------------------------------------------+
| gsim_logic_tree         | `gsim_logic_tree.xml <gsim_logic_tree.xml>`_                 |
+-------------------------+--------------------------------------------------------------+
| job_ini                 | `job.ini <job.ini>`_                                         |
+-------------------------+--------------------------------------------------------------+
| source_model_logic_tree | `source_model_logic_tree.xml <source_model_logic_tree.xml>`_ |
+-------------------------+--------------------------------------------------------------+

Required parameters per tectonic region type
--------------------------------------------
+----------------------+------------------+-----------+------------+------------+
| trt_smr              | gsims            | distances | siteparams | ruptparams |
+----------------------+------------------+-----------+------------+------------+
| active shallow crust | [SadighEtAl1997] | rrup      | vs30       | mag rake   |
+----------------------+------------------+-----------+------------+------------+

Slowest sources
---------------
+-----------+------+-----------+-----------+--------------+
| source_id | code | calc_time | num_sites | eff_ruptures |
+-----------+------+-----------+-----------+--------------+
| 1         | A    | 0.0       | 307       | 307          |
+-----------+------+-----------+-----------+--------------+

Computation times by source typology
------------------------------------
+------+-----------+-----------+--------------+--------+
| code | calc_time | num_sites | eff_ruptures | weight |
+------+-----------+-----------+--------------+--------+
| A    | 0.0       | 307       | 307          | 620.1  |
+------+-----------+-----------+--------------+--------+

Information about the tasks
---------------------------
+--------------------+--------+---------+--------+-----------+---------+---------+
| operation-duration | counts | mean    | stddev | min       | max     | slowfac |
+--------------------+--------+---------+--------+-----------+---------+---------+
| preclassical       | 2      | 0.15451 | 99%    | 2.112E-04 | 0.30880 | 1.99863 |
+--------------------+--------+---------+--------+-----------+---------+---------+
| read_source_model  | 1      | 0.00420 | nan    | 0.00420   | 0.00420 | 1.00000 |
+--------------------+--------+---------+--------+-----------+---------+---------+

Data transfer
-------------
+-------------------+------------------------------------------+----------+
| task              | sent                                     | received |
+-------------------+------------------------------------------+----------+
| read_source_model |                                          | 2.64 KB  |
+-------------------+------------------------------------------+----------+
| split_task        | args=519.61 KB func=66 B elements=5 B    | 0 B      |
+-------------------+------------------------------------------+----------+
| preclassical      | cmaker=519.28 KB srcs=3.4 KB sites=439 B | 66.56 KB |
+-------------------+------------------------------------------+----------+

Slowest operations
------------------
+---------------------------+----------+-----------+--------+
| calc_50512, maxmem=1.9 GB | time_sec | memory_mb | counts |
+---------------------------+----------+-----------+--------+
| total preclassical        | 0.30880  | 1.54297   | 1      |
+---------------------------+----------+-----------+--------+
| weighting sources         | 0.25722  | 0.0       | 307    |
+---------------------------+----------+-----------+--------+
| importing inputs          | 0.10000  | 0.17969   | 1      |
+---------------------------+----------+-----------+--------+
| composite source model    | 0.09442  | 0.0       | 1      |
+---------------------------+----------+-----------+--------+
| splitting sources         | 0.04825  | 0.82812   | 1      |
+---------------------------+----------+-----------+--------+
| total read_source_model   | 0.00420  | 0.0       | 1      |
+---------------------------+----------+-----------+--------+