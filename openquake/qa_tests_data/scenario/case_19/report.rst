Reading ruptures.csv
====================

+----------------+----------------------+
| checksum32     | 2_513_801_080        |
+----------------+----------------------+
| date           | 2022-03-17T11:28:54  |
+----------------+----------------------+
| engine_version | 3.14.0-gitaed816bf7b |
+----------------+----------------------+
| input_size     | 26_131               |
+----------------+----------------------+

num_sites = 1, num_levels = 1, num_rlzs = ?

Parameters
----------
+---------------------------------+----------------------------------------+
| parameter                       | value                                  |
+---------------------------------+----------------------------------------+
| calculation_mode                | 'scenario'                             |
+---------------------------------+----------------------------------------+
| number_of_logic_tree_samples    | 0                                      |
+---------------------------------+----------------------------------------+
| maximum_distance                | {'default': [[2.5, 200], [10.2, 200]]} |
+---------------------------------+----------------------------------------+
| investigation_time              | None                                   |
+---------------------------------+----------------------------------------+
| ses_per_logic_tree_path         | 1                                      |
+---------------------------------+----------------------------------------+
| truncation_level                | None                                   |
+---------------------------------+----------------------------------------+
| rupture_mesh_spacing            | 5.0                                    |
+---------------------------------+----------------------------------------+
| complex_fault_mesh_spacing      | 5.0                                    |
+---------------------------------+----------------------------------------+
| width_of_mfd_bin                | None                                   |
+---------------------------------+----------------------------------------+
| area_source_discretization      | None                                   |
+---------------------------------+----------------------------------------+
| pointsource_distance            | {'default': '1000'}                    |
+---------------------------------+----------------------------------------+
| ground_motion_correlation_model | None                                   |
+---------------------------------+----------------------------------------+
| minimum_intensity               | {}                                     |
+---------------------------------+----------------------------------------+
| random_seed                     | 113                                    |
+---------------------------------+----------------------------------------+
| master_seed                     | 123456789                              |
+---------------------------------+----------------------------------------+
| ses_seed                        | 42                                     |
+---------------------------------+----------------------------------------+

Input files
-----------
+-----------------+----------------------------------+
| Name            | File                             |
+-----------------+----------------------------------+
| gsim_logic_tree | `gmpe_sif.xml <gmpe_sif.xml>`_   |
+-----------------+----------------------------------+
| job_ini         | `job.ini <job.ini>`_             |
+-----------------+----------------------------------+
| rupture_model   | `ruptures.csv <ruptures.csv>`_   |
+-----------------+----------------------------------+
| site_model      | `sitemodel.csv <sitemodel.csv>`_ |
+-----------------+----------------------------------+

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
| calc_50663       | time_sec | memory_mb | counts |
+------------------+----------+-----------+--------+
| importing inputs | 0.02398  | 0.0       | 1      |
+------------------+----------+-----------+--------+