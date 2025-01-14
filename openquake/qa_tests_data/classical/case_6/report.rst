Classical Hazard QA Test, Case 6
================================

+----------------+----------------------+
| checksum32     | 2_233_480_381        |
+----------------+----------------------+
| date           | 2022-03-17T11:24:38  |
+----------------+----------------------+
| engine_version | 3.14.0-gitaed816bf7b |
+----------------+----------------------+
| input_size     | 4_505                |
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
| rupture_mesh_spacing            | 0.1                                        |
+---------------------------------+--------------------------------------------+
| complex_fault_mesh_spacing      | 0.1                                        |
+---------------------------------+--------------------------------------------+
| width_of_mfd_bin                | 1.0                                        |
+---------------------------------+--------------------------------------------+
| area_source_discretization      | 10.0                                       |
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
| 2         | C    | 0.0       | 1         | 49           |
+-----------+------+-----------+-----------+--------------+
| 1         | S    | 0.0       | 1         | 91           |
+-----------+------+-----------+-----------+--------------+

Computation times by source typology
------------------------------------
+------+-----------+-----------+--------------+--------+
| code | calc_time | num_sites | eff_ruptures | weight |
+------+-----------+-----------+--------------+--------+
| C    | 0.0       | 1         | 49           | 51.0   |
+------+-----------+-----------+--------------+--------+
| S    | 0.0       | 1         | 91           | 93.8   |
+------+-----------+-----------+--------------+--------+

Information about the tasks
---------------------------
+--------------------+--------+---------+--------+-----------+---------+---------+
| operation-duration | counts | mean    | stddev | min       | max     | slowfac |
+--------------------+--------+---------+--------+-----------+---------+---------+
| preclassical       | 2      | 0.10044 | 99%    | 2.110E-04 | 0.20067 | 1.99790 |
+--------------------+--------+---------+--------+-----------+---------+---------+
| read_source_model  | 1      | 0.00393 | nan    | 0.00393   | 0.00393 | 1.00000 |
+--------------------+--------+---------+--------+-----------+---------+---------+

Data transfer
-------------
+-------------------+------------------------------------------+----------+
| task              | sent                                     | received |
+-------------------+------------------------------------------+----------+
| read_source_model |                                          | 2.25 KB  |
+-------------------+------------------------------------------+----------+
| split_task        | args=1.01 MB elements=2.04 KB func=132 B | 0 B      |
+-------------------+------------------------------------------+----------+
| preclassical      |                                          | 2.94 KB  |
+-------------------+------------------------------------------+----------+

Slowest operations
------------------
+---------------------------+----------+-----------+--------+
| calc_50545, maxmem=1.9 GB | time_sec | memory_mb | counts |
+---------------------------+----------+-----------+--------+
| total preclassical        | 0.20067  | 1.39844   | 2      |
+---------------------------+----------+-----------+--------+
| weighting sources         | 0.10110  | 0.0       | 2      |
+---------------------------+----------+-----------+--------+
| importing inputs          | 0.06402  | 0.0       | 1      |
+---------------------------+----------+-----------+--------+
| composite source model    | 0.05843  | 0.0       | 1      |
+---------------------------+----------+-----------+--------+
| total read_source_model   | 0.00393  | 0.0       | 1      |
+---------------------------+----------+-----------+--------+
| splitting sources         | 0.00318  | 0.0       | 2      |
+---------------------------+----------+-----------+--------+