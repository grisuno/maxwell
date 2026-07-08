❯ python3 maxwell_crystal.py
2026-03-14 14:35:05,695 - Main - INFO - ================================================================================
2026-03-14 14:35:05,695 - Main - INFO - MAXWELL EQUATIONS GROKKING VIA HAMILTONIAN TOPOLOGICAL CRYSTALLIZATION
2026-03-14 14:35:05,695 - Main - INFO - ================================================================================
2026-03-14 14:35:05,695 - Main - INFO - Grid size: 16
2026-03-14 14:35:05,695 - Main - INFO - Hidden dim: 32
2026-03-14 14:35:05,695 - Main - INFO - Expansion dim: 64
2026-03-14 14:35:05,695 - Main - INFO - Spectral layers: 2
2026-03-14 14:35:05,695 - Main - INFO - Field components (TM mode): 3
2026-03-14 14:35:05,695 - Main - INFO - Device: cpu
2026-03-14 14:35:05,695 - Main - INFO - Backbone: best.pth
2026-03-14 14:35:05,695 - Main - INFO - ================================================================================
2026-03-14 14:35:05,709 - HamiltonianInferenceEngine - INFO - Backbone checkpoint not found at best.pth, using analytical Maxwell operator
2026-03-14 14:35:05,709 - Phase0Orchestrator - INFO - ================================================================================
2026-03-14 14:35:05,709 - Phase0Orchestrator - INFO - PHASE 0: SPECTRAL KERNEL RATIO OPTIMIZATION (Chapter 10: GOE-GUE Transition)
2026-03-14 14:35:05,709 - Phase0Orchestrator - INFO - ================================================================================
2026-03-14 14:35:05,709 - Phase0Orchestrator - INFO - Matrix size: 256, Ensemble size: 10 matrices per ratio
2026-03-14 14:35:06,550 - Phase0Orchestrator - INFO -   Ratio 0.100: P(s) loss=0.0067, R2 loss=0.6780, Combined=0.1376, beta=0.50, ens_ratio=1.219
2026-03-14 14:35:07,584 - Phase0Orchestrator - INFO -   Ratio 0.121: P(s) loss=0.0055, R2 loss=0.6781, Combined=0.1373, beta=0.50, ens_ratio=1.222
2026-03-14 14:35:08,580 - Phase0Orchestrator - INFO -   Ratio 0.142: P(s) loss=0.0058, R2 loss=0.6757, Combined=0.1369, beta=0.50, ens_ratio=1.221
2026-03-14 14:35:09,573 - Phase0Orchestrator - INFO -   Ratio 0.163: P(s) loss=0.0047, R2 loss=0.6786, Combined=0.1371, beta=0.50, ens_ratio=1.221
2026-03-14 14:35:10,643 - Phase0Orchestrator - INFO -   Ratio 0.184: P(s) loss=0.0046, R2 loss=0.6763, Combined=0.1367, beta=2.50, ens_ratio=1.218
2026-03-14 14:35:11,717 - Phase0Orchestrator - INFO -   Ratio 0.205: P(s) loss=0.0053, R2 loss=0.6763, Combined=0.1369, beta=0.50, ens_ratio=1.219
2026-03-14 14:35:12,742 - Phase0Orchestrator - INFO -   Ratio 0.226: P(s) loss=0.0041, R2 loss=0.6786, Combined=0.1369, beta=1.38, ens_ratio=1.218
2026-03-14 14:35:13,649 - Phase0Orchestrator - INFO -   Ratio 0.247: P(s) loss=0.0041, R2 loss=0.6797, Combined=0.1372, beta=2.50, ens_ratio=1.219
2026-03-14 14:35:14,629 - Phase0Orchestrator - INFO -   Ratio 0.268: P(s) loss=0.0053, R2 loss=0.6747, Combined=0.1365, beta=0.50, ens_ratio=1.216
2026-03-14 14:35:15,619 - Phase0Orchestrator - INFO -   Ratio 0.289: P(s) loss=0.0037, R2 loss=0.6760, Combined=0.1363, beta=0.50, ens_ratio=1.217
2026-03-14 14:35:16,635 - Phase0Orchestrator - INFO -   Ratio 0.311: P(s) loss=0.0045, R2 loss=0.6711, Combined=0.1356, beta=1.37, ens_ratio=1.219
2026-03-14 14:35:17,667 - Phase0Orchestrator - INFO -   Ratio 0.332: P(s) loss=0.0051, R2 loss=0.6788, Combined=0.1373, beta=0.50, ens_ratio=1.216
2026-03-14 14:35:18,744 - Phase0Orchestrator - INFO -   Ratio 0.353: P(s) loss=0.0044, R2 loss=0.6787, Combined=0.1371, beta=0.50, ens_ratio=1.218
2026-03-14 14:35:19,698 - Phase0Orchestrator - INFO -   Ratio 0.374: P(s) loss=0.0046, R2 loss=0.6735, Combined=0.1361, beta=2.50, ens_ratio=1.216
2026-03-14 14:35:20,724 - Phase0Orchestrator - INFO -   Ratio 0.395: P(s) loss=0.0044, R2 loss=0.6784, Combined=0.1370, beta=2.50, ens_ratio=1.216
2026-03-14 14:35:21,739 - Phase0Orchestrator - INFO -   Ratio 0.416: P(s) loss=0.0043, R2 loss=0.6786, Combined=0.1370, beta=2.50, ens_ratio=1.211
2026-03-14 14:35:22,742 - Phase0Orchestrator - INFO -   Ratio 0.437: P(s) loss=0.0036, R2 loss=0.6793, Combined=0.1369, beta=0.50, ens_ratio=1.218
2026-03-14 14:35:23,773 - Phase0Orchestrator - INFO -   Ratio 0.458: P(s) loss=0.0049, R2 loss=0.6779, Combined=0.1371, beta=2.50, ens_ratio=1.213
2026-03-14 14:35:24,794 - Phase0Orchestrator - INFO -   Ratio 0.479: P(s) loss=0.0050, R2 loss=0.6787, Combined=0.1372, beta=0.50, ens_ratio=1.215
2026-03-14 14:35:25,810 - Phase0Orchestrator - INFO -   Ratio 0.500: P(s) loss=0.0038, R2 loss=0.6770, Combined=0.1365, beta=2.50, ens_ratio=1.215
2026-03-14 14:35:25,810 - Phase0Orchestrator - INFO - Phase 0 complete: Optimal imaginary ratio = 0.311 (combined loss = 0.1356)
2026-03-14 14:35:25,810 - Phase0Orchestrator - INFO -   Reference values: P(s) optimal ~0.18, R2 optimal ~0.30
2026-03-14 14:35:25,810 - Phase0Orchestrator - INFO -   Beta index indicates: GOE(beta=1) <-> GUE(beta=2) transition
2026-03-14 14:35:25,811 - BatchSizeProspector - INFO - Phase 1: Batch size prospecting started
2026-03-14 14:35:25,811 - BatchSizeProspector - INFO -   Testing batch_size=8
2026-03-14 14:35:52,520 - BatchSizeProspector - INFO -     batch_size=8: delta=0.485263, val_acc=1.0000, kappa=inf
2026-03-14 14:35:52,520 - BatchSizeProspector - INFO -   Testing batch_size=16
2026-03-14 14:36:07,171 - BatchSizeProspector - INFO -     batch_size=16: delta=0.485898, val_acc=1.0000, kappa=inf
2026-03-14 14:36:07,171 - BatchSizeProspector - INFO -   Testing batch_size=32
2026-03-14 14:36:17,928 - BatchSizeProspector - INFO -     batch_size=32: delta=0.486208, val_acc=1.0000, kappa=1.00e+00
2026-03-14 14:36:17,928 - BatchSizeProspector - INFO -   Testing batch_size=64
2026-03-14 14:36:26,907 - BatchSizeProspector - INFO -     batch_size=64: delta=0.486379, val_acc=1.0000, kappa=1.00e+00
2026-03-14 14:36:26,907 - BatchSizeProspector - INFO - Phase 1 complete: Best batch_size=32 (delta=0.486208, kappa=1.00e+00)
2026-03-14 14:36:26,909 - SeedMiner - INFO - Phase 2: Seed mining started
2026-03-14 14:36:41,148 - SeedMiner - INFO -   Seed    1 (1/200): delta=0.497918 v_delta=-0.000017 COOLING kappa=inf
2026-03-14 14:36:56,356 - SeedMiner - INFO -   Seed    2 (2/200): delta=0.499040 v_delta=-0.000012 COOLING kappa~1
2026-03-14 14:37:10,140 - SeedMiner - INFO -   Seed    3 (3/200): delta=0.497364 v_delta=-0.000014 COOLING kappa=inf
2026-03-14 14:37:24,661 - SeedMiner - INFO -   Seed    4 (4/200): delta=0.495227 v_delta=+0.000013 warming kappa~1
2026-03-14 14:37:39,494 - SeedMiner - INFO -   Seed    5 (5/200): delta=0.499256 v_delta=+0.000012 warming kappa=inf
2026-03-14 14:37:55,379 - SeedMiner - INFO -   Seed    6 (6/200): delta=0.490900 v_delta=+0.000017 warming kappa=inf
2026-03-14 14:38:10,278 - SeedMiner - INFO -   Seed    7 (7/200): delta=0.498332 v_delta=+0.000011 warming kappa~1
2026-03-14 14:38:25,059 - SeedMiner - INFO -   Seed    8 (8/200): delta=0.497320 v_delta=+0.000011 warming kappa=inf
2026-03-14 14:38:41,582 - SeedMiner - INFO -   Seed    9 (9/200): delta=0.487839 v_delta=-0.000012 COOLING kappa=inf
2026-03-14 14:38:56,649 - SeedMiner - INFO -   Seed   10 (10/200): delta=0.470193 v_delta=-0.000010 COOLING kappa~1
2026-03-14 14:39:10,456 - SeedMiner - INFO -   Seed   11 (11/200): delta=0.490497 v_delta=+0.000016 warming kappa~1
2026-03-14 14:39:26,367 - SeedMiner - INFO -   Seed   12 (12/200): delta=0.487595 v_delta=-0.000016 COOLING kappa~1
2026-03-14 14:39:42,969 - SeedMiner - INFO -   Seed   13 (13/200): delta=0.487172 v_delta=+0.000012 warming kappa=inf
2026-03-14 14:39:57,670 - SeedMiner - INFO -   Seed   14 (14/200): delta=0.493061 v_delta=-0.000012 COOLING kappa~1
2026-03-14 14:40:13,323 - SeedMiner - INFO -   Seed   15 (15/200): delta=0.462644 v_delta=-0.000010 COOLING kappa=inf
2026-03-14 14:40:29,830 - SeedMiner - INFO -   Seed   16 (16/200): delta=0.466706 v_delta=-0.000011 COOLING kappa=inf
2026-03-14 14:40:43,522 - SeedMiner - INFO -   Seed   17 (17/200): delta=0.466473 v_delta=-0.000012 COOLING kappa=inf
2026-03-14 14:40:57,463 - SeedMiner - INFO -   Seed   18 (18/200): delta=0.483574 v_delta=+0.000009 warming kappa=inf
2026-03-14 14:41:11,813 - SeedMiner - INFO -   Seed   19 (19/200): delta=0.493754 v_delta=+0.000016 warming kappa=inf
2026-03-14 14:41:27,212 - SeedMiner - INFO -   Seed   20 (20/200): delta=0.464337 v_delta=-0.000011 COOLING kappa~1
2026-03-14 14:41:44,546 - SeedMiner - INFO -   Seed   21 (21/200): delta=0.493212 v_delta=-0.000014 COOLING kappa~1
2026-03-14 14:41:59,789 - SeedMiner - INFO -   Seed   22 (22/200): delta=0.492723 v_delta=-0.000010 COOLING kappa=inf
2026-03-14 14:42:13,599 - SeedMiner - INFO -   Seed   23 (23/200): delta=0.499560 v_delta=-0.000008 COOLING kappa=inf
2026-03-14 14:42:27,466 - SeedMiner - INFO -   Seed   24 (24/200): delta=0.474706 v_delta=-0.000017 COOLING kappa=inf
2026-03-14 14:42:40,921 - SeedMiner - INFO -   Seed   25 (25/200): delta=0.483567 v_delta=-0.000012 COOLING kappa=inf
2026-03-14 14:42:54,661 - SeedMiner - INFO -   Seed   26 (26/200): delta=0.499798 v_delta=+0.000014 warming kappa~1
2026-03-14 14:43:08,085 - SeedMiner - INFO -   Seed   27 (27/200): delta=0.479649 v_delta=-0.000009 COOLING kappa=inf
2026-03-14 14:43:21,642 - SeedMiner - INFO -   Seed   28 (28/200): delta=0.494400 v_delta=+0.000012 warming kappa=inf
2026-03-14 14:43:34,930 - SeedMiner - INFO -   Seed   29 (29/200): delta=0.489315 v_delta=-0.000012 COOLING kappa~1
2026-03-14 14:43:48,590 - SeedMiner - INFO -   Seed   30 (30/200): delta=0.494171 v_delta=+0.000012 warming kappa=inf
2026-03-14 14:44:02,087 - SeedMiner - INFO -   Seed   31 (31/200): delta=0.496595 v_delta=-0.000014 COOLING kappa~1
2026-03-14 14:44:15,680 - SeedMiner - INFO -   Seed   32 (32/200): delta=0.499099 v_delta=-0.000010 COOLING kappa=inf
2026-03-14 14:44:29,238 - SeedMiner - INFO -   Seed   33 (33/200): delta=0.495829 v_delta=-0.000009 COOLING kappa=inf
2026-03-14 14:44:42,814 - SeedMiner - INFO -   Seed   34 (34/200): delta=0.494370 v_delta=+0.000013 warming kappa~1
2026-03-14 14:44:56,528 - SeedMiner - INFO -   Seed   35 (35/200): delta=0.488895 v_delta=-0.000013 COOLING kappa~1
2026-03-14 14:45:10,204 - SeedMiner - INFO -   Seed   36 (36/200): delta=0.499687 v_delta=-0.000009 COOLING kappa=inf
2026-03-14 14:45:23,857 - SeedMiner - INFO -   Seed   37 (37/200): delta=0.469807 v_delta=-0.000010 COOLING kappa~1
2026-03-14 14:45:37,556 - SeedMiner - INFO -   Seed   38 (38/200): delta=0.489201 v_delta=-0.000014 COOLING kappa~1
2026-03-14 14:45:51,042 - SeedMiner - INFO -   Seed   39 (39/200): delta=0.498171 v_delta=-0.000005 COOLING kappa~1
2026-03-14 14:46:04,881 - SeedMiner - INFO -   Seed   40 (40/200): delta=0.498196 v_delta=-0.000011 COOLING kappa=inf
2026-03-14 14:46:18,630 - SeedMiner - INFO -   Seed   41 (41/200): delta=0.494177 v_delta=-0.000017 COOLING kappa=inf
2026-03-14 14:46:32,544 - SeedMiner - INFO -   Seed   42 (42/200): delta=0.486137 v_delta=-0.000013 COOLING kappa=inf
2026-03-14 14:46:46,244 - SeedMiner - INFO -   Seed   43 (43/200): delta=0.479075 v_delta=+0.000011 warming kappa~1
2026-03-14 14:46:59,826 - SeedMiner - INFO -   Seed   44 (44/200): delta=0.495098 v_delta=+0.000014 warming kappa~1
2026-03-14 14:47:13,294 - SeedMiner - INFO -   Seed   45 (45/200): delta=0.498319 v_delta=+0.000015 warming kappa~1
2026-03-14 14:47:26,849 - SeedMiner - INFO -   Seed   46 (46/200): delta=0.489329 v_delta=-0.000014 COOLING kappa~1
2026-03-14 14:47:40,276 - SeedMiner - INFO -   Seed   47 (47/200): delta=0.481445 v_delta=-0.000013 COOLING kappa=inf
2026-03-14 14:47:53,796 - SeedMiner - INFO -   Seed   48 (48/200): delta=0.479688 v_delta=-0.000009 COOLING kappa=inf
2026-03-14 14:48:07,262 - SeedMiner - INFO -   Seed   49 (49/200): delta=0.493848 v_delta=-0.000011 COOLING kappa=inf
2026-03-14 14:48:20,782 - SeedMiner - INFO -   Seed   50 (50/200): delta=0.486117 v_delta=-0.000012 COOLING kappa~1
2026-03-14 14:48:34,432 - SeedMiner - INFO -   Seed   51 (51/200): delta=0.483538 v_delta=-0.000006 COOLING kappa=inf
2026-03-14 14:48:48,003 - SeedMiner - INFO -   Seed   52 (52/200): delta=0.493386 v_delta=-0.000011 COOLING kappa~1
2026-03-14 14:49:01,637 - SeedMiner - INFO -   Seed   53 (53/200): delta=0.499194 v_delta=+0.000011 warming kappa~1
2026-03-14 14:49:15,329 - SeedMiner - INFO -   Seed   54 (54/200): delta=0.496293 v_delta=-0.000011 COOLING kappa=inf
2026-03-14 14:49:28,670 - SeedMiner - INFO -   Seed   55 (55/200): delta=0.476933 v_delta=-0.000013 COOLING kappa~1
2026-03-14 14:49:42,234 - SeedMiner - INFO -   Seed   56 (56/200): delta=0.492974 v_delta=+0.000014 warming kappa=inf
2026-03-14 14:49:55,744 - SeedMiner - INFO -   Seed   57 (57/200): delta=0.489327 v_delta=-0.000013 COOLING kappa=inf
2026-03-14 14:50:09,244 - SeedMiner - INFO -   Seed   58 (58/200): delta=0.488178 v_delta=-0.000014 COOLING kappa~1
2026-03-14 14:50:22,801 - SeedMiner - INFO -   Seed   59 (59/200): delta=0.498265 v_delta=+0.000009 warming kappa~1
2026-03-14 14:50:36,362 - SeedMiner - INFO -   Seed   60 (60/200): delta=0.499928 v_delta=+0.000010 warming kappa=inf
2026-03-14 14:50:49,820 - SeedMiner - INFO -   Seed   61 (61/200): delta=0.485277 v_delta=-0.000013 COOLING kappa=inf
2026-03-14 14:51:03,567 - SeedMiner - INFO -   Seed   62 (62/200): delta=0.496281 v_delta=+0.000015 warming kappa=inf
2026-03-14 14:51:17,251 - SeedMiner - INFO -   Seed   63 (63/200): delta=0.495797 v_delta=-0.000011 COOLING kappa~1
2026-03-14 14:51:31,398 - SeedMiner - INFO -   Seed   64 (64/200): delta=0.493726 v_delta=-0.000008 COOLING kappa~1
2026-03-14 14:51:45,001 - SeedMiner - INFO -   Seed   65 (65/200): delta=0.492807 v_delta=+0.000012 warming kappa~1
2026-03-14 14:51:58,769 - SeedMiner - INFO -   Seed   66 (66/200): delta=0.499576 v_delta=-0.000013 COOLING kappa=inf
2026-03-14 14:52:12,081 - SeedMiner - INFO -   Seed   67 (67/200): delta=0.499423 v_delta=+0.000012 warming kappa=inf
2026-03-14 14:52:25,731 - SeedMiner - INFO -   Seed   68 (68/200): delta=0.499854 v_delta=+0.000007 warming kappa=inf
2026-03-14 14:52:39,192 - SeedMiner - INFO -   Seed   69 (69/200): delta=0.492054 v_delta=-0.000013 COOLING kappa~1
2026-03-14 14:52:52,648 - SeedMiner - INFO -   Seed   70 (70/200): delta=0.459889 v_delta=-0.000011 COOLING kappa=inf
2026-03-14 14:53:06,149 - SeedMiner - INFO -   Seed   71 (71/200): delta=0.495847 v_delta=+0.000012 warming kappa~1
2026-03-14 14:53:19,599 - SeedMiner - INFO -   Seed   72 (72/200): delta=0.496302 v_delta=+0.000012 warming kappa=inf
2026-03-14 14:53:33,044 - SeedMiner - INFO -   Seed   73 (73/200): delta=0.476773 v_delta=-0.000012 COOLING kappa~1
2026-03-14 14:53:46,491 - SeedMiner - INFO -   Seed   74 (74/200): delta=0.487474 v_delta=-0.000016 COOLING kappa=inf
2026-03-14 14:53:59,923 - SeedMiner - INFO -   Seed   75 (75/200): delta=0.498229 v_delta=-0.000014 COOLING kappa=inf
2026-03-14 14:54:13,201 - SeedMiner - INFO -   Seed   76 (76/200): delta=0.496647 v_delta=-0.000013 COOLING kappa=inf
2026-03-14 14:54:26,527 - SeedMiner - INFO -   Seed   77 (77/200): delta=0.482311 v_delta=-0.000013 COOLING kappa~1
2026-03-14 14:54:39,801 - SeedMiner - INFO -   Seed   78 (78/200): delta=0.493398 v_delta=+0.000009 warming kappa~1
2026-03-14 14:54:53,086 - SeedMiner - INFO -   Seed   79 (79/200): delta=0.496519 v_delta=-0.000013 COOLING kappa~1
2026-03-14 14:55:06,388 - SeedMiner - INFO -   Seed   80 (80/200): delta=0.493449 v_delta=+0.000010 warming kappa=inf
2026-03-14 14:55:19,743 - SeedMiner - INFO -   Seed   81 (81/200): delta=0.495632 v_delta=+0.000016 warming kappa~1
2026-03-14 14:55:33,625 - SeedMiner - INFO -   Seed   82 (82/200): delta=0.484269 v_delta=+0.000011 warming kappa=inf
2026-03-14 14:55:47,217 - SeedMiner - INFO -   Seed   83 (83/200): delta=0.491438 v_delta=+0.000012 warming kappa=inf
2026-03-14 14:56:00,624 - SeedMiner - INFO -   Seed   84 (84/200): delta=0.474734 v_delta=-0.000014 COOLING kappa=inf
2026-03-14 14:56:14,184 - SeedMiner - INFO -   Seed   85 (85/200): delta=0.473270 v_delta=-0.000012 COOLING kappa=inf
2026-03-14 14:56:27,639 - SeedMiner - INFO -   Seed   86 (86/200): delta=0.497016 v_delta=-0.000014 COOLING kappa~1
2026-03-14 14:56:41,061 - SeedMiner - INFO -   Seed   87 (87/200): delta=0.487303 v_delta=-0.000014 COOLING kappa~1
2026-03-14 14:56:54,707 - SeedMiner - INFO -   Seed   88 (88/200): delta=0.483317 v_delta=-0.000016 COOLING kappa=inf
2026-03-14 14:57:08,256 - SeedMiner - INFO -   Seed   89 (89/200): delta=0.485894 v_delta=-0.000015 COOLING kappa=inf
2026-03-14 14:57:21,807 - SeedMiner - INFO -   Seed   90 (90/200): delta=0.483799 v_delta=-0.000010 COOLING kappa~1
2026-03-14 14:57:35,190 - SeedMiner - INFO -   Seed   91 (91/200): delta=0.487823 v_delta=-0.000012 COOLING kappa=inf
2026-03-14 14:57:48,630 - SeedMiner - INFO -   Seed   92 (92/200): delta=0.491479 v_delta=-0.000015 COOLING kappa~1
2026-03-14 14:58:02,381 - SeedMiner - INFO -   Seed   93 (93/200): delta=0.482251 v_delta=-0.000011 COOLING kappa=inf
2026-03-14 14:58:17,135 - SeedMiner - INFO -   Seed   94 (94/200): delta=0.486697 v_delta=-0.000014 COOLING kappa=inf
2026-03-14 14:58:32,417 - SeedMiner - INFO -   Seed   95 (95/200): delta=0.496019 v_delta=+0.000015 warming kappa~1
2026-03-14 14:58:48,220 - SeedMiner - INFO -   Seed   96 (96/200): delta=0.470769 v_delta=-0.000012 COOLING kappa=inf
2026-03-14 14:59:03,859 - SeedMiner - INFO -   Seed   97 (97/200): delta=0.495870 v_delta=+0.000013 warming kappa=inf
2026-03-14 14:59:20,585 - SeedMiner - INFO -   Seed   98 (98/200): delta=0.480382 v_delta=-0.000013 COOLING kappa=inf
2026-03-14 14:59:35,655 - SeedMiner - INFO -   Seed   99 (99/200): delta=0.452344 v_delta=-0.000015 COOLING kappa=inf
2026-03-14 14:59:50,459 - SeedMiner - INFO -   Seed  100 (100/200): delta=0.497708 v_delta=+0.000016 warming kappa=inf
2026-03-14 15:00:06,565 - SeedMiner - INFO -   Seed  101 (101/200): delta=0.488678 v_delta=-0.000013 COOLING kappa=inf
2026-03-14 15:00:22,020 - SeedMiner - INFO -   Seed  102 (102/200): delta=0.494780 v_delta=-0.000013 COOLING kappa~1
2026-03-14 15:00:37,873 - SeedMiner - INFO -   Seed  103 (103/200): delta=0.458811 v_delta=-0.000010 COOLING kappa=inf
2026-03-14 15:00:53,587 - SeedMiner - INFO -   Seed  104 (104/200): delta=0.497814 v_delta=-0.000013 COOLING kappa~1
2026-03-14 15:01:08,511 - SeedMiner - INFO -   Seed  105 (105/200): delta=0.495215 v_delta=+0.000014 warming kappa~1
2026-03-14 15:01:22,943 - SeedMiner - INFO -   Seed  106 (106/200): delta=0.471560 v_delta=-0.000008 COOLING kappa=inf
2026-03-14 15:01:37,564 - SeedMiner - INFO -   Seed  107 (107/200): delta=0.494571 v_delta=+0.000011 warming kappa~1
2026-03-14 15:01:52,377 - SeedMiner - INFO -   Seed  108 (108/200): delta=0.496616 v_delta=-0.000011 COOLING kappa~1
2026-03-14 15:02:08,012 - SeedMiner - INFO -   Seed  109 (109/200): delta=0.499542 v_delta=-0.000015 COOLING kappa~1
2026-03-14 15:02:23,179 - SeedMiner - INFO -   Seed  110 (110/200): delta=0.462747 v_delta=-0.000012 COOLING kappa=inf
2026-03-14 15:02:38,854 - SeedMiner - INFO -   Seed  111 (111/200): delta=0.497768 v_delta=-0.000010 COOLING kappa=inf
2026-03-14 15:02:55,731 - SeedMiner - INFO -   Seed  112 (112/200): delta=0.490640 v_delta=-0.000009 COOLING kappa~1
2026-03-14 15:03:13,982 - SeedMiner - INFO -   Seed  113 (113/200): delta=0.497484 v_delta=-0.000012 COOLING kappa~1
2026-03-14 15:03:30,213 - SeedMiner - INFO -   Seed  114 (114/200): delta=0.493212 v_delta=-0.000013 COOLING kappa=inf
2026-03-14 15:03:44,594 - SeedMiner - INFO -   Seed  115 (115/200): delta=0.491966 v_delta=-0.000010 COOLING kappa~1
2026-03-14 15:03:57,999 - SeedMiner - INFO -   Seed  116 (116/200): delta=0.493353 v_delta=+0.000009 warming kappa~1
2026-03-14 15:04:11,287 - SeedMiner - INFO -   Seed  117 (117/200): delta=0.488304 v_delta=+0.000014 warming kappa=inf
2026-03-14 15:04:24,542 - SeedMiner - INFO -   Seed  118 (118/200): delta=0.496567 v_delta=+0.000010 warming kappa=inf
2026-03-14 15:04:37,812 - SeedMiner - INFO -   Seed  119 (119/200): delta=0.490669 v_delta=-0.000013 COOLING kappa=inf
2026-03-14 15:04:51,116 - SeedMiner - INFO -   Seed  120 (120/200): delta=0.488035 v_delta=-0.000015 COOLING kappa=inf
2026-03-14 15:05:04,370 - SeedMiner - INFO -   Seed  121 (121/200): delta=0.493069 v_delta=-0.000012 COOLING kappa=inf
2026-03-14 15:05:17,740 - SeedMiner - INFO -   Seed  122 (122/200): delta=0.498951 v_delta=+0.000014 warming kappa=inf
2026-03-14 15:05:31,171 - SeedMiner - INFO -   Seed  123 (123/200): delta=0.485061 v_delta=+0.000013 warming kappa~1
2026-03-14 15:05:44,544 - SeedMiner - INFO -   Seed  124 (124/200): delta=0.495202 v_delta=-0.000011 COOLING kappa=inf
2026-03-14 15:05:57,849 - SeedMiner - INFO -   Seed  125 (125/200): delta=0.499898 v_delta=+0.000013 warming kappa~1
2026-03-14 15:06:11,191 - SeedMiner - INFO -   Seed  126 (126/200): delta=0.491134 v_delta=-0.000014 COOLING kappa=inf
2026-03-14 15:06:24,544 - SeedMiner - INFO -   Seed  127 (127/200): delta=0.499035 v_delta=+0.000016 warming kappa=inf
2026-03-14 15:06:37,844 - SeedMiner - INFO -   Seed  128 (128/200): delta=0.490741 v_delta=-0.000013 COOLING kappa~1
2026-03-14 15:06:51,354 - SeedMiner - INFO -   Seed  129 (129/200): delta=0.477239 v_delta=-0.000012 COOLING kappa~1
2026-03-14 15:07:04,663 - SeedMiner - INFO -   Seed  130 (130/200): delta=0.493956 v_delta=-0.000014 COOLING kappa=inf
2026-03-14 15:07:17,820 - SeedMiner - INFO -   Seed  131 (131/200): delta=0.499406 v_delta=+0.000013 warming kappa=inf
2026-03-14 15:07:31,202 - SeedMiner - INFO -   Seed  132 (132/200): delta=0.467981 v_delta=-0.000013 COOLING kappa~1
2026-03-14 15:07:44,666 - SeedMiner - INFO -   Seed  133 (133/200): delta=0.488106 v_delta=-0.000011 COOLING kappa~1
2026-03-14 15:07:58,021 - SeedMiner - INFO -   Seed  134 (134/200): delta=0.480843 v_delta=-0.000013 COOLING kappa=inf
2026-03-14 15:08:11,266 - SeedMiner - INFO -   Seed  135 (135/200): delta=0.497469 v_delta=+0.000012 warming kappa=inf
2026-03-14 15:08:24,492 - SeedMiner - INFO -   Seed  136 (136/200): delta=0.481880 v_delta=-0.000012 COOLING kappa=inf
2026-03-14 15:08:37,909 - SeedMiner - INFO -   Seed  137 (137/200): delta=0.497795 v_delta=+0.000014 warming kappa=inf
2026-03-14 15:08:51,094 - SeedMiner - INFO -   Seed  138 (138/200): delta=0.499029 v_delta=-0.000013 COOLING kappa=inf
2026-03-14 15:09:04,572 - SeedMiner - INFO -   Seed  139 (139/200): delta=0.492244 v_delta=-0.000013 COOLING kappa=inf
2026-03-14 15:09:17,801 - SeedMiner - INFO -   Seed  140 (140/200): delta=0.484488 v_delta=-0.000014 COOLING kappa=inf
2026-03-14 15:09:31,295 - SeedMiner - INFO -   Seed  141 (141/200): delta=0.496530 v_delta=-0.000011 COOLING kappa~1
2026-03-14 15:09:44,726 - SeedMiner - INFO -   Seed  142 (142/200): delta=0.489637 v_delta=-0.000011 COOLING kappa=inf
2026-03-14 15:09:57,874 - SeedMiner - INFO -   Seed  143 (143/200): delta=0.497921 v_delta=-0.000010 COOLING kappa=inf
2026-03-14 15:10:11,125 - SeedMiner - INFO -   Seed  144 (144/200): delta=0.491986 v_delta=-0.000010 COOLING kappa~1
2026-03-14 15:10:24,347 - SeedMiner - INFO -   Seed  145 (145/200): delta=0.475963 v_delta=+0.000012 warming kappa=inf
2026-03-14 15:10:37,568 - SeedMiner - INFO -   Seed  146 (146/200): delta=0.488579 v_delta=+0.000013 warming kappa=inf
2026-03-14 15:10:50,835 - SeedMiner - INFO -   Seed  147 (147/200): delta=0.491547 v_delta=+0.000016 warming kappa=inf
2026-03-14 15:11:04,167 - SeedMiner - INFO -   Seed  148 (148/200): delta=0.486213 v_delta=-0.000009 COOLING kappa~1
2026-03-14 15:11:17,421 - SeedMiner - INFO -   Seed  149 (149/200): delta=0.493131 v_delta=+0.000014 warming kappa~1
2026-03-14 15:11:30,832 - SeedMiner - INFO -   Seed  150 (150/200): delta=0.492038 v_delta=+0.000008 warming kappa~1
2026-03-14 15:11:44,078 - SeedMiner - INFO -   Seed  151 (151/200): delta=0.476648 v_delta=-0.000013 COOLING kappa=inf
2026-03-14 15:11:57,207 - SeedMiner - INFO -   Seed  152 (152/200): delta=0.491706 v_delta=+0.000013 warming kappa=inf
2026-03-14 15:12:10,431 - SeedMiner - INFO -   Seed  153 (153/200): delta=0.497821 v_delta=-0.000012 COOLING kappa~1
2026-03-14 15:12:23,687 - SeedMiner - INFO -   Seed  154 (154/200): delta=0.495742 v_delta=-0.000014 COOLING kappa=inf
2026-03-14 15:12:36,864 - SeedMiner - INFO -   Seed  155 (155/200): delta=0.489303 v_delta=-0.000015 COOLING kappa=inf
2026-03-14 15:12:50,238 - SeedMiner - INFO -   Seed  156 (156/200): delta=0.497806 v_delta=+0.000015 warming kappa~1
2026-03-14 15:13:03,703 - SeedMiner - INFO -   Seed  157 (157/200): delta=0.497173 v_delta=+0.000011 warming kappa=inf
2026-03-14 15:13:17,211 - SeedMiner - INFO -   Seed  158 (158/200): delta=0.497314 v_delta=-0.000011 COOLING kappa~1
2026-03-14 15:13:30,692 - SeedMiner - INFO -   Seed  159 (159/200): delta=0.487673 v_delta=-0.000012 COOLING kappa=inf
2026-03-14 15:13:44,032 - SeedMiner - INFO -   Seed  160 (160/200): delta=0.492339 v_delta=-0.000011 COOLING kappa=inf
2026-03-14 15:13:57,233 - SeedMiner - INFO -   Seed  161 (161/200): delta=0.497515 v_delta=+0.000011 warming kappa~1
2026-03-14 15:14:10,626 - SeedMiner - INFO -   Seed  162 (162/200): delta=0.497677 v_delta=+0.000012 warming kappa=inf
2026-03-14 15:14:23,914 - SeedMiner - INFO -   Seed  163 (163/200): delta=0.487662 v_delta=-0.000019 COOLING kappa=inf
2026-03-14 15:14:37,417 - SeedMiner - INFO -   Seed  164 (164/200): delta=0.491370 v_delta=+0.000009 warming kappa=inf
2026-03-14 15:14:50,799 - SeedMiner - INFO -   Seed  165 (165/200): delta=0.497576 v_delta=-0.000012 COOLING kappa~1
2026-03-14 15:15:04,045 - SeedMiner - INFO -   Seed  166 (166/200): delta=0.473180 v_delta=-0.000011 COOLING kappa~1
2026-03-14 15:15:17,515 - SeedMiner - INFO -   Seed  167 (167/200): delta=0.472062 v_delta=-0.000012 COOLING kappa=inf
2026-03-14 15:15:30,890 - SeedMiner - INFO -   Seed  168 (168/200): delta=0.494515 v_delta=+0.000010 warming kappa=inf
2026-03-14 15:15:44,243 - SeedMiner - INFO -   Seed  169 (169/200): delta=0.497977 v_delta=-0.000011 COOLING kappa=inf
2026-03-14 15:15:57,414 - SeedMiner - INFO -   Seed  170 (170/200): delta=0.488861 v_delta=+0.000013 warming kappa=inf
2026-03-14 15:16:10,644 - SeedMiner - INFO -   Seed  171 (171/200): delta=0.498911 v_delta=-0.000010 COOLING kappa=inf
2026-03-14 15:16:23,882 - SeedMiner - INFO -   Seed  172 (172/200): delta=0.488909 v_delta=-0.000016 COOLING kappa~1
2026-03-14 15:16:37,188 - SeedMiner - INFO -   Seed  173 (173/200): delta=0.495123 v_delta=-0.000006 COOLING kappa=inf
2026-03-14 15:16:50,685 - SeedMiner - INFO -   Seed  174 (174/200): delta=0.464687 v_delta=+0.000012 warming kappa=inf
2026-03-14 15:17:04,114 - SeedMiner - INFO -   Seed  175 (175/200): delta=0.476338 v_delta=-0.000009 COOLING kappa=inf
2026-03-14 15:17:17,942 - SeedMiner - INFO -   Seed  176 (176/200): delta=0.474632 v_delta=-0.000011 COOLING kappa~1
2026-03-14 15:17:31,147 - SeedMiner - INFO -   Seed  177 (177/200): delta=0.488324 v_delta=-0.000012 COOLING kappa=inf
2026-03-14 15:17:44,493 - SeedMiner - INFO -   Seed  178 (178/200): delta=0.479186 v_delta=+0.000010 warming kappa~1
2026-03-14 15:17:57,803 - SeedMiner - INFO -   Seed  179 (179/200): delta=0.498116 v_delta=+0.000014 warming kappa=inf
2026-03-14 15:18:11,232 - SeedMiner - INFO -   Seed  180 (180/200): delta=0.499825 v_delta=+0.000013 warming kappa~1
2026-03-14 15:18:24,738 - SeedMiner - INFO -   Seed  181 (181/200): delta=0.464020 v_delta=-0.000012 COOLING kappa=inf
2026-03-14 15:18:38,055 - SeedMiner - INFO -   Seed  182 (182/200): delta=0.493987 v_delta=-0.000012 COOLING kappa~1
2026-03-14 15:18:51,400 - SeedMiner - INFO -   Seed  183 (183/200): delta=0.499871 v_delta=+0.000002 warming kappa=inf
2026-03-14 15:19:04,874 - SeedMiner - INFO -   Seed  184 (184/200): delta=0.496983 v_delta=-0.000012 COOLING kappa=inf
2026-03-14 15:19:18,317 - SeedMiner - INFO -   Seed  185 (185/200): delta=0.496548 v_delta=+0.000009 warming kappa=inf
2026-03-14 15:19:31,683 - SeedMiner - INFO -   Seed  186 (186/200): delta=0.457881 v_delta=-0.000012 COOLING kappa~1
2026-03-14 15:19:45,116 - SeedMiner - INFO -   Seed  187 (187/200): delta=0.489905 v_delta=+0.000014 warming kappa~1
2026-03-14 15:19:58,765 - SeedMiner - INFO -   Seed  188 (188/200): delta=0.494684 v_delta=-0.000010 COOLING kappa~1
2026-03-14 15:20:12,260 - SeedMiner - INFO -   Seed  189 (189/200): delta=0.493890 v_delta=+0.000013 warming kappa=inf
2026-03-14 15:20:25,624 - SeedMiner - INFO -   Seed  190 (190/200): delta=0.491724 v_delta=-0.000012 COOLING kappa~1
2026-03-14 15:20:39,215 - SeedMiner - INFO -   Seed  191 (191/200): delta=0.496543 v_delta=-0.000012 COOLING kappa=inf
2026-03-14 15:20:52,723 - SeedMiner - INFO -   Seed  192 (192/200): delta=0.483433 v_delta=+0.000012 warming kappa~1
2026-03-14 15:21:06,473 - SeedMiner - INFO -   Seed  193 (193/200): delta=0.488254 v_delta=-0.000018 COOLING kappa=inf
2026-03-14 15:21:19,738 - SeedMiner - INFO -   Seed  194 (194/200): delta=0.493570 v_delta=+0.000009 warming kappa=inf
2026-03-14 15:21:33,238 - SeedMiner - INFO -   Seed  195 (195/200): delta=0.497423 v_delta=-0.000011 COOLING kappa=inf
2026-03-14 15:21:46,499 - SeedMiner - INFO -   Seed  196 (196/200): delta=0.484979 v_delta=-0.000021 COOLING kappa~1
2026-03-14 15:21:59,987 - SeedMiner - INFO -   Seed  197 (197/200): delta=0.492066 v_delta=-0.000012 COOLING kappa=inf
2026-03-14 15:22:13,324 - SeedMiner - INFO -   Seed  198 (198/200): delta=0.495272 v_delta=+0.000013 warming kappa~1
2026-03-14 15:22:26,747 - SeedMiner - INFO -   Seed  199 (199/200): delta=0.466012 v_delta=-0.000008 COOLING kappa=inf
2026-03-14 15:22:40,101 - SeedMiner - INFO -   Seed  200 (200/200): delta=0.497810 v_delta=-0.000014 COOLING kappa~1
2026-03-14 15:22:40,102 - SeedMiner - INFO - Phase 2 complete: Best seed=186 (delta=0.457881, v_delta=-0.000012, kappa=1.00e+00)
2026-03-14 15:22:40,105 - FullTrainingOrchestrator - INFO - Phase 3: Full training started (seed=186, batch_size=32, epochs=5000, start_epoch=0)
2026-03-14 15:26:06,445 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 10/5000
Loss=0.007760 ValLoss=0.002035 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1991 Alpha=0.7804 Kappa=1.00e+00 Kappa_q=1.12e+04
Delta=0.458242 Purity=0.5418 Crystal=0
T_eff=2.48e-25 C_v=4.69e+10 Poynting=2.40e-02 E_flow=2.40e-02
Lambda=1.00e+00 hbar_eff=2.10e-01 S_spectral=8.3541 Bragg=10
LR=5.00e-03 AnnealT=0.00e+00 dDelta/dt=0.00e+00 NormErr=4.61e-01
Gibbs=4.5824e-01 T_crit=6.77e-04 SpecGap=2.1317e-02 PartRatio=1.0000
LvlSpacing=0.5321 Ricci=2.22e+15 Stability=S
Topo[CM_x=-0.1881 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 15:27:53,801 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_15_20260314_152753.pth
2026-03-14 15:29:33,465 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 20/5000
Loss=0.006272 ValLoss=0.000770 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1990 Alpha=0.7806 Kappa=1.00e+00 Kappa_q=1.12e+04
Delta=0.458127 Purity=0.5419 Crystal=0
T_eff=5.45e-26 C_v=7.12e+10 Poynting=2.39e-02 E_flow=2.39e-02
Lambda=1.00e+00 hbar_eff=2.10e-01 S_spectral=8.3541 Bragg=10
LR=5.00e-03 AnnealT=0.00e+00 dDelta/dt=0.00e+00 NormErr=5.69e-01
Gibbs=4.5813e-01 T_crit=6.77e-04 SpecGap=2.1307e-02 PartRatio=1.0000
LvlSpacing=0.5362 Ricci=2.22e+15 Stability=S
Topo[CM_x=-0.1881 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 15:32:52,856 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 30/5000
Loss=0.006142 ValLoss=0.000663 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7808 Kappa=1.00e+00 Kappa_q=1.12e+04
Delta=0.458018 Purity=0.5420 Crystal=0
T_eff=1.09e-26 C_v=6.32e+10 Poynting=2.38e-02 E_flow=2.38e-02
Lambda=1.00e+00 hbar_eff=2.10e-01 S_spectral=8.3541 Bragg=10
LR=5.00e-03 AnnealT=0.00e+00 dDelta/dt=0.00e+00 NormErr=8.58e-01
Gibbs=4.5802e-01 T_crit=6.77e-04 SpecGap=2.1296e-02 PartRatio=1.0000
LvlSpacing=0.5274 Ricci=2.24e+15 Stability=S
Topo[CM_x=-0.1881 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 15:33:12,717 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_31_20260314_153312.pth
2026-03-14 15:36:17,619 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 40/5000
Loss=0.006125 ValLoss=0.000652 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7811 Kappa=1.00e+00 Kappa_q=1.12e+04
Delta=0.457904 Purity=0.5421 Crystal=0
T_eff=9.11e-27 C_v=5.34e+10 Poynting=2.38e-02 E_flow=2.38e-02
Lambda=1.00e+00 hbar_eff=2.10e-01 S_spectral=8.3541 Bragg=10
LR=5.00e-03 AnnealT=0.00e+00 dDelta/dt=0.00e+00 NormErr=9.57e-01
Gibbs=4.5790e-01 T_crit=6.77e-04 SpecGap=2.1285e-02 PartRatio=1.0000
LvlSpacing=0.5416 Ricci=2.22e+15 Stability=S
Topo[CM_x=-0.1881 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 15:38:16,340 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_46_20260314_153816.pth
2026-03-14 15:39:34,576 - FullTrainingOrchestrator - INFO -   GROKKING detected at epoch 50: train_acc=1.0000, val_acc=1.0000, delta=0.457775, delta_slope=-1.13e-05
2026-03-14 15:39:34,576 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 50/5000
Loss=0.006121 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7814 Kappa=inf Kappa_q=1.12e+04
Delta=0.457775 Purity=0.5422 Crystal=0
T_eff=8.89e-27 C_v=4.56e+10 Poynting=2.38e-02 E_flow=2.38e-02
Lambda=1.00e+00 hbar_eff=2.10e-01 S_spectral=8.3541 Bragg=10
LR=5.00e-03 AnnealT=0.00e+00 dDelta/dt=0.00e+00 NormErr=9.86e-01
Gibbs=4.5778e-01 T_crit=6.77e-04 SpecGap=2.1275e-02 PartRatio=1.0000
LvlSpacing=0.5338 Ricci=2.25e+15 Stability=S
Topo[CM_x=-0.1881 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 15:42:51,107 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 60/5000
Loss=0.006118 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7817 Kappa=inf Kappa_q=1.12e+04
Delta=0.457620 Purity=0.5424 Crystal=0
T_eff=1.01e-26 C_v=1.18e+09 Poynting=2.37e-02 E_flow=2.37e-02
Lambda=1.00e+00 hbar_eff=2.09e-01 S_spectral=8.3541 Bragg=10
LR=5.00e-03 AnnealT=0.00e+00 dDelta/dt=-1.22e-05 NormErr=9.92e-01
Gibbs=4.5762e-01 T_crit=6.76e-04 SpecGap=2.1263e-02 PartRatio=1.0000
LvlSpacing=0.5301 Ricci=2.25e+15 Stability=S
Topo[CM_x=-0.1881 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 15:43:29,045 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_62_20260314_154328.pth
2026-03-14 15:46:02,504 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 70/5000
Loss=0.006115 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7820 Kappa=inf Kappa_q=1.12e+04
Delta=0.457505 Purity=0.5425 Crystal=0
T_eff=9.28e-27 C_v=1.05e+07 Poynting=2.37e-02 E_flow=2.37e-02
Lambda=1.00e+00 hbar_eff=2.09e-01 S_spectral=8.3541 Bragg=10
LR=5.00e-03 AnnealT=0.00e+00 dDelta/dt=-1.29e-05 NormErr=9.94e-01
Gibbs=4.5751e-01 T_crit=6.76e-04 SpecGap=2.1253e-02 PartRatio=1.0000
LvlSpacing=0.5231 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1881 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 15:48:45,494 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_78_20260314_154845.pth
2026-03-14 15:49:24,521 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 80/5000
Loss=0.006113 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7822 Kappa=inf Kappa_q=1.12e+04
Delta=0.457403 Purity=0.5426 Crystal=0
T_eff=8.73e-27 C_v=4.29e+05 Poynting=2.38e-02 E_flow=2.38e-02
Lambda=1.00e+00 hbar_eff=2.09e-01 S_spectral=8.3541 Bragg=10
LR=5.00e-03 AnnealT=0.00e+00 dDelta/dt=-1.30e-05 NormErr=9.94e-01
Gibbs=4.5740e-01 T_crit=6.76e-04 SpecGap=2.1242e-02 PartRatio=1.0000
LvlSpacing=0.5446 Ricci=2.22e+15 Stability=S
Topo[CM_x=-0.1881 Loc=0.2999 Align=0.00 Aniso=0.7001 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 15:53:20,618 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 90/5000
Loss=0.006110 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7824 Kappa=inf Kappa_q=1.11e+04
Delta=0.457289 Purity=0.5427 Crystal=0
T_eff=8.17e-27 C_v=1.73e+05 Poynting=2.37e-02 E_flow=2.37e-02
Lambda=1.00e+00 hbar_eff=2.09e-01 S_spectral=8.3541 Bragg=10
LR=5.00e-03 AnnealT=0.00e+00 dDelta/dt=-1.24e-05 NormErr=9.94e-01
Gibbs=4.5729e-01 T_crit=6.76e-04 SpecGap=2.1232e-02 PartRatio=1.0000
LvlSpacing=0.5201 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1881 Loc=0.2999 Align=0.00 Aniso=0.7001 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 15:54:02,944 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_92_20260314_155402.pth
2026-03-14 15:56:30,362 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 100/5000
Loss=0.006107 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7827 Kappa=inf Kappa_q=1.11e+04
Delta=0.457180 Purity=0.5428 Crystal=0
T_eff=7.82e-27 C_v=1.59e+05 Poynting=2.37e-02 E_flow=2.37e-02
Lambda=1.00e+00 hbar_eff=2.09e-01 S_spectral=8.3541 Bragg=10
LR=5.00e-03 AnnealT=0.00e+00 dDelta/dt=-1.13e-05 NormErr=9.94e-01
Gibbs=4.5718e-01 T_crit=6.76e-04 SpecGap=2.1221e-02 PartRatio=1.0000
LvlSpacing=0.5153 Ricci=2.25e+15 Stability=S
Topo[CM_x=-0.1881 Loc=0.2999 Align=0.00 Aniso=0.7001 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 15:59:15,565 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_109_20260314_155915.pth
2026-03-14 15:59:33,757 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 110/5000
Loss=0.006104 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7830 Kappa=inf Kappa_q=1.11e+04
Delta=0.457055 Purity=0.5429 Crystal=0
T_eff=8.47e-27 C_v=1.57e+05 Poynting=2.37e-02 E_flow=2.37e-02
Lambda=1.00e+00 hbar_eff=2.09e-01 S_spectral=8.3541 Bragg=10
LR=4.99e-03 AnnealT=0.00e+00 dDelta/dt=-1.12e-05 NormErr=9.94e-01
Gibbs=4.5706e-01 T_crit=6.76e-04 SpecGap=2.1210e-02 PartRatio=1.0000
LvlSpacing=0.5190 Ricci=2.22e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:02:35,337 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 120/5000
Loss=0.006102 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7832 Kappa=inf Kappa_q=1.11e+04
Delta=0.456940 Purity=0.5431 Crystal=0
T_eff=9.03e-27 C_v=1.57e+05 Poynting=2.36e-02 E_flow=2.36e-02
Lambda=1.00e+00 hbar_eff=2.09e-01 S_spectral=8.3541 Bragg=10
LR=4.99e-03 AnnealT=0.00e+00 dDelta/dt=-1.14e-05 NormErr=9.94e-01
Gibbs=4.5694e-01 T_crit=6.76e-04 SpecGap=2.1199e-02 PartRatio=1.0000
LvlSpacing=0.5279 Ricci=2.22e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:04:24,597 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_126_20260314_160424.pth
2026-03-14 16:05:37,436 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 130/5000
Loss=0.006099 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7835 Kappa=1.00e+00 Kappa_q=1.11e+04
Delta=0.456810 Purity=0.5432 Crystal=0
T_eff=8.93e-27 C_v=1.57e+05 Poynting=2.37e-02 E_flow=2.37e-02
Lambda=1.00e+00 hbar_eff=2.09e-01 S_spectral=8.3541 Bragg=10
LR=4.99e-03 AnnealT=0.00e+00 dDelta/dt=-1.17e-05 NormErr=9.93e-01
Gibbs=4.5681e-01 T_crit=6.76e-04 SpecGap=2.1188e-02 PartRatio=1.0000
LvlSpacing=0.5461 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1881 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:08:39,030 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 140/5000
Loss=0.006096 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7837 Kappa=inf Kappa_q=1.11e+04
Delta=0.456694 Purity=0.5433 Crystal=0
T_eff=8.63e-27 C_v=1.56e+05 Poynting=2.37e-02 E_flow=2.37e-02
Lambda=1.00e+00 hbar_eff=2.09e-01 S_spectral=8.3541 Bragg=10
LR=4.99e-03 AnnealT=0.00e+00 dDelta/dt=-1.19e-05 NormErr=9.93e-01
Gibbs=4.5669e-01 T_crit=6.76e-04 SpecGap=2.1177e-02 PartRatio=1.0000
LvlSpacing=0.5345 Ricci=2.22e+15 Stability=S
Topo[CM_x=-0.1881 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:09:33,537 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_143_20260314_160933.pth
2026-03-14 16:11:41,068 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 150/5000
Loss=0.006093 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7840 Kappa=inf Kappa_q=1.11e+04
Delta=0.456595 Purity=0.5434 Crystal=0
T_eff=8.88e-27 C_v=1.56e+05 Poynting=2.36e-02 E_flow=2.36e-02
Lambda=1.00e+00 hbar_eff=2.08e-01 S_spectral=8.3541 Bragg=10
LR=4.99e-03 AnnealT=0.00e+00 dDelta/dt=-1.20e-05 NormErr=9.92e-01
Gibbs=4.5660e-01 T_crit=6.76e-04 SpecGap=2.1167e-02 PartRatio=1.0000
LvlSpacing=0.5326 Ricci=2.24e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:14:42,854 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 160/5000
Loss=0.006091 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7841 Kappa=inf Kappa_q=1.11e+04
Delta=0.456513 Purity=0.5435 Crystal=0
T_eff=8.96e-27 C_v=1.56e+05 Poynting=2.36e-02 E_flow=2.36e-02
Lambda=1.00e+00 hbar_eff=2.08e-01 S_spectral=8.3541 Bragg=10
LR=4.99e-03 AnnealT=0.00e+00 dDelta/dt=-1.11e-05 NormErr=9.91e-01
Gibbs=4.5651e-01 T_crit=6.76e-04 SpecGap=2.1156e-02 PartRatio=1.0000
LvlSpacing=0.5332 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:14:42,924 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_160_20260314_161442.pth
2026-03-14 16:17:45,558 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 170/5000
Loss=0.006088 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7844 Kappa=inf Kappa_q=1.11e+04
Delta=0.456399 Purity=0.5436 Crystal=0
T_eff=8.25e-27 C_v=1.56e+05 Poynting=2.35e-02 E_flow=2.35e-02
Lambda=1.00e+00 hbar_eff=2.08e-01 S_spectral=8.3541 Bragg=10
LR=4.99e-03 AnnealT=0.00e+00 dDelta/dt=-1.04e-05 NormErr=9.93e-01
Gibbs=4.5640e-01 T_crit=6.76e-04 SpecGap=2.1146e-02 PartRatio=1.0000
LvlSpacing=0.5336 Ricci=2.22e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:19:53,771 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_177_20260314_161953.pth
2026-03-14 16:20:48,712 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 180/5000
Loss=0.006085 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7844 Kappa=inf Kappa_q=1.11e+04
Delta=0.456390 Purity=0.5436 Crystal=0
T_eff=8.99e-27 C_v=1.56e+05 Poynting=2.35e-02 E_flow=2.35e-02
Lambda=1.00e+00 hbar_eff=2.08e-01 S_spectral=8.3540 Bragg=10
LR=4.98e-03 AnnealT=0.00e+00 dDelta/dt=-9.25e-06 NormErr=9.91e-01
Gibbs=4.5639e-01 T_crit=6.76e-04 SpecGap=2.1135e-02 PartRatio=1.0000
LvlSpacing=0.5180 Ricci=2.24e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:23:51,253 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 190/5000
Loss=0.006083 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7846 Kappa=inf Kappa_q=1.11e+04
Delta=0.456282 Purity=0.5437 Crystal=0
T_eff=9.16e-27 C_v=1.55e+05 Poynting=2.35e-02 E_flow=2.35e-02
Lambda=1.00e+00 hbar_eff=2.08e-01 S_spectral=8.3540 Bragg=10
LR=4.98e-03 AnnealT=0.00e+00 dDelta/dt=-7.84e-06 NormErr=9.92e-01
Gibbs=4.5628e-01 T_crit=6.75e-04 SpecGap=2.1124e-02 PartRatio=1.0000
LvlSpacing=0.5486 Ricci=2.22e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:25:05,336 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_194_20260314_162505.pth
2026-03-14 16:26:55,641 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 200/5000
Loss=0.006080 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7849 Kappa=inf Kappa_q=1.11e+04
Delta=0.456154 Purity=0.5438 Crystal=0
T_eff=8.82e-27 C_v=1.55e+05 Poynting=2.35e-02 E_flow=2.35e-02
Lambda=1.00e+00 hbar_eff=2.08e-01 S_spectral=8.3540 Bragg=10
LR=4.98e-03 AnnealT=0.00e+00 dDelta/dt=-7.96e-06 NormErr=9.93e-01
Gibbs=4.5615e-01 T_crit=6.75e-04 SpecGap=2.1114e-02 PartRatio=1.0000
LvlSpacing=0.5320 Ricci=2.24e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:29:58,768 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 210/5000
Loss=0.006077 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7852 Kappa=1.00e+00 Kappa_q=1.11e+04
Delta=0.456039 Purity=0.5440 Crystal=0
T_eff=8.97e-27 C_v=1.55e+05 Poynting=2.35e-02 E_flow=2.35e-02
Lambda=1.00e+00 hbar_eff=2.08e-01 S_spectral=8.3540 Bragg=10
LR=4.98e-03 AnnealT=0.00e+00 dDelta/dt=-8.72e-06 NormErr=9.94e-01
Gibbs=4.5604e-01 T_crit=6.75e-04 SpecGap=2.1103e-02 PartRatio=1.0000
LvlSpacing=0.5382 Ricci=2.22e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:30:17,281 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_211_20260314_163017.pth
2026-03-14 16:33:09,288 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 220/5000
Loss=0.006074 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7854 Kappa=inf Kappa_q=1.11e+04
Delta=0.455924 Purity=0.5441 Crystal=0
T_eff=8.19e-27 C_v=1.55e+05 Poynting=2.34e-02 E_flow=2.34e-02
Lambda=1.00e+00 hbar_eff=2.08e-01 S_spectral=8.3540 Bragg=10
LR=4.98e-03 AnnealT=0.00e+00 dDelta/dt=-1.03e-05 NormErr=9.94e-01
Gibbs=4.5592e-01 T_crit=6.75e-04 SpecGap=2.1093e-02 PartRatio=1.0000
LvlSpacing=0.5241 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:35:32,504 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_227_20260314_163532.pth
2026-03-14 16:36:42,876 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 230/5000
Loss=0.006072 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7854 Kappa=1.00e+00 Kappa_q=1.11e+04
Delta=0.455954 Purity=0.5440 Crystal=0
T_eff=7.45e-27 C_v=1.55e+05 Poynting=2.35e-02 E_flow=2.35e-02
Lambda=1.00e+00 hbar_eff=2.08e-01 S_spectral=8.3540 Bragg=10
LR=4.97e-03 AnnealT=0.00e+00 dDelta/dt=-1.07e-05 NormErr=9.93e-01
Gibbs=4.5595e-01 T_crit=6.75e-04 SpecGap=2.1081e-02 PartRatio=1.0000
LvlSpacing=0.5384 Ricci=2.26e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2999 Align=0.00 Aniso=0.7001 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6429 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:40:30,626 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 240/5000
Loss=0.006069 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7856 Kappa=inf Kappa_q=1.11e+04
Delta=0.455847 Purity=0.5442 Crystal=0
T_eff=9.21e-27 C_v=1.54e+05 Poynting=2.34e-02 E_flow=2.34e-02
Lambda=1.00e+00 hbar_eff=2.08e-01 S_spectral=8.3540 Bragg=10
LR=4.97e-03 AnnealT=0.00e+00 dDelta/dt=-8.20e-06 NormErr=9.93e-01
Gibbs=4.5585e-01 T_crit=6.75e-04 SpecGap=2.1071e-02 PartRatio=1.0000
LvlSpacing=0.5270 Ricci=2.24e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2999 Align=0.00 Aniso=0.7001 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6429 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:40:53,767 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_241_20260314_164053.pth
2026-03-14 16:44:31,776 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 250/5000
Loss=0.006066 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7859 Kappa=inf Kappa_q=1.11e+04
Delta=0.455732 Purity=0.5443 Crystal=0
T_eff=8.37e-27 C_v=1.54e+05 Poynting=2.34e-02 E_flow=2.34e-02
Lambda=1.00e+00 hbar_eff=2.08e-01 S_spectral=8.3540 Bragg=10
LR=4.97e-03 AnnealT=0.00e+00 dDelta/dt=-6.95e-06 NormErr=9.94e-01
Gibbs=4.5573e-01 T_crit=6.75e-04 SpecGap=2.1060e-02 PartRatio=1.0000
LvlSpacing=0.5281 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2999 Align=0.00 Aniso=0.7001 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6429 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:46:06,250 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_254_20260314_164606.pth
2026-03-14 16:48:32,239 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 260/5000
Loss=0.006064 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7861 Kappa=inf Kappa_q=1.11e+04
Delta=0.455624 Purity=0.5444 Crystal=0
T_eff=8.40e-27 C_v=1.54e+05 Poynting=2.36e-02 E_flow=2.36e-02
Lambda=1.00e+00 hbar_eff=2.08e-01 S_spectral=8.3540 Bragg=10
LR=4.97e-03 AnnealT=0.00e+00 dDelta/dt=-7.33e-06 NormErr=9.94e-01
Gibbs=4.5562e-01 T_crit=6.75e-04 SpecGap=2.1049e-02 PartRatio=1.0000
LvlSpacing=0.5087 Ricci=2.24e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2999 Align=0.00 Aniso=0.7001 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6429 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:51:54,898 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_267_20260314_165154.pth
2026-03-14 16:55:57,723 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 270/5000
Loss=0.006061 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7863 Kappa=inf Kappa_q=1.10e+04
Delta=0.455510 Purity=0.5445 Crystal=0
T_eff=8.11e-27 C_v=1.53e+05 Poynting=2.35e-02 E_flow=2.35e-02
Lambda=1.00e+00 hbar_eff=2.07e-01 S_spectral=8.3540 Bragg=10
LR=4.96e-03 AnnealT=0.00e+00 dDelta/dt=-9.18e-06 NormErr=9.94e-01
Gibbs=4.5551e-01 T_crit=6.75e-04 SpecGap=2.1038e-02 PartRatio=1.0000
LvlSpacing=0.5426 Ricci=2.22e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2999 Align=0.00 Aniso=0.7001 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6429 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 16:57:12,651 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_271_20260314_165712.pth
2026-03-14 17:02:14,264 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_279_20260314_170214.pth
2026-03-14 17:02:33,348 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 280/5000
Loss=0.006058 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7866 Kappa=1.00e+00 Kappa_q=1.10e+04
Delta=0.455391 Purity=0.5446 Crystal=0
T_eff=7.89e-27 C_v=1.53e+05 Poynting=2.35e-02 E_flow=2.35e-02
Lambda=1.00e+00 hbar_eff=2.07e-01 S_spectral=8.3540 Bragg=10
LR=4.96e-03 AnnealT=0.00e+00 dDelta/dt=-1.13e-05 NormErr=9.92e-01
Gibbs=4.5539e-01 T_crit=6.75e-04 SpecGap=2.1028e-02 PartRatio=1.0000
LvlSpacing=0.5444 Ricci=2.22e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 17:07:02,641 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 290/5000
Loss=0.006055 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7868 Kappa=inf Kappa_q=1.10e+04
Delta=0.455278 Purity=0.5447 Crystal=0
T_eff=8.05e-27 C_v=1.53e+05 Poynting=2.35e-02 E_flow=2.35e-02
Lambda=1.00e+00 hbar_eff=2.07e-01 S_spectral=8.3540 Bragg=10
LR=4.96e-03 AnnealT=0.00e+00 dDelta/dt=-1.14e-05 NormErr=9.93e-01
Gibbs=4.5528e-01 T_crit=6.75e-04 SpecGap=2.1017e-02 PartRatio=1.0000
LvlSpacing=0.5214 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 17:07:34,631 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_291_20260314_170734.pth
2026-03-14 17:12:25,811 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 300/5000
Loss=0.006053 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7871 Kappa=inf Kappa_q=1.10e+04
Delta=0.455171 Purity=0.5448 Crystal=0
T_eff=8.11e-27 C_v=1.52e+05 Poynting=2.34e-02 E_flow=2.34e-02
Lambda=1.00e+00 hbar_eff=2.07e-01 S_spectral=8.3540 Bragg=10
LR=4.96e-03 AnnealT=0.00e+00 dDelta/dt=-1.15e-05 NormErr=9.94e-01
Gibbs=4.5517e-01 T_crit=6.75e-04 SpecGap=2.1006e-02 PartRatio=1.0000
LvlSpacing=0.5443 Ricci=2.22e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 17:12:59,256 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_301_20260314_171259.pth
2026-03-14 17:16:23,679 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 310/5000
Loss=0.006050 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7874 Kappa=inf Kappa_q=1.10e+04
Delta=0.455030 Purity=0.5450 Crystal=0
T_eff=8.47e-27 C_v=1.52e+05 Poynting=2.35e-02 E_flow=2.35e-02
Lambda=1.00e+00 hbar_eff=2.07e-01 S_spectral=8.3540 Bragg=10
LR=4.95e-03 AnnealT=0.00e+00 dDelta/dt=-1.18e-05 NormErr=9.94e-01
Gibbs=4.5503e-01 T_crit=6.75e-04 SpecGap=2.0995e-02 PartRatio=1.0000
LvlSpacing=0.5395 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 17:17:59,920 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_314_20260314_171759.pth
2026-03-14 17:20:21,620 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 320/5000
Loss=0.006047 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7876 Kappa=inf Kappa_q=1.10e+04
Delta=0.454916 Purity=0.5451 Crystal=0
T_eff=7.97e-27 C_v=1.52e+05 Poynting=2.34e-02 E_flow=2.34e-02
Lambda=1.00e+00 hbar_eff=2.07e-01 S_spectral=8.3540 Bragg=10
LR=4.95e-03 AnnealT=0.00e+00 dDelta/dt=-1.20e-05 NormErr=9.94e-01
Gibbs=4.5492e-01 T_crit=6.74e-04 SpecGap=2.0984e-02 PartRatio=1.0000
LvlSpacing=0.5386 Ricci=2.24e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 17:23:15,602 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_328_20260314_172315.pth
2026-03-14 17:23:56,529 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 330/5000
Loss=0.006045 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7878 Kappa=1.00e+00 Kappa_q=1.10e+04
Delta=0.454850 Purity=0.5451 Crystal=0
T_eff=8.60e-27 C_v=1.51e+05 Poynting=2.34e-02 E_flow=2.34e-02
Lambda=1.00e+00 hbar_eff=2.07e-01 S_spectral=8.3540 Bragg=10
LR=4.95e-03 AnnealT=0.00e+00 dDelta/dt=-1.16e-05 NormErr=9.94e-01
Gibbs=4.5485e-01 T_crit=6.74e-04 SpecGap=2.0973e-02 PartRatio=1.0000
LvlSpacing=0.5533 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 17:27:24,147 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 340/5000
Loss=0.006042 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7880 Kappa=inf Kappa_q=1.10e+04
Delta=0.454739 Purity=0.5453 Crystal=0
T_eff=7.08e-27 C_v=1.51e+05 Poynting=2.34e-02 E_flow=2.34e-02
Lambda=1.00e+00 hbar_eff=2.07e-01 S_spectral=8.3540 Bragg=10
LR=4.94e-03 AnnealT=0.00e+00 dDelta/dt=-1.07e-05 NormErr=9.94e-01
Gibbs=4.5474e-01 T_crit=6.74e-04 SpecGap=2.0963e-02 PartRatio=1.0000
LvlSpacing=0.5372 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 17:28:26,522 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_343_20260314_172826.pth
2026-03-14 17:30:51,504 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 350/5000
Loss=0.006039 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7883 Kappa=1.00e+00 Kappa_q=1.10e+04
Delta=0.454619 Purity=0.5454 Crystal=0
T_eff=8.00e-27 C_v=1.51e+05 Poynting=2.34e-02 E_flow=2.34e-02
Lambda=1.00e+00 hbar_eff=2.07e-01 S_spectral=8.3540 Bragg=10
LR=4.94e-03 AnnealT=0.00e+00 dDelta/dt=-1.00e-05 NormErr=9.93e-01
Gibbs=4.5462e-01 T_crit=6.74e-04 SpecGap=2.0952e-02 PartRatio=1.0000
LvlSpacing=0.5330 Ricci=2.21e+15 Stability=S
Topo[CM_x=-0.1880 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 17:33:37,390 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_358_20260314_173337.pth
2026-03-14 17:34:18,981 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 360/5000
Loss=0.006037 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7886 Kappa=inf Kappa_q=1.10e+04
Delta=0.454500 Purity=0.5455 Crystal=0
T_eff=7.70e-27 C_v=1.50e+05 Poynting=2.33e-02 E_flow=2.33e-02
Lambda=1.00e+00 hbar_eff=2.07e-01 S_spectral=8.3541 Bragg=10
LR=4.94e-03 AnnealT=0.00e+00 dDelta/dt=-1.03e-05 NormErr=9.93e-01
Gibbs=4.5450e-01 T_crit=6.74e-04 SpecGap=2.0941e-02 PartRatio=1.0000
LvlSpacing=0.5252 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 17:37:45,107 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 370/5000
Loss=0.006034 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7888 Kappa=inf Kappa_q=1.10e+04
Delta=0.454387 Purity=0.5456 Crystal=0
T_eff=8.00e-27 C_v=1.50e+05 Poynting=2.33e-02 E_flow=2.33e-02
Lambda=1.00e+00 hbar_eff=2.06e-01 S_spectral=8.3541 Bragg=10
LR=4.93e-03 AnnealT=0.00e+00 dDelta/dt=-1.10e-05 NormErr=9.93e-01
Gibbs=4.5439e-01 T_crit=6.74e-04 SpecGap=2.0931e-02 PartRatio=1.0000
LvlSpacing=0.5435 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 17:38:47,130 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_373_20260314_173847.pth
2026-03-14 17:41:10,453 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 380/5000
Loss=0.006031 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7890 Kappa=inf Kappa_q=1.10e+04
Delta=0.454284 Purity=0.5457 Crystal=0
T_eff=7.91e-27 C_v=1.50e+05 Poynting=2.33e-02 E_flow=2.33e-02
Lambda=1.00e+00 hbar_eff=2.06e-01 S_spectral=8.3541 Bragg=10
LR=4.93e-03 AnnealT=0.00e+00 dDelta/dt=-1.17e-05 NormErr=9.92e-01
Gibbs=4.5428e-01 T_crit=6.74e-04 SpecGap=2.0921e-02 PartRatio=1.0000
LvlSpacing=0.5383 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 17:43:55,886 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_388_20260314_174355.pth
2026-03-14 17:44:36,815 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 390/5000
Loss=0.006029 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7893 Kappa=inf Kappa_q=1.10e+04
Delta=0.454173 Purity=0.5458 Crystal=0
T_eff=8.63e-27 C_v=1.49e+05 Poynting=2.33e-02 E_flow=2.33e-02
Lambda=1.00e+00 hbar_eff=2.06e-01 S_spectral=8.3541 Bragg=10
LR=4.93e-03 AnnealT=0.00e+00 dDelta/dt=-1.13e-05 NormErr=9.94e-01
Gibbs=4.5417e-01 T_crit=6.74e-04 SpecGap=2.0911e-02 PartRatio=1.0000
LvlSpacing=0.5539 Ricci=2.21e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 17:48:02,142 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 400/5000
Loss=0.006026 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7895 Kappa=inf Kappa_q=1.10e+04
Delta=0.454057 Purity=0.5459 Crystal=0
T_eff=7.18e-27 C_v=1.49e+05 Poynting=2.33e-02 E_flow=2.33e-02
Lambda=1.00e+00 hbar_eff=2.06e-01 S_spectral=8.3541 Bragg=10
LR=4.92e-03 AnnealT=0.00e+00 dDelta/dt=-1.10e-05 NormErr=9.94e-01
Gibbs=4.5406e-01 T_crit=6.74e-04 SpecGap=2.0901e-02 PartRatio=1.0000
LvlSpacing=0.5309 Ricci=2.24e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 17:49:03,925 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_403_20260314_174903.pth
2026-03-14 17:51:27,987 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 410/5000
Loss=0.006023 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7898 Kappa=inf Kappa_q=1.10e+04
Delta=0.453955 Purity=0.5460 Crystal=0
T_eff=7.85e-27 C_v=1.49e+05 Poynting=2.32e-02 E_flow=2.32e-02
Lambda=1.00e+00 hbar_eff=2.06e-01 S_spectral=8.3541 Bragg=10
LR=4.92e-03 AnnealT=0.00e+00 dDelta/dt=-1.08e-05 NormErr=9.93e-01
Gibbs=4.5396e-01 T_crit=6.74e-04 SpecGap=2.0890e-02 PartRatio=1.0000
LvlSpacing=0.5420 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 17:54:12,662 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_418_20260314_175412.pth
2026-03-14 17:54:53,774 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 420/5000
Loss=0.006021 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7900 Kappa=inf Kappa_q=1.10e+04
Delta=0.453843 Purity=0.5462 Crystal=0
T_eff=8.13e-27 C_v=1.48e+05 Poynting=2.33e-02 E_flow=2.33e-02
Lambda=1.00e+00 hbar_eff=2.06e-01 S_spectral=8.3541 Bragg=10
LR=4.91e-03 AnnealT=0.00e+00 dDelta/dt=-1.08e-05 NormErr=9.93e-01
Gibbs=4.5384e-01 T_crit=6.74e-04 SpecGap=2.0880e-02 PartRatio=1.0000
LvlSpacing=0.5504 Ricci=2.24e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 17:58:20,003 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 430/5000
Loss=0.006018 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7903 Kappa=1.00e+00 Kappa_q=1.10e+04
Delta=0.453723 Purity=0.5463 Crystal=0
T_eff=8.05e-27 C_v=1.48e+05 Poynting=2.32e-02 E_flow=2.32e-02
Lambda=1.00e+00 hbar_eff=2.06e-01 S_spectral=8.3541 Bragg=10
LR=4.91e-03 AnnealT=0.00e+00 dDelta/dt=-1.11e-05 NormErr=9.93e-01
Gibbs=4.5372e-01 T_crit=6.74e-04 SpecGap=2.0870e-02 PartRatio=1.0000
LvlSpacing=0.5281 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6429 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 17:59:21,783 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_433_20260314_175921.pth
2026-03-14 18:01:45,963 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 440/5000
Loss=0.006015 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7905 Kappa=inf Kappa_q=1.10e+04
Delta=0.453611 Purity=0.5464 Crystal=0
T_eff=8.28e-27 C_v=1.47e+05 Poynting=2.32e-02 E_flow=2.32e-02
Lambda=1.00e+00 hbar_eff=2.06e-01 S_spectral=8.3541 Bragg=10
LR=4.91e-03 AnnealT=0.00e+00 dDelta/dt=-1.12e-05 NormErr=9.93e-01
Gibbs=4.5361e-01 T_crit=6.74e-04 SpecGap=2.0860e-02 PartRatio=1.0000
LvlSpacing=0.5509 Ricci=2.24e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6429 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 18:04:31,546 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_448_20260314_180431.pth
2026-03-14 18:05:55,865 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 450/5000
Loss=0.006013 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7908 Kappa=inf Kappa_q=1.09e+04
Delta=0.453472 Purity=0.5465 Crystal=0
T_eff=7.85e-27 C_v=1.47e+05 Poynting=2.33e-02 E_flow=2.33e-02
Lambda=1.00e+00 hbar_eff=2.06e-01 S_spectral=8.3541 Bragg=10
LR=4.90e-03 AnnealT=0.00e+00 dDelta/dt=-1.14e-05 NormErr=9.93e-01
Gibbs=4.5347e-01 T_crit=6.73e-04 SpecGap=2.0849e-02 PartRatio=1.0000
LvlSpacing=0.5421 Ricci=2.24e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 18:10:16,025 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_453_20260314_181015.pth
2026-03-14 18:15:34,795 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_459_20260314_181534.pth
2026-03-14 18:16:07,186 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 460/5000
Loss=0.006010 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7913 Kappa=inf Kappa_q=1.09e+04
Delta=0.453264 Purity=0.5467 Crystal=0
T_eff=8.21e-27 C_v=1.47e+05 Poynting=2.34e-02 E_flow=2.34e-02
Lambda=1.00e+00 hbar_eff=2.05e-01 S_spectral=8.3541 Bragg=10
LR=4.90e-03 AnnealT=0.00e+00 dDelta/dt=-1.34e-05 NormErr=9.93e-01
Gibbs=4.5326e-01 T_crit=6.73e-04 SpecGap=2.0839e-02 PartRatio=1.0000
LvlSpacing=0.5286 Ricci=2.24e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 18:20:17,277 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 470/5000
Loss=0.006007 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7915 Kappa=inf Kappa_q=1.09e+04
Delta=0.453152 Purity=0.5468 Crystal=0
T_eff=8.09e-27 C_v=1.47e+05 Poynting=2.33e-02 E_flow=2.33e-02
Lambda=1.00e+00 hbar_eff=2.05e-01 S_spectral=8.3541 Bragg=10
LR=4.89e-03 AnnealT=0.00e+00 dDelta/dt=-1.47e-05 NormErr=9.93e-01
Gibbs=4.5315e-01 T_crit=6.73e-04 SpecGap=2.0828e-02 PartRatio=1.0000
LvlSpacing=0.5231 Ricci=2.24e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 18:20:41,565 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_471_20260314_182041.pth
2026-03-14 18:24:12,940 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 480/5000
Loss=0.006005 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7916 Kappa=inf Kappa_q=1.09e+04
Delta=0.453097 Purity=0.5469 Crystal=0
T_eff=7.43e-27 C_v=1.46e+05 Poynting=2.34e-02 E_flow=2.34e-02
Lambda=1.00e+00 hbar_eff=2.05e-01 S_spectral=8.3541 Bragg=10
LR=4.89e-03 AnnealT=0.00e+00 dDelta/dt=-1.43e-05 NormErr=9.92e-01
Gibbs=4.5310e-01 T_crit=6.73e-04 SpecGap=2.0818e-02 PartRatio=1.0000
LvlSpacing=0.5263 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 18:25:59,162 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_484_20260314_182559.pth
2026-03-14 18:28:37,375 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 490/5000
Loss=0.006002 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7919 Kappa=inf Kappa_q=1.09e+04
Delta=0.452988 Purity=0.5470 Crystal=0
T_eff=7.61e-27 C_v=1.46e+05 Poynting=2.34e-02 E_flow=2.34e-02
Lambda=1.00e+00 hbar_eff=2.05e-01 S_spectral=8.3541 Bragg=10
LR=4.88e-03 AnnealT=0.00e+00 dDelta/dt=-1.24e-05 NormErr=9.93e-01
Gibbs=4.5299e-01 T_crit=6.73e-04 SpecGap=2.0808e-02 PartRatio=1.0000
LvlSpacing=0.5294 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 18:31:05,586 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_496_20260314_183105.pth
2026-03-14 18:32:18,400 - LambdaPressureScheduler - INFO - Lambda pressure increased to 1.000000e+01 at epoch 500
2026-03-14 18:32:42,850 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 500/5000
Loss=0.054135 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7921 Kappa=inf Kappa_q=1.09e+04
Delta=0.452896 Purity=0.5471 Crystal=0
T_eff=7.48e-27 C_v=1.45e+05 Poynting=2.34e-02 E_flow=2.34e-02
Lambda=1.00e+01 hbar_eff=6.49e-01 S_spectral=8.3541 Bragg=10
LR=4.88e-03 AnnealT=0.00e+00 dDelta/dt=-9.93e-06 NormErr=9.93e-01
Gibbs=4.5290e-01 T_crit=6.73e-04 SpecGap=2.0798e-02 PartRatio=1.0000
LvlSpacing=0.5259 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 18:36:13,479 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_507_20260314_183613.pth
2026-03-14 18:37:30,146 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 510/5000
Loss=0.054107 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7923 Kappa=inf Kappa_q=1.09e+04
Delta=0.452814 Purity=0.5472 Crystal=0
T_eff=7.91e-27 C_v=3.70e+12 Poynting=2.34e-02 E_flow=2.34e-02
Lambda=1.00e+01 hbar_eff=6.48e-01 S_spectral=8.3541 Bragg=10
LR=4.87e-03 AnnealT=0.00e+00 dDelta/dt=-8.73e-06 NormErr=9.93e-01
Gibbs=4.5281e-01 T_crit=6.73e-04 SpecGap=2.0787e-02 PartRatio=1.0000
LvlSpacing=0.5412 Ricci=2.24e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 18:41:01,281 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 520/5000
Loss=0.054079 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7925 Kappa=inf Kappa_q=1.09e+04
Delta=0.452695 Purity=0.5473 Crystal=0
T_eff=7.29e-27 C_v=5.55e+12 Poynting=2.34e-02 E_flow=2.34e-02
Lambda=1.00e+01 hbar_eff=6.48e-01 S_spectral=8.3541 Bragg=10
LR=4.87e-03 AnnealT=0.00e+00 dDelta/dt=-9.05e-06 NormErr=9.94e-01
Gibbs=4.5269e-01 T_crit=6.73e-04 SpecGap=2.0776e-02 PartRatio=1.0000
LvlSpacing=0.5215 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 18:41:25,679 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_521_20260314_184125.pth
2026-03-14 18:45:24,318 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 530/5000
Loss=0.054051 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7928 Kappa=inf Kappa_q=1.09e+04
Delta=0.452571 Purity=0.5474 Crystal=0
T_eff=7.40e-27 C_v=5.55e+12 Poynting=2.33e-02 E_flow=2.33e-02
Lambda=1.00e+01 hbar_eff=6.48e-01 S_spectral=8.3541 Bragg=10
LR=4.86e-03 AnnealT=0.00e+00 dDelta/dt=-1.00e-05 NormErr=9.94e-01
Gibbs=4.5257e-01 T_crit=6.73e-04 SpecGap=2.0765e-02 PartRatio=1.0000
LvlSpacing=0.5257 Ricci=2.21e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 18:46:50,803 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_533_20260314_184650.pth
2026-03-14 18:49:47,627 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 540/5000
Loss=0.054023 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7931 Kappa=inf Kappa_q=1.09e+04
Delta=0.452452 Purity=0.5475 Crystal=0
T_eff=8.32e-27 C_v=3.70e+12 Poynting=2.34e-02 E_flow=2.34e-02
Lambda=1.00e+01 hbar_eff=6.47e-01 S_spectral=8.3541 Bragg=10
LR=4.86e-03 AnnealT=0.00e+00 dDelta/dt=-1.07e-05 NormErr=9.94e-01
Gibbs=4.5245e-01 T_crit=6.73e-04 SpecGap=2.0754e-02 PartRatio=1.0000
LvlSpacing=0.5307 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 18:52:09,611 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_546_20260314_185209.pth
2026-03-14 18:53:51,425 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 550/5000
Loss=0.053994 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7934 Kappa=inf Kappa_q=1.09e+04
Delta=0.452325 Purity=0.5477 Crystal=0
T_eff=6.96e-27 C_v=1.65e+07 Poynting=2.34e-02 E_flow=2.34e-02
Lambda=1.00e+01 hbar_eff=6.47e-01 S_spectral=8.3541 Bragg=10
LR=4.85e-03 AnnealT=0.00e+00 dDelta/dt=-1.19e-05 NormErr=9.94e-01
Gibbs=4.5233e-01 T_crit=6.73e-04 SpecGap=2.0743e-02 PartRatio=1.0000
LvlSpacing=0.5175 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 18:57:25,865 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_559_20260314_185725.pth
2026-03-14 18:57:48,283 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 560/5000
Loss=0.053967 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7937 Kappa=inf Kappa_q=1.09e+04
Delta=0.452180 Purity=0.5478 Crystal=0
T_eff=7.88e-27 C_v=1.64e+07 Poynting=2.33e-02 E_flow=2.33e-02
Lambda=1.00e+01 hbar_eff=6.47e-01 S_spectral=8.3541 Bragg=10
LR=4.85e-03 AnnealT=0.00e+00 dDelta/dt=-1.26e-05 NormErr=9.94e-01
Gibbs=4.5218e-01 T_crit=6.72e-04 SpecGap=2.0732e-02 PartRatio=1.0000
LvlSpacing=0.5330 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 19:01:57,266 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 570/5000
Loss=0.053939 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7939 Kappa=inf Kappa_q=1.09e+04
Delta=0.452061 Purity=0.5479 Crystal=0
T_eff=7.75e-27 C_v=1.63e+07 Poynting=2.33e-02 E_flow=2.33e-02
Lambda=1.00e+01 hbar_eff=6.46e-01 S_spectral=8.3541 Bragg=10
LR=4.84e-03 AnnealT=0.00e+00 dDelta/dt=-1.29e-05 NormErr=9.94e-01
Gibbs=4.5206e-01 T_crit=6.72e-04 SpecGap=2.0721e-02 PartRatio=1.0000
LvlSpacing=0.5376 Ricci=2.24e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 19:02:49,000 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_572_20260314_190248.pth
2026-03-14 19:06:09,545 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 580/5000
Loss=0.053911 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7941 Kappa=1.00e+00 Kappa_q=1.09e+04
Delta=0.451992 Purity=0.5480 Crystal=0
T_eff=7.37e-27 C_v=1.63e+07 Poynting=2.33e-02 E_flow=2.33e-02
Lambda=1.00e+01 hbar_eff=6.46e-01 S_spectral=8.3541 Bragg=10
LR=4.84e-03 AnnealT=0.00e+00 dDelta/dt=-1.26e-05 NormErr=9.94e-01
Gibbs=4.5199e-01 T_crit=6.72e-04 SpecGap=2.0710e-02 PartRatio=1.0000
LvlSpacing=0.5268 Ricci=2.24e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6429 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 19:07:50,920 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_584_20260314_190750.pth
2026-03-14 19:10:19,274 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 590/5000
Loss=0.053883 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7943 Kappa=inf Kappa_q=1.09e+04
Delta=0.451878 Purity=0.5481 Crystal=0
T_eff=7.51e-27 C_v=1.62e+07 Poynting=2.33e-02 E_flow=2.33e-02
Lambda=1.00e+01 hbar_eff=6.46e-01 S_spectral=8.3541 Bragg=10
LR=4.83e-03 AnnealT=0.00e+00 dDelta/dt=-1.14e-05 NormErr=9.93e-01
Gibbs=4.5188e-01 T_crit=6.72e-04 SpecGap=2.0699e-02 PartRatio=1.0000
LvlSpacing=0.5563 Ricci=2.22e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6429 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 19:13:13,476 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_597_20260314_191313.pth
2026-03-14 19:14:26,866 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 600/5000
Loss=0.053855 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7946 Kappa=inf Kappa_q=1.09e+04
Delta=0.451783 Purity=0.5482 Crystal=0
T_eff=6.76e-27 C_v=1.62e+07 Poynting=2.33e-02 E_flow=2.33e-02
Lambda=1.00e+01 hbar_eff=6.45e-01 S_spectral=8.3541 Bragg=10
LR=4.83e-03 AnnealT=0.00e+00 dDelta/dt=-1.04e-05 NormErr=9.93e-01
Gibbs=4.5178e-01 T_crit=6.72e-04 SpecGap=2.0688e-02 PartRatio=1.0000
LvlSpacing=0.5222 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6429 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 19:18:34,990 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 610/5000
Loss=0.053827 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7947 Kappa=1.00e+00 Kappa_q=1.09e+04
Delta=0.451704 Purity=0.5483 Crystal=0
T_eff=7.79e-27 C_v=1.61e+07 Poynting=2.32e-02 E_flow=2.32e-02
Lambda=1.00e+01 hbar_eff=6.45e-01 S_spectral=8.3541 Bragg=10
LR=4.82e-03 AnnealT=0.00e+00 dDelta/dt=-9.34e-06 NormErr=9.94e-01
Gibbs=4.5170e-01 T_crit=6.72e-04 SpecGap=2.0678e-02 PartRatio=1.0000
LvlSpacing=0.5440 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6429 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 19:18:35,063 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_610_20260314_191834.pth
2026-03-14 19:22:39,299 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 620/5000
Loss=0.053800 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7950 Kappa=inf Kappa_q=1.09e+04
Delta=0.451586 Purity=0.5484 Crystal=0
T_eff=7.37e-27 C_v=1.61e+07 Poynting=2.32e-02 E_flow=2.32e-02
Lambda=1.00e+01 hbar_eff=6.45e-01 S_spectral=8.3541 Bragg=10
LR=4.81e-03 AnnealT=0.00e+00 dDelta/dt=-9.28e-06 NormErr=9.94e-01
Gibbs=4.5159e-01 T_crit=6.72e-04 SpecGap=2.0667e-02 PartRatio=1.0000
LvlSpacing=0.5173 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6429 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
2026-03-14 19:23:52,847 - FullTrainingOrchestrator - INFO -   Checkpoint saved: checkpoints_maxwell_phase3/checkpoint_phase3_training_epoch_623_20260314_192352.pth
2026-03-14 19:26:25,085 - FullTrainingOrchestrator - INFO - [P3-TRAIN] Epoch 630/5000
Loss=0.053772 ValLoss=0.000651 TrainAcc=1.0000 ValAcc=1.0000
LC=0.0000 SP=0.1989 Alpha=0.7952 Kappa=inf Kappa_q=1.08e+04
Delta=0.451479 Purity=0.5485 Crystal=0
T_eff=8.48e-27 C_v=1.61e+07 Poynting=2.31e-02 E_flow=2.31e-02
Lambda=1.00e+01 hbar_eff=6.45e-01 S_spectral=8.3541 Bragg=10
LR=4.81e-03 AnnealT=0.00e+00 dDelta/dt=-9.88e-06 NormErr=9.93e-01
Gibbs=4.5148e-01 T_crit=6.72e-04 SpecGap=2.0657e-02 PartRatio=1.0000
LvlSpacing=0.5309 Ricci=2.23e+15 Stability=S
Topo[CM_x=-0.1879 Loc=0.2998 Align=0.00 Aniso=0.7002 Phase=0.0000 Cryst=0]
Resonance=0.2726 PhaseCoh=0.6428 SpecConc=0.0365 Harm=3
ImagRatio=0.3105 KernelRatio=0.3109
