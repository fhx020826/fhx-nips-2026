# Continuous VLN / VLN-CE 高质量精选论文列表（飞书可直接粘贴）

说明：

- 这是内部精选高质量列表，不等同于上面的“完整时间线大表”。
- 排序依据是当前项目阶段最关心的综合启发式判断：
  - 与 `R2R-CE / RxR-CE / VLN-CE` 的直接相关性
  - benchmark 可比性
  - 方法完整度与后续可借鉴性
  - 代码 / 项目页 / checkpoint / 数据生态完整度
  - 对后续 baseline / codebase reconnaissance 的帮助
  - 对你当前核心问题的覆盖程度：
    - history / memory
    - progress
    - hierarchical planning-control
    - subgoal / latent bridge
    - obstacle avoidance
    - deadlock recovery
    - closed-loop stability
- 排名越靠前，越值得优先粗读、优先侦察、优先借鉴。

## 第一部分：Top 30 排名

| 排名 | 论文 | 首发日期 | 当前形态 | 优先用途 | 为什么优先 |
|---:|---|---|---|---|---|
| 1 | ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments | 2023-04-06 | TPAMI 线 + arXiv + 官方代码 | 最稳 baseline / topo planning / codebase | continuous VLN 最成熟的经典强基线之一，结构清晰，代码与实验生态最完整 |
| 2 | JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation | 2025-09-26 | ICLR 2026 + arXiv + 官方代码 | memory 主线 / 新 SOTA / 高价值精读 | dual implicit memory 正中 history 与 spatial interface 问题，而且代码和项目页完整 |
| 3 | Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation | 2025-12-09 | arXiv | 高层架构参考 | 双系统分工直接命中“高层语义-低层控制接口缺口” |
| 4 | One Agent to Guide Them All: Empowering MLLMs for Vision-and-Language Navigation via Explicit World Representation | 2026-02-17 | arXiv | explicit world representation / zero-shot sim2real | 把 `RGB-D` metric world representation 做成跨 embodiment 接口，结构价值很高，但 `RxR-CE` 结果基于 sampled subset |
| 5 | P$^{3}$Nav: End-to-End Perception, Prediction and Planning for Vision-and-Language Navigation | 2026-03-18 | arXiv | perception-prediction-planning 一体化 | 同时补 perception / future waypoint / planning 三个缺口，且直接报告 R2R-CE / RxR-CE |
| 6 | StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling | 2025-07-07 | arXiv + 官方代码 + 项目页 | history / streaming / deployment | long-context 压缩、KV cache 复用、在线闭环非常有参考价值 |
| 7 | DAgger Diffusion Navigation: DAgger Boosted Diffusion Policy for Vision-Language Navigation | 2025-08-13 | arXiv + 部分公开代码 | diffusion / 低层动作专家 | 是 continuous VLN 中最关键的 diffusion direct-hit 之一 |
| 8 | Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments | 2024-12-13 | TPAMI 2025 + arXiv + 官方代码 | zero-shot / progress / sub-instruction | constraint、progress、subgoal switching 都做得非常直接 |
| 9 | NavForesee: A Unified Vision-Language World Model for Hierarchical Planning and Dual-Horizon Navigation Prediction | 2025-12-01 | arXiv | world model / hierarchical planning | 高层规划与局部预测统一建模，方法闭环很强 |
| 10 | Affordances-Oriented Planning using Foundation Models for Continuous Vision-Language Navigation | 2024-07-08 | AAAI 2025 + arXiv + 官方代码 | zero-shot / low-level affordance planning | foundation models 与 continuous low-level planning 的代表作 |
| 11 | CLASH: Collaborative Large-Small Hierarchical Framework for Continuous Vision-and-Language Navigation | 2025-12-11 | arXiv | hierarchical collaboration / current strong method | 大模型+小模型协作是很现实的系统方向 |
| 12 | ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-and-Language Navigation in Continuous Environments | 2025-12-24 | arXiv | topo follow-up / RFT | 直接回答 topo 路线在新一代 post-training 下是否仍强 |
| 13 | NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation | 2024-02-24 | arXiv | video history backbone / planner | video history 是高层理解和规划的重要支点 |
| 14 | DREAMWALKER: Mental Planning for Continuous Vision-and-Language Navigation | 2023-08-14 | ICCV 2023 + arXiv | planning / mental simulation | 是早期 world-model / planning 主线的重要代表 |
| 15 | Open-Nav: Exploring Zero-Shot Vision-and-Language Navigation in Continuous Environment with Open-Source LLMs | 2024-09-27 | arXiv | open-source LLM zero-shot scaffold | zero-shot CE 方向里最值得保留的公开基线之一 |
| 16 | View Invariant Learning for Vision-Language Navigation in Continuous Environments | 2025-07-05 | arXiv | viewpoint robustness / post-training | 直接针对 viewpoint generalization gap，且仍绑定 R2R-CE / RxR-CE |
| 17 | Dynamic Topology Awareness: Breaking the Granularity Rigidity in Vision-Language Navigation | 2026-01-29 | arXiv + 官方代码 | topo granularity | 非常新，且正面修 topo 粒度刚性问题，同时具备代码侦察价值 |
| 18 | Spatial-VLN: Zero-Shot Vision-and-Language Navigation With Explicit Spatial Perception and Exploration | 2026-01-19 | arXiv + 项目页 | zero-shot / spatial exploration | 直接围绕复杂空间场景的 spatial bottleneck 展开，但更适合作为空间推理与部署参考，不是标准主榜 baseline |
| 19 | NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments | 2025-06-30 | arXiv | world model / online adaptation | 强调环境动态建模与在线适配，和 closed-loop stability 关系紧密 |
| 20 | VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning | 2025-06-20 | arXiv + 项目页 | LVLM / RFT / long-short memory | 把 RFT 直接带入 VLN-CE，是后续 reasoning 路线的重要参照 |
| 21 | GC-VLN: Instruction as Graph Constraints for Training-free Vision-and-Language Navigation | 2025-09-12 | CoRL 2025 + arXiv | training-free / graph constraints | 结构性强，适合作为图约束路线参考 |
| 22 | SpatialNav: Leveraging Spatial Scene Graphs for Zero-Shot Vision-and-Language Navigation | 2026-01-11 | arXiv | scene graph / zero-shot | scene-graph + zero-shot 在 CE 场景里值得保留，但要明确它建立在 pre-exploration 与 sampled subset 设定上 |
| 23 | Safe-VLN: Collision Avoidance for Vision-and-Language Navigation of Autonomous Robots Operating in Continuous Environments | 2023-11-06 | arXiv | obstacle avoidance / recovery | 明确把 collision / recovery 当主问题，非常契合你的痛点 |
| 24 | GridMM: Grid Memory Map for Vision-and-Language Navigation | 2023-07-24 | arXiv | memory / map | memory-map 方向的代表作之一 |
| 25 | Bridging the Gap Between Learning in Discrete and Continuous Environments for Vision-and-Language Navigation | 2022-03-05 | arXiv | waypoint predictor / bridge baseline | 对理解 discrete-to-continuous 接口至关重要 |
| 26 | Cross-modal Map Learning for Vision and Language Navigation | 2022-03-10 | CVPR 2022 + arXiv | explicit map baseline | 显式地图与 waypoint 路线的 solid baseline |
| 27 | 1st Place Solutions for RxR-Habitat Vision-and-Language Navigation Competition (CVPR 2022) | 2022-06-23 | arXiv / challenge report | competition recipe / engineering baseline | 模块化 plan-control recipe 非常关键 |
| 28 | Ground-level Viewpoint Vision-and-Language Navigation in Continuous Environments | 2025-02-26 | arXiv | robot viewpoint gap / deployment | 很适合真实机器人视角偏差这条线 |
| 29 | Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation | 2024-04-02 | arXiv | future observation / lookahead | 未来观测建模与 lookahead exploration 很有启发 |
| 30 | Mind the Error! Detection and Localization of Instruction Errors in Vision-and-Language Navigation | 2024-03-15 | IROS 2024 + arXiv + 官方代码 | robustness / benchmark extension | instruction error robustness 是非常值得保留的支线问题 |

