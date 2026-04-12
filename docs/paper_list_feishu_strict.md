# 连续具身导航论文总表（飞书可直接粘贴）

说明：
- 本轮按更严格口径重构，只保留与当前项目真正相关的论文：`ground-agent embodied navigation`、`language-conditioned`、`continuous / closed-loop environment`，以及直接服务于这条主线的 benchmark、robustness、real-robot 和 long-horizon 扩展工作。
- 已从旧版 `61` 篇总表中剔除 `11` 篇明显偏离当前主线的论文：`AirNav`、`IndoorUAV`、`SoraNav`、`VPN`、`SkyVLN`、`TRAVEL`、`RoomTour3D`、`Bootstrapping Language-Guided Navigation Learning with Self-Refining Data Flywheel`、`Towards Realistic UAV Vision-Language Navigation`、`AerialVLN`、`Room-Across-Room`。
- 本轮新增纳入 `25` 篇论文，均已在条目前用 `【新增】` 标出，并单独汇总到 `docs/paper_list_new_additions_round2.md`，作为下一轮粗读入口。
- 当前主表共 `75` 篇，按首次公开时间从新到旧排列；能核到 `arXiv v1` 的优先用 `arXiv v1` 日期，否则用 publisher / DOI / OpenAlex 可核实日期。
- 这一版是之后批量粗读、shortlist 维护、codebase reconnaissance 的唯一执行总表。

