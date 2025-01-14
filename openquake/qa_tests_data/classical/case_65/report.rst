test multi-fault source
=======================

+----------------+----------------------+
| checksum32     | 1_902_944_982        |
+----------------+----------------------+
| date           | 2022-03-17T11:24:55  |
+----------------+----------------------+
| engine_version | 3.14.0-gitaed816bf7b |
+----------------+----------------------+
| input_size     | 3_479                |
+----------------+----------------------+

num_sites = 1, num_levels = 20, num_rlzs = 1

Parameters
----------
+---------------------------------+--------------------------------------------+
| parameter                       | value                                      |
+---------------------------------+--------------------------------------------+
| calculation_mode                | 'preclassical'                             |
+---------------------------------+--------------------------------------------+
| number_of_logic_tree_samples    | 0                                          |
+---------------------------------+--------------------------------------------+
| maximum_distance                | {'default': [[2.5, 100.0], [10.2, 100.0]]} |
+---------------------------------+--------------------------------------------+
| investigation_time              | 1.0                                        |
+---------------------------------+--------------------------------------------+
| ses_per_logic_tree_path         | 1                                          |
+---------------------------------+--------------------------------------------+
| truncation_level                | 5.0                                        |
+---------------------------------+--------------------------------------------+
| rupture_mesh_spacing            | 5.0                                        |
+---------------------------------+--------------------------------------------+
| complex_fault_mesh_spacing      | 5.0                                        |
+---------------------------------+--------------------------------------------+
| width_of_mfd_bin                | 0.1                                        |
+---------------------------------+--------------------------------------------+
| area_source_discretization      | 5.0                                        |
+---------------------------------+--------------------------------------------+
| pointsource_distance            | {'default': '1000'}                        |
+---------------------------------+--------------------------------------------+
| ground_motion_correlation_model | None                                       |
+---------------------------------+--------------------------------------------+
| minimum_intensity               | {}                                         |
+---------------------------------+--------------------------------------------+
| random_seed                     | 23                                         |
+---------------------------------+--------------------------------------------+
| master_seed                     | 123456789                                  |
+---------------------------------+--------------------------------------------+
| ses_seed                        | 42                                         |
+---------------------------------+--------------------------------------------+

Input files
-----------
+-------------------------+--------------------------+
| Name                    | File                     |
+-------------------------+--------------------------+
| gsim_logic_tree         | `gmmLT.xml <gmmLT.xml>`_ |
+-------------------------+--------------------------+
| job_ini                 | `job.ini <job.ini>`_     |
+-------------------------+--------------------------+
| source_model_logic_tree | `ssmLT.xml <ssmLT.xml>`_ |
+-------------------------+--------------------------+

Required parameters per tectonic region type
--------------------------------------------
+----------------------+----------------------+-----------------+-------------------------+-------------------------+
| trt_smr              | gsims                | distances       | siteparams              | ruptparams              |
+----------------------+----------------------+-----------------+-------------------------+-------------------------+
| Active Shallow Crust | [AbrahamsonEtAl2014] | rjb rrup rx ry0 | vs30 vs30measured z1pt0 | dip mag rake width ztor |
+----------------------+----------------------+-----------------+-------------------------+-------------------------+

Slowest sources
---------------
+-----------+------+-----------+-----------+--------------+
| source_id | code | calc_time | num_sites | eff_ruptures |
+-----------+------+-----------+-----------+--------------+
| 1         | F    | 0.0       | 1         | 3            |
+-----------+------+-----------+-----------+--------------+

Computation times by source typology
------------------------------------
+------+-----------+-----------+--------------+--------+
| code | calc_time | num_sites | eff_ruptures | weight |
+------+-----------+-----------+--------------+--------+
| F    | 0.0       | 1         | 3            | 60.0   |
+------+-----------+-----------+--------------+--------+

Information about the tasks
---------------------------
+--------------------+--------+-----------+--------+-----------+---------+---------+
| operation-duration | counts | mean      | stddev | min       | max     | slowfac |
+--------------------+--------+-----------+--------+-----------+---------+---------+
| preclassical       | 2      | 9.843E-04 | 75%    | 2.456E-04 | 0.00172 | 1.75051 |
+--------------------+--------+-----------+--------+-----------+---------+---------+
| read_source_model  | 2      | 0.05295   | 97%    | 0.00130   | 0.10459 | 1.97539 |
+--------------------+--------+-----------+--------+-----------+---------+---------+

Data transfer
-------------
+-------------------+------------------------------------------+----------+
| task              | sent                                     | received |
+-------------------+------------------------------------------+----------+
| read_source_model | converter=722 B fname=181 B              | 7.09 KB  |
+-------------------+------------------------------------------+----------+
| split_task        | args=1.02 MB elements=6.75 KB func=132 B | 0 B      |
+-------------------+------------------------------------------+----------+
| preclassical      |                                          | 6.79 KB  |
+-------------------+------------------------------------------+----------+

Slowest operations
------------------
+---------------------------+----------+-----------+--------+
| calc_50551, maxmem=1.9 GB | time_sec | memory_mb | counts |
+---------------------------+----------+-----------+--------+
| importing inputs          | 1.62282  | 0.04297   | 1      |
+---------------------------+----------+-----------+--------+
| composite source model    | 1.61681  | 0.0       | 1      |
+---------------------------+----------+-----------+--------+
| total read_source_model   | 0.10590  | 0.83203   | 2      |
+---------------------------+----------+-----------+--------+
| total preclassical        | 0.00172  | 0.51953   | 1      |
+---------------------------+----------+-----------+--------+
| splitting sources         | 0.00129  | 0.51953   | 1      |
+---------------------------+----------+-----------+--------+