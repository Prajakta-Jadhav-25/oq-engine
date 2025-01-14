scenario hazard
===============

+----------------+----------------------+
| checksum32     | 1_553_725_326        |
+----------------+----------------------+
| date           | 2022-03-17T11:28:56  |
+----------------+----------------------+
| engine_version | 3.14.0-gitaed816bf7b |
+----------------+----------------------+
| input_size     | 6_629                |
+----------------+----------------------+

num_sites = 7, num_levels = 1, num_rlzs = ?

Parameters
----------
+---------------------------------+--------------------------------------------+
| parameter                       | value                                      |
+---------------------------------+--------------------------------------------+
| calculation_mode                | 'scenario'                                 |
+---------------------------------+--------------------------------------------+
| number_of_logic_tree_samples    | 0                                          |
+---------------------------------+--------------------------------------------+
| maximum_distance                | {'default': [[2.5, 200.0], [10.2, 200.0]]} |
+---------------------------------+--------------------------------------------+
| investigation_time              | None                                       |
+---------------------------------+--------------------------------------------+
| ses_per_logic_tree_path         | 1                                          |
+---------------------------------+--------------------------------------------+
| truncation_level                | 3.0                                        |
+---------------------------------+--------------------------------------------+
| rupture_mesh_spacing            | 2.0                                        |
+---------------------------------+--------------------------------------------+
| complex_fault_mesh_spacing      | 2.0                                        |
+---------------------------------+--------------------------------------------+
| width_of_mfd_bin                | None                                       |
+---------------------------------+--------------------------------------------+
| area_source_discretization      | None                                       |
+---------------------------------+--------------------------------------------+
| pointsource_distance            | {'default': '1000'}                        |
+---------------------------------+--------------------------------------------+
| ground_motion_correlation_model | 'JB2009'                                   |
+---------------------------------+--------------------------------------------+
| minimum_intensity               | {}                                         |
+---------------------------------+--------------------------------------------+
| random_seed                     | 42                                         |
+---------------------------------+--------------------------------------------+
| master_seed                     | 123456789                                  |
+---------------------------------+--------------------------------------------+
| ses_seed                        | 42                                         |
+---------------------------------+--------------------------------------------+

Input files
-----------
+-----------------+----------------------------------------------+
| Name            | File                                         |
+-----------------+----------------------------------------------+
| exposure        | `exposure_model.xml <exposure_model.xml>`_   |
+-----------------+----------------------------------------------+
| gsim_logic_tree | `gsim_logic_tree.xml <gsim_logic_tree.xml>`_ |
+-----------------+----------------------------------------------+
| job_ini         | `job_haz.ini <job_haz.ini>`_                 |
+-----------------+----------------------------------------------+
| rupture_model   | `rupture_model.xml <rupture_model.xml>`_     |
+-----------------+----------------------------------------------+

Exposure model
--------------
+-------------+---+
| #assets     | 7 |
+-------------+---+
| #taxonomies | 3 |
+-------------+---+

+----------+-----------+---------+--------+-----+-----+------------+
| taxonomy | num_sites | mean    | stddev | min | max | num_assets |
+----------+-----------+---------+--------+-----+-----+------------+
| tax1     | 4         | 1.00000 | 0%     | 1   | 1   | 4          |
+----------+-----------+---------+--------+-----+-----+------------+
| tax2     | 2         | 1.00000 | 0%     | 1   | 1   | 2          |
+----------+-----------+---------+--------+-----+-----+------------+
| tax3     | 1         | 1.00000 | nan    | 1   | 1   | 1          |
+----------+-----------+---------+--------+-----+-----+------------+
| *ALL*    | 7         | 1.00000 | 0%     | 1   | 1   | 7          |
+----------+-----------+---------+--------+-----+-----+------------+

Information about the tasks
---------------------------
Not available

Data transfer
-------------
+------+------+----------+
| task | sent | received |
+------+------+----------+

Slowest operations
------------------
+------------------+----------+-----------+--------+
| calc_50678       | time_sec | memory_mb | counts |
+------------------+----------+-----------+--------+
| importing inputs | 0.02553  | 0.0       | 1      |
+------------------+----------+-----------+--------+
| reading exposure | 0.00833  | 0.0       | 1      |
+------------------+----------+-----------+--------+