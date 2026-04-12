# 连续具身导航新增论文清单（Round 2）

说明：
- 本表只列相对旧版 `61` 篇总表新纳入的论文。
- 这些论文已经同步插入 `docs/paper_list_feishu_strict.md`，并全部用 `【新增】` 标注。
- 后续新一轮粗读默认优先从这里开始。
- 排序方式与主表一致：按首次公开时间从新到旧排列。

## 本轮新增论文

1. 【新增】LatentPilot: Scene-Aware Vision-and-Language Navigation by Dreaming Ahead with Latent Visual Reasoning | 2026-03-31 | https://arxiv.org/abs/2603.29165
2. 【新增】NavTrust: Benchmarking Trustworthiness for Embodied Navigation | 2026-03-19 | https://arxiv.org/abs/2603.19229
3. 【新增】CorrectNav: Self-Correction Flywheel Empowers Vision-Language-Action Navigation Model | 2026-03-14 | https://doi.org/10.1609/aaai.v40i22.38942
4. 【新增】ImagiNav: Scalable Embodied Navigation via Generative Visual Prediction and Inverse Dynamics | 2026-03-14 | https://arxiv.org/abs/2603.13833
5. 【新增】SPAN-Nav: Generalized Spatial Awareness for Versatile Vision-Language Navigation | 2026-03-10 | https://arxiv.org/abs/2603.09163
6. 【新增】History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation | 2026-03-06 | https://arxiv.org/abs/2603.06480
7. 【新增】PROSPECT: Unified Streaming Vision-Language Navigation via Semantic-Spatial Fusion and Latent Predictive Representation | 2026-03-04 | https://arxiv.org/abs/2603.03739
8. 【新增】Nipping the Drift in the Bud: Retrospective Rectification for Robust Vision-Language Navigation | 2026-02-06 | https://arxiv.org/abs/2602.06356
9. 【新增】NaVIDA: Vision-Language Navigation with Inverse Dynamics Augmentation | 2026-01-26 | https://arxiv.org/abs/2601.18188
10. 【新增】FantasyVLN: Unified Multimodal Chain-of-Thought Reasoning for Vision-Language Navigation | 2026-01-20 | https://arxiv.org/abs/2601.13976
11. 【新增】VLNVerse: A Benchmark for Vision-Language Navigation with Versatile, Embodied, Realistic Simulation and Evaluation | 2025-12-22 | https://arxiv.org/abs/2512.19021
12. 【新增】Fast-SmartWay: Panoramic-Free End-to-End Zero-Shot Vision-and-Language Navigation | 2025-11-02 | https://arxiv.org/abs/2511.00933
13. 【新增】ComposableNav: Instruction-Following Navigation in Dynamic Environments via Composable Diffusion | 2025-09-22 | https://arxiv.org/abs/2509.17941
14. 【新增】FSR-VLN: Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph | 2025-09-17 | https://arxiv.org/abs/2509.13733
15. 【新增】DreamNav: A Trajectory-Based Imaginative Framework for Zero-Shot Vision-and-Language Navigation | 2025-09-14 | https://arxiv.org/abs/2509.11197
16. 【新增】Active Test-time Vision-Language Navigation | 2025-06-07 | https://arxiv.org/abs/2506.06630
17. 【新增】ST-Booster: An Iterative SpatioTemporal Perception Booster for Vision-and-Language Navigation in Continuous Environments | 2025-04-14 | https://arxiv.org/abs/2504.09843
18. 【新增】Endowing Embodied Agents with Spatial Reasoning Capabilities for Vision-and-Language Navigation | 2025-04-09 | https://arxiv.org/abs/2504.08806
19. 【新增】SmartWay: Enhanced Waypoint Prediction and Backtracking for Zero-Shot Vision-and-Language Navigation | 2025-03-13 | https://arxiv.org/abs/2503.10069
20. 【新增】UnitedVLN: Generalizable Gaussian Splatting for Continuous Vision-Language Navigation | 2024-11-25 | https://arxiv.org/abs/2411.16053
21. 【新增】Zero-Shot Vision-and-Language Navigation with Collision Mitigation in Continuous Environment | 2024-10-07 | https://arxiv.org/abs/2410.17267
22. 【新增】InstructNav: Zero-shot System for Generic Instruction Navigation in Unexplored Environment | 2024-06-07 | https://arxiv.org/abs/2406.04882
23. 【新增】Waypoint Models for Instruction-guided Navigation in Continuous Environments | 2021-10-05 | https://arxiv.org/abs/2110.02207
24. 【新增】Language-Aligned Waypoint (LAW) Supervision for Vision-and-Language Navigation in Continuous Environments | 2021-09-30 | https://arxiv.org/abs/2109.15207
25. 【新增】Hierarchical Cross-Modal Agent for Robotics Vision-and-Language Navigation | 2021-04-21 | https://arxiv.org/abs/2104.10674

## 建议优先粗读

1. PROSPECT：直接落在 `VLN-CE benchmark + real robot`，而且同时覆盖 streaming 和 latent predictive representation。
2. LatentPilot：明确做 action-conditioned dreaming ahead，并直接报告 `R2R-CE / RxR-CE / R2R-PE`。
3. NaVIDA：把 inverse dynamics augmentation 和 hierarchical action chunking 合进 VLN，结构上很值得深挖。
4. NavTrust：不是方法论文，但它直接给当前主线补上了 instruction / RGB / depth corruption 下的 trustworthiness 评测。
5. VLNVerse：如果后面需要重新评估 benchmark 版图，它是这一轮最值得先看的新 benchmark。
6. SmartWay / Fast-SmartWay：是当前 zero-shot waypoint + backtracking 路线中最完整的一组连续导航工作。
7. InstructNav：是 foundation-model zero-shot continuous instruction navigation 的早期关键节点。
8. Waypoint Models / LAW / Hierarchical Cross-Modal Agent：这三篇是旧表中缺失但方法谱系上必须补齐的 foundational papers。