## 第二部分：建议的 baseline / codebase reconnaissance 优先级

### A. 第一优先：最值得先看代码底座的

1. ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments
2. JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation
3. StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling
4. Affordances-Oriented Planning using Foundation Models for Continuous Vision-Language Navigation
5. 1st Place Solutions for RxR-Habitat Vision-and-Language Navigation Competition (CVPR 2022)

### B. 第二优先：最值得做高层结构参考的

1. Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation
2. One Agent to Guide Them All: Empowering MLLMs for Vision-and-Language Navigation via Explicit World Representation
3. NavForesee: A Unified Vision-Language World Model for Hierarchical Planning and Dual-Horizon Navigation Prediction
4. Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments
5. NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation

### C. 第三优先：最值得补 history / progress / memory / robustness 的

1. JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation
2. StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling
3. Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments
4. GridMM: Grid Memory Map for Vision-and-Language Navigation
5. Mind the Error! Detection and Localization of Instruction Errors in Vision-and-Language Navigation
6. Ground-level Viewpoint Vision-and-Language Navigation in Continuous Environments

### D. 第四优先：最值得补 topo / world model / planning-control bridge 的

1. ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments
2. ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-and-Language Navigation in Continuous Environments
3. Dynamic Topology Awareness: Breaking the Granularity Rigidity in Vision-and-Language Navigation
4. NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments
5. DREAMWALKER: Mental Planning for Continuous Vision-and-Language Navigation
6. P$^{3}$Nav: End-to-End Perception, Prediction and Planning for Vision-and-Language Navigation

## 第三部分：当前应持续跟踪但不放入第一优先复现队列的

1. EmergeNav: Structured Embodied Inference for Zero-Shot Vision-and-Language Navigation in Continuous Environments
2. HiMemVLN: Enhancing Reliability of Open-Source Zero-Shot Vision-and-Language Navigation with Hierarchical Memory System
3. Let’s Reward Step-by-Step: Step-Aware Contrastive Alignment for Vision-Language Navigation in Continuous Environments
4. Enhancing Vision-Language Navigation with Multimodal Event Knowledge from Real-World Indoor Tour Videos
5. Spatial-VLN: Zero-Shot Vision-and-Language Navigation With Explicit Spatial Perception and Exploration
6. SpatialNav: Leveraging Spatial Scene Graphs for Zero-Shot Vision-and-Language Navigation
7. SeqWalker: Sequential-Horizon Vision-and-Language Navigation with Hierarchical Planning
原因：属于长程多阶段 `SH IR2R-CE` 扩展设定的重要论文，更适合作为 hierarchical planning / progress / recovery 参考，而不是标准主榜 baseline。
8. VLN-Zero: Rapid Exploration and Cache-Enabled Neurosymbolic Vision-Language Planning for Zero-Shot Transfer in Robot Navigation
9. GC-VLN: Instruction as Graph Constraints for Training-free Vision-and-Language Navigation
10. HA-VLN: A Benchmark for Human-Aware Navigation in Discrete-Continuous Environments with Dynamic Multi-Human Interactions, Real-World Validation, and an Open Leaderboard
11. Towards Long-Horizon Vision-Language Navigation: Platform, Benchmark and Method
12. RoomTour3D: Geometry-Aware Video-Instruction Tuning for Embodied Navigation

## 第四部分：当前不建议放进第一优先 shortlist，但可放在完整时间线大表里的

1. AirNav: A Large-Scale Real-World UAV Vision-and-Language Navigation Dataset with Natural and Diverse Instructions
原因：更偏 UAV 数据集与真实场景扩展，不是当前 Habitat continuous 主 benchmark 主线。

2. AerialVLN: Vision-and-Language Navigation for UAVs
原因：很重要的 UAV VLN 起点，但与 `R2R-CE / RxR-CE` 主线存在平台差异。

3. SkyVLN: Vision-and-Language Navigation and NMPC Control for UAVs in Urban Environments
原因：UAV urban navigation 很有意思，但当前与室内 Habitat 主线接口较远。

4. Enhancing Large Language Models with RAG for Visual Language Navigation in Continuous Environments
原因：问题相关，但目前更适合作为补充性尝试，不宜放在主方法参考的前列。