1. 【新增】LatentPilot: Scene-Aware Vision-and-Language Navigation by Dreaming Ahead with Latent Visual Reasoning | 2026-03-31 | https://arxiv.org/abs/2603.29165
2. 【新增】NavTrust: Benchmarking Trustworthiness for Embodied Navigation | 2026-03-19 | https://arxiv.org/abs/2603.19229
3. P$^{3}$Nav: End-to-End Perception, Prediction and Planning for Vision-and-Language Navigation | 2026-03-18 | https://arxiv.org/abs/2603.17459
4. EmergeNav: Structured Embodied Inference for Zero-Shot Vision-and-Language Navigation in Continuous Environments | 2026-03-16 | https://arxiv.org/abs/2603.16947
5. HiMemVLN: Enhancing Reliability of Open-Source Zero-Shot Vision-and-Language Navigation with Hierarchical Memory System | 2026-03-16 | https://arxiv.org/abs/2603.14807
6. 【新增】CorrectNav: Self-Correction Flywheel Empowers Vision-Language-Action Navigation Model | 2026-03-14 | https://doi.org/10.1609/aaai.v40i22.38942
7. 【新增】ImagiNav: Scalable Embodied Navigation via Generative Visual Prediction and Inverse Dynamics | 2026-03-14 | https://arxiv.org/abs/2603.13833
8. Let's Reward Step-by-Step: Step-Aware Contrastive Alignment for Vision-Language Navigation in Continuous Environments | 2026-03-10 | https://arxiv.org/abs/2603.09740
9. 【新增】SPAN-Nav: Generalized Spatial Awareness for Versatile Vision-Language Navigation | 2026-03-10 | https://arxiv.org/abs/2603.09163
10. 【新增】History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation | 2026-03-06 | https://arxiv.org/abs/2603.06480
11. 【新增】PROSPECT: Unified Streaming Vision-Language Navigation via Semantic-Spatial Fusion and Latent Predictive Representation | 2026-03-04 | https://arxiv.org/abs/2603.03739
12. Enhancing Vision-Language Navigation with Multimodal Event Knowledge from Real-World Indoor Tour Videos | 2026-02-27 | https://arxiv.org/abs/2602.23937
13. One Agent to Guide Them All: Empowering MLLMs for Vision-and-Language Navigation via Explicit World Representation | 2026-02-17 | https://arxiv.org/abs/2602.15400
14. 【新增】Nipping the Drift in the Bud: Retrospective Rectification for Robust Vision-Language Navigation | 2026-02-06 | https://arxiv.org/abs/2602.06356
15. Dynamic Topology Awareness: Breaking the Granularity Rigidity in Vision-Language Navigation | 2026-01-29 | https://arxiv.org/abs/2601.21751
16. 【新增】NaVIDA: Vision-Language Navigation with Inverse Dynamics Augmentation | 2026-01-26 | https://arxiv.org/abs/2601.18188
17. 【新增】FantasyVLN: Unified Multimodal Chain-of-Thought Reasoning for Vision-Language Navigation | 2026-01-20 | https://arxiv.org/abs/2601.13976
18. Spatial-VLN: Zero-Shot Vision-and-Language Navigation With Explicit Spatial Perception and Exploration | 2026-01-19 | https://arxiv.org/abs/2601.12766
19. SpatialNav: Leveraging Spatial Scene Graphs for Zero-Shot Vision-and-Language Navigation | 2026-01-11 | https://arxiv.org/abs/2601.06806
20. SeqWalker: Sequential-Horizon Vision-and-Language Navigation with Hierarchical Planning | 2026-01-08 | https://arxiv.org/abs/2601.04699
21. ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-and-Language Navigation in Continuous Environments | 2025-12-24 | https://arxiv.org/abs/2512.20940
22. 【新增】VLNVerse: A Benchmark for Vision-Language Navigation with Versatile, Embodied, Realistic Simulation and Evaluation | 2025-12-22 | https://arxiv.org/abs/2512.19021
23. CLASH: Collaborative Large-Small Hierarchical Framework for Continuous Vision-and-Language Navigation | 2025-12-11 | https://arxiv.org/abs/2512.10360
24. Efficient-VLN: A Training-Efficient Vision-Language Navigation Model | 2025-12-11 | https://arxiv.org/abs/2512.10310
25. Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation | 2025-12-09 | https://arxiv.org/abs/2512.08186
26. NavForesee: A Unified Vision-Language World Model for Hierarchical Planning and Dual-Horizon Navigation Prediction | 2025-12-01 | https://arxiv.org/abs/2512.01550
27. 【新增】Fast-SmartWay: Panoramic-Free End-to-End Zero-Shot Vision-and-Language Navigation | 2025-11-02 | https://arxiv.org/abs/2511.00933
28. LaViRA: Language-Vision-Robot Actions Translation for Zero-Shot Vision Language Navigation in Continuous Environments | 2025-10-22 | https://arxiv.org/abs/2510.19655
29. JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation | 2025-09-26 | https://arxiv.org/abs/2509.22548
30. VLN-Zero: Rapid Exploration and Cache-Enabled Neurosymbolic Vision-Language Planning for Zero-Shot Transfer in Robot Navigation | 2025-09-23 | https://arxiv.org/abs/2509.18592
31. 【新增】ComposableNav: Instruction-Following Navigation in Dynamic Environments via Composable Diffusion | 2025-09-22 | https://arxiv.org/abs/2509.17941
32. 【新增】FSR-VLN: Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph | 2025-09-17 | https://arxiv.org/abs/2509.13733
33. 【新增】DreamNav: A Trajectory-Based Imaginative Framework for Zero-Shot Vision-and-Language Navigation | 2025-09-14 | https://arxiv.org/abs/2509.11197
34. GC-VLN: Instruction as Graph Constraints for Training-free Vision-and-Language Navigation | 2025-09-12 | https://arxiv.org/abs/2509.10454
35. DAgger Diffusion Navigation: DAgger Boosted Diffusion Policy for Vision-Language Navigation | 2025-08-13 | https://arxiv.org/abs/2508.09444
36. MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming | 2025-08-04 | https://arxiv.org/abs/2508.02549
37. StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling | 2025-07-07 | https://arxiv.org/abs/2507.05240
38. View Invariant Learning for Vision-Language Navigation in Continuous Environments | 2025-07-05 | https://arxiv.org/abs/2507.08831
39. NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments | 2025-06-30 | https://arxiv.org/abs/2506.23468
40. VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning | 2025-06-20 | https://arxiv.org/abs/2506.17221
41. DyNaVLM: Zero-Shot Vision-Language Navigation System with Dynamic Viewpoints and Self-Refining Graph Memory | 2025-06-18 | https://arxiv.org/abs/2506.15096
42. 【新增】Active Test-time Vision-Language Navigation | 2025-06-07 | https://arxiv.org/abs/2506.06630
43. 【新增】ST-Booster: An Iterative SpatioTemporal Perception Booster for Vision-and-Language Navigation in Continuous Environments | 2025-04-14 | https://arxiv.org/abs/2504.09843
44. 【新增】Endowing Embodied Agents with Spatial Reasoning Capabilities for Vision-and-Language Navigation | 2025-04-09 | https://arxiv.org/abs/2504.08806
45. HA-VLN: A Benchmark for Human-Aware Navigation in Discrete-Continuous Environments with Dynamic Multi-Human Interactions, Real-World Validation, and an Open Leaderboard | 2025-03-18 | https://arxiv.org/abs/2503.14229
46. 【新增】SmartWay: Enhanced Waypoint Prediction and Backtracking for Zero-Shot Vision-and-Language Navigation | 2025-03-13 | https://arxiv.org/abs/2503.10069
47. Ground-level Viewpoint Vision-and-Language Navigation in Continuous Environments | 2025-02-26 | https://arxiv.org/abs/2502.19024
48. Enhancing Large Language Models with RAG for Visual Language Navigation in Continuous Environments | 2025-02-25 | https://www.mdpi.com/2079-9292/14/5/909
49. Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments | 2024-12-13 | https://arxiv.org/abs/2412.10137
50. Towards Long-Horizon Vision-Language Navigation: Platform, Benchmark and Method | 2024-12-12 | https://arxiv.org/abs/2412.09082
51. 【新增】UnitedVLN: Generalizable Gaussian Splatting for Continuous Vision-Language Navigation | 2024-11-25 | https://arxiv.org/abs/2411.16053
52. 【新增】Zero-Shot Vision-and-Language Navigation with Collision Mitigation in Continuous Environment | 2024-10-07 | https://arxiv.org/abs/2410.17267
53. Open-Nav: Exploring Zero-Shot Vision-and-Language Navigation in Continuous Environment with Open-Source LLMs | 2024-09-27 | https://arxiv.org/abs/2409.18794
54. Cog-GA: A Large Language Models-based Generative Agent for Vision-Language Navigation in Continuous Environments | 2024-09-04 | https://arxiv.org/abs/2409.02522
55. Affordances-Oriented Planning using Foundation Models for Continuous Vision-Language Navigation | 2024-07-08 | https://arxiv.org/abs/2407.05890
56. Human-Aware Vision-and-Language Navigation: Bridging Simulation to Reality with Dynamic Human Interactions | 2024-06-27 | https://arxiv.org/abs/2406.19236
57. 【新增】InstructNav: Zero-shot System for Generic Instruction Navigation in Unexplored Environment | 2024-06-07 | https://arxiv.org/abs/2406.04882
58. Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation | 2024-04-02 | https://arxiv.org/abs/2404.01943
59. Mind the Error! Detection and Localization of Instruction Errors in Vision-and-Language Navigation | 2024-03-15 | https://arxiv.org/abs/2403.10700
60. NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation | 2024-02-24 | https://arxiv.org/abs/2402.15852
61. Safe-VLN: Collision Avoidance for Vision-and-Language Navigation of Autonomous Robots Operating in Continuous Environments | 2023-11-06 | https://arxiv.org/abs/2311.02817
62. DREAMWALKER: Mental Planning for Continuous Vision-and-Language Navigation | 2023-08-14 | https://arxiv.org/abs/2308.07498
63. GridMM: Grid Memory Map for Vision-and-Language Navigation | 2023-07-24 | https://arxiv.org/abs/2307.12907
64. ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments | 2023-04-06 | https://arxiv.org/abs/2304.03047
65. Graph based Environment Representation for Vision-and-Language Navigation in Continuous Environments | 2023-01-11 | https://arxiv.org/abs/2301.04352
66. Iterative Vision-and-Language Navigation in Continuous Environments | 2022-10-06 | https://arxiv.org/abs/2210.03087
67. 1st Place Solutions for RxR-Habitat Vision-and-Language Navigation Competition (CVPR 2022) | 2022-06-23 | https://arxiv.org/abs/2206.11610
68. Sim-2-Sim Transfer for Vision-and-Language Navigation in Continuous Environments | 2022-04-20 | https://arxiv.org/abs/2204.09667
69. Cross-modal Map Learning for Vision and Language Navigation | 2022-03-10 | https://arxiv.org/abs/2203.05137
70. Bridging the Gap Between Learning in Discrete and Continuous Environments for Vision-and-Language Navigation | 2022-03-05 | https://arxiv.org/abs/2203.02764
71. 【新增】Waypoint Models for Instruction-guided Navigation in Continuous Environments | 2021-10-05 | https://arxiv.org/abs/2110.02207
72. 【新增】Language-Aligned Waypoint (LAW) Supervision for Vision-and-Language Navigation in Continuous Environments | 2021-09-30 | https://arxiv.org/abs/2109.15207
73. SASRA: Semantically-aware Spatio-temporal Reasoning Agent for Vision-and-Language Navigation in Continuous Environments | 2021-08-26 | https://arxiv.org/abs/2108.11945
74. 【新增】Hierarchical Cross-Modal Agent for Robotics Vision-and-Language Navigation | 2021-04-21 | https://arxiv.org/abs/2104.10674
75. Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments | 2020-04-06 | https://arxiv.org/abs/2004.02857
