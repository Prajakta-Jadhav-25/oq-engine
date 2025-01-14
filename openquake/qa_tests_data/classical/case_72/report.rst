USA NSHMP14 (excluding California) - Collapsed Model
====================================================

+----------------+----------------------+
| checksum32     | 3_615_018_993        |
+----------------+----------------------+
| date           | 2022-03-17T11:25:16  |
+----------------+----------------------+
| engine_version | 3.14.0-gitaed816bf7b |
+----------------+----------------------+
| input_size     | 128_703              |
+----------------+----------------------+

num_sites = 2, num_levels = 20, num_rlzs = 1

Parameters
----------
+---------------------------------+----------------------------------------+
| parameter                       | value                                  |
+---------------------------------+----------------------------------------+
| calculation_mode                | 'preclassical'                         |
+---------------------------------+----------------------------------------+
| number_of_logic_tree_samples    | 1                                      |
+---------------------------------+----------------------------------------+
| maximum_distance                | {'default': [[2.5, 200], [10.2, 200]]} |
+---------------------------------+----------------------------------------+
| investigation_time              | 1.0                                    |
+---------------------------------+----------------------------------------+
| ses_per_logic_tree_path         | 1                                      |
+---------------------------------+----------------------------------------+
| truncation_level                | 3.0                                    |
+---------------------------------+----------------------------------------+
| rupture_mesh_spacing            | 5.0                                    |
+---------------------------------+----------------------------------------+
| complex_fault_mesh_spacing      | 10.0                                   |
+---------------------------------+----------------------------------------+
| width_of_mfd_bin                | 0.1                                    |
+---------------------------------+----------------------------------------+
| area_source_discretization      | 10.0                                   |
+---------------------------------+----------------------------------------+
| pointsource_distance            | {'default': '1000'}                    |
+---------------------------------+----------------------------------------+
| ground_motion_correlation_model | None                                   |
+---------------------------------+----------------------------------------+
| minimum_intensity               | {}                                     |
+---------------------------------+----------------------------------------+
| random_seed                     | 23                                     |
+---------------------------------+----------------------------------------+
| master_seed                     | 123456789                              |
+---------------------------------+----------------------------------------+
| ses_seed                        | 42                                     |
+---------------------------------+----------------------------------------+

Input files
-----------
+---------------------------+------------------------------------------------+
| Name                      | File                                           |
+---------------------------+------------------------------------------------+
| gsim_logic_tree           | `gmmLT.xml <gmmLT.xml>`_                       |
+---------------------------+------------------------------------------------+
| job_ini                   | `job.ini <job.ini>`_                           |
+---------------------------+------------------------------------------------+
| reqv:Active Shallow Crust | `lookup_reqv_asc.hdf5 <lookup_reqv_asc.hdf5>`_ |
+---------------------------+------------------------------------------------+
| sites                     | `sites.csv <sites.csv>`_                       |
+---------------------------+------------------------------------------------+
| source_model_logic_tree   | `ssmLT.xml <ssmLT.xml>`_                       |
+---------------------------+------------------------------------------------+

Required parameters per tectonic region type
--------------------------------------------
+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------------------------+------------------------------------+
| trt_smr              | gsims                                                                                                                                                                                                                                                                 | distances       | siteparams                    | ruptparams                         |
+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------------------------+------------------------------------+
| Active Shallow Crust | [NSHMP2014]\ngmpe_name = 'AbrahamsonEtAl2014'\nsgn = 0 [NSHMP2014]\ngmpe_name = 'BooreEtAl2014'\nsgn = 0 [NSHMP2014]\ngmpe_name = 'CampbellBozorgnia2014'\nsgn = 0 [NSHMP2014]\ngmpe_name = 'ChiouYoungs2014'\nsgn = 0 [NSHMP2014]\ngmpe_name = 'Idriss2014'\nsgn = 0 | rjb rrup rx ry0 | vs30 vs30measured z1pt0 z2pt5 | dip hypo_depth mag rake width ztor |
+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------+-------------------------------+------------------------------------+

Slowest sources
---------------
+----------------------------+------+-----------+-----------+--------------+
| source_id                  | code | calc_time | num_sites | eff_ruptures |
+----------------------------+------+-----------+-----------+--------------+
| -123_4000_46_4000_1_0_15_0 | P    | 0.0       | 2         | 16           |
+----------------------------+------+-----------+-----------+--------------+

Computation times by source typology
------------------------------------
+------+-----------+-----------+--------------+---------+
| code | calc_time | num_sites | eff_ruptures | weight  |
+------+-----------+-----------+--------------+---------+
| P    | 0.0       | 2         | 16           | 3.08000 |
+------+-----------+-----------+--------------+---------+

Information about the tasks
---------------------------
+--------------------+--------+---------+--------+---------+---------+---------+
| operation-duration | counts | mean    | stddev | min     | max     | slowfac |
+--------------------+--------+---------+--------+---------+---------+---------+
| preclassical       | 1      | 0.00212 | nan    | 0.00212 | 0.00212 | 1.00000 |
+--------------------+--------+---------+--------+---------+---------+---------+
| read_source_model  | 1      | 0.00148 | nan    | 0.00148 | 0.00148 | 1.00000 |
+--------------------+--------+---------+--------+---------+---------+---------+

Data transfer
-------------
+-------------------+-------------------------------------------+----------+
| task              | sent                                      | received |
+-------------------+-------------------------------------------+----------+
| read_source_model |                                           | 1.64 KB  |
+-------------------+-------------------------------------------+----------+
| split_task        | args=630.66 KB elements=1.22 KB func=66 B | 0 B      |
+-------------------+-------------------------------------------+----------+
| preclassical      |                                           | 1.37 KB  |
+-------------------+-------------------------------------------+----------+

Slowest operations
------------------
+---------------------------+-----------+-----------+--------+
| calc_50558, maxmem=1.9 GB | time_sec  | memory_mb | counts |
+---------------------------+-----------+-----------+--------+
| importing inputs          | 0.11496   | 0.0       | 1      |
+---------------------------+-----------+-----------+--------+
| composite source model    | 0.09864   | 0.0       | 1      |
+---------------------------+-----------+-----------+--------+
| total preclassical        | 0.00212   | 0.0       | 1      |
+---------------------------+-----------+-----------+--------+
| total read_source_model   | 0.00148   | 0.0       | 1      |
+---------------------------+-----------+-----------+--------+
| weighting sources         | 0.00126   | 0.0       | 1      |
+---------------------------+-----------+-----------+--------+
| splitting sources         | 3.481E-04 | 0.0       | 1      |
+---------------------------+-----------+-----------+--------+