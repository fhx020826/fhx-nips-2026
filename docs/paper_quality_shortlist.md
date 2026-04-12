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
| 3 | Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation | 2025-12-09 | ICLR 2026 + arXiv + 官方代码/模型/数据 | 高层架构参考 / 代码侦察高优先 | 双系统分工直接命中“高层语义-低层控制接口缺口”，而且资源生态已明显成熟 |
| 4 | One Agent to Guide Them All: Empowering MLLMs for Vision-and-Language Navigation via Explicit World Representation | 2026-02-17 | arXiv | explicit world representation / zero-shot sim2real | 把 `RGB-D` metric world representation 做成跨 embodiment 接口，结构价值很高，但 `RxR-CE` 结果基于 sampled subset |
| 5 | P$^{3}$Nav: End-to-End Perception, Prediction and Planning for Vision-and-Language Navigation | 2026-03-18 | arXiv | perception-prediction-planning 一体化 | 同时补 perception / future waypoint / planning 三个缺口，且直接报告 R2R-CE / RxR-CE |
| 6 | StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling | 2025-07-07 | arXiv + 官方代码 + 项目页 | history / streaming / deployment | long-context 压缩、KV cache 复用、在线闭环非常有参考价值 |
| 7 | DAgger Diffusion Navigation: DAgger Boosted Diffusion Policy for Vision-Language Navigation | 2025-08-13 | arXiv + 部分公开代码 | diffusion / 低层动作专家 | 是 continuous VLN 中最关键的 diffusion direct-hit 之一 |
| 8 | Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments | 2024-12-13 | TPAMI 2025 + arXiv + 官方代码 | zero-shot / progress / sub-instruction | constraint、progress、subgoal switching 都做得非常直接 |
| 9 | NavForesee: A Unified Vision-Language World Model for Hierarchical Planning and Dual-Horizon Navigation Prediction | 2025-12-01 | arXiv | world model / hierarchical planning | 高层规划与局部预测统一建模，方法闭环很强 |
| 10 | Affordances-Oriented Planning using Foundation Models for Continuous Vision-Language Navigation | 2024-07-08 | AAAI 2025 + arXiv + 官方代码 | zero-shot / low-level affordance planning | foundation models 与 continuous low-level planning 的代表作 |
| 11 | CLASH: Collaborative Large-Small Hierarchical Framework for Continuous Vision-and-Language Navigation | 2025-12-11 | arXiv + 官方代码（逐步清理发布） | hierarchical collaboration / current strong method | 大模型+小模型协作是很现实的系统方向 |
| 12 | ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-and-Language Navigation in Continuous Environments | 2025-12-24 | arXiv + 官方代码 + 数据/ckpt | topo follow-up / RFT | 直接回答 topo 路线在新一代 post-training 下是否仍强 |
| 13 | NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation | 2024-02-24 | arXiv | video history backbone / planner | video history 是高层理解和规划的重要支点 |
| 14 | DREAMWALKER: Mental Planning for Continuous Vision-and-Language Navigation | 2023-08-14 | ICCV 2023 + arXiv | planning / mental simulation | 是早期 world-model / planning 主线的重要代表 |
| 15 | Open-Nav: Exploring Zero-Shot Vision-and-Language Navigation in Continuous Environment with Open-Source LLMs | 2024-09-27 | arXiv | open-source LLM zero-shot scaffold | zero-shot CE 方向里最值得保留的公开基线之一 |
| 16 | View Invariant Learning for Vision-Language Navigation in Continuous Environments | 2025-07-05 | arXiv | viewpoint robustness / post-training | 直接针对 viewpoint generalization gap，且仍绑定 R2R-CE / RxR-CE |
| 17 | Dynamic Topology Awareness: Breaking the Granularity Rigidity in Vision-Language Navigation | 2026-01-29 | arXiv + 官方代码 | topo granularity | 非常新，且正面修 topo 粒度刚性问题，同时具备代码侦察价值 |
| 18 | Efficient-VLN: A Training-Efficient Vision-Language Navigation Model | 2025-12-11 | arXiv + 项目页（链接异常，未核到可信代码） | history compression / cost-efficient strong baseline | 直接对准 history token 膨胀与 DAgger 成本问题，是当前非常值得保留的高性价比主线参考 |
| 19 | Spatial-VLN: Zero-Shot Vision-and-Language Navigation With Explicit Spatial Perception and Exploration | 2026-01-19 | arXiv + 项目页 | zero-shot / spatial exploration | 直接围绕复杂空间场景的 spatial bottleneck 展开，但更适合作为空间推理与部署参考，不是标准主榜 baseline |
| 20 | NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments | 2025-06-30 | arXiv | world model / online adaptation | 强调环境动态建模与在线适配，和 closed-loop stability 关系紧密 |
| 21 | VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning | 2025-06-20 | arXiv + 项目页 | LVLM / RFT / long-short memory | 把 RFT 直接带入 VLN-CE，是后续 reasoning 路线的重要参照 |
| 22 | GC-VLN: Instruction as Graph Constraints for Training-free Vision-and-Language Navigation | 2025-09-12 | CoRL 2025 + arXiv | training-free / graph constraints | 结构性强，适合作为图约束路线参考 |
| 23 | SpatialNav: Leveraging Spatial Scene Graphs for Zero-Shot Vision-and-Language Navigation | 2026-01-11 | arXiv | scene graph / zero-shot | scene-graph + zero-shot 在 CE 场景里值得保留，但要明确它建立在 pre-exploration 与 sampled subset 设定上 |
| 24 | Safe-VLN: Collision Avoidance for Vision-and-Language Navigation of Autonomous Robots Operating in Continuous Environments | 2023-11-06 | arXiv | obstacle avoidance / recovery | 明确把 collision / recovery 当主问题，非常契合你的痛点 |
| 25 | GridMM: Grid Memory Map for Vision-and-Language Navigation | 2023-07-24 | arXiv | memory / map | memory-map 方向的代表作之一 |
| 26 | Bridging the Gap Between Learning in Discrete and Continuous Environments for Vision-and-Language Navigation | 2022-03-05 | arXiv | waypoint predictor / bridge baseline | 对理解 discrete-to-continuous 接口至关重要 |
| 27 | Cross-modal Map Learning for Vision and Language Navigation | 2022-03-10 | CVPR 2022 + arXiv | explicit map baseline | 显式地图与 waypoint 路线的 solid baseline |
| 28 | 1st Place Solutions for RxR-Habitat Vision-and-Language Navigation Competition (CVPR 2022) | 2022-06-23 | arXiv / challenge report | competition recipe / engineering baseline | 模块化 plan-control recipe 非常关键 |
| 29 | Ground-level Viewpoint Vision-and-Language Navigation in Continuous Environments | 2025-02-26 | arXiv | robot viewpoint gap / deployment | 很适合真实机器人视角偏差这条线 |
| 30 | Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation | 2024-04-02 | arXiv | future observation / lookahead | 未来观测建模与 lookahead exploration 很有启发 |

## 第二部分：建议的 baseline / codebase reconnaissance 优先级

### A. 第一优先：最值得先看代码底座的

1. ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments
2. JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation
3. StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling
4. ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-and-Language Navigation in Continuous Environments
5. Affordances-Oriented Planning using Foundation Models for Continuous Vision-Language Navigation

### B. 第二优先：最值得做高层结构参考的

1. Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation
2. One Agent to Guide Them All: Empowering MLLMs for Vision-and-Language Navigation via Explicit World Representation
3. NavForesee: A Unified Vision-Language World Model for Hierarchical Planning and Dual-Horizon Navigation Prediction
4. Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments
5. NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation
6. CLASH: Collaborative Large-Small Hierarchical Framework for Continuous Vision-and-Language Navigation

### C. 第三优先：最值得补 history / progress / memory / robustness 的

1. JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation
2. StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling
3. Efficient-VLN: A Training-Efficient Vision-Language Navigation Model
4. Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments
5. GridMM: Grid Memory Map for Vision-and-Language Navigation
6. Mind the Error! Detection and Localization of Instruction Errors in Vision-and-Language Navigation
7. Ground-level Viewpoint Vision-and-Language Navigation in Continuous Environments

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
12. MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming
13. Mind the Error! Detection and Localization of Instruction Errors in Vision-and-Language Navigation

原因：这部分论文都很值得保留，但当前更适合作为专项结构参考而不是第一优先复现底座。
- `VLN-Zero`：zero-shot continuous VLN 的代表性系统，官方仓库已可运行，但依赖 environment-specific exploration 与 `OPENAI_API_KEY`，更适合作为零样本部署参考。
- `GC-VLN`：`CoRL 2025` 已确认，图约束与回溯机制非常有启发，但当前官方仓库仍偏项目展示，不能按成熟开源基线处理。
- `MonoDream`：是 monocular VLN-CE 里很值得保留的 latent imagination 路线论文，不用外部 web 数据且跨数据集泛化强，但当前未核到官方代码和项目页。

## 第四部分：本轮新增并纳入内部跟踪池的

1. PROSPECT: Unified Streaming Vision-Language Navigation via Semantic-Spatial Fusion and Latent Predictive Representation
原因：同时覆盖 `streaming context`、`latent predictive learning` 和 `VLN-CE + real robot`，是这轮新增论文里最值得尽快粗读和后续代码侦察的系统工作之一。

2. LatentPilot: Scene-Aware Vision-and-Language Navigation by Dreaming Ahead with Latent Visual Reasoning
原因：直接把 `dreaming ahead` 做进 `R2R-CE / RxR-CE` 主线，并且强调 action-conditioned visual dynamics，和当前“高层语义到低层控制桥接”非常贴近。

3. NaVIDA: Vision-Language Navigation with Inverse Dynamics Augmentation
原因：把 inverse dynamics supervision 和 hierarchical action chunking 用在 VLN 上，既补稳定性也补 longer-horizon visual dynamics，属于结构上很值得精读的新工作。

4. NavTrust: Benchmarking Trustworthiness for Embodied Navigation
原因：虽然是 robustness benchmark，但它直接把 instruction corruption、RGB-depth corruption 和真实部署可靠性带回当前主线，后续做鲁棒性分析时价值很高。

5. VLNVerse: A Benchmark for Vision-Language Navigation with Versatile, Embodied, Realistic Simulation and Evaluation
原因：它不是传统 `R2R-CE` 主榜延伸，而是重新做了 realistic physics 和 full-kinematics embodiment 的大 benchmark，值得作为后续 benchmark 版图更新的重要节点。

6. SmartWay / Fast-SmartWay
原因：这是当前 zero-shot waypoint + backtracking 路线里最值得连读的一组论文，尤其适合补 waypoint quality、history-aware reasoning 和 recovery 机制。

7. InstructNav: Zero-shot System for Generic Instruction Navigation in Unexplored Environment
原因：是 foundation-model zero-shot continuous instruction navigation 的早期关键工作，不只覆盖 `R2R-CE`，还连到 ObjNav 和 real robot，历史位置很重要。

8. Waypoint Models / LAW / Hierarchical Cross-Modal Agent
原因：这三篇是旧表缺失的 foundational chain，补齐后，连续导航从 `robo-vln -> waypoint -> LAW -> ETP / SmartWay` 的方法谱系才完整。

9. ComposableNav: Instruction-Following Navigation in Dynamic Environments via Composable Diffusion
原因：如果后面要专门看 dynamic environment + diffusion trajectory composition，这篇会比单纯 waypoint papers 更接近连续控制建模。

10. FSR-VLN: Fast and Slow Reasoning for Vision-Language Navigation with Hierarchical Multi-modal Scene Graph
原因：虽然不是 Habitat 主榜论文，但它把 hierarchical multi-modal scene graph、fast-slow reasoning 和 real humanoid deployment 串了起来，适合作为 embodied system reference。

11. Zero-Shot Vision-and-Language Navigation with Collision Mitigation in Continuous Environment
原因：这篇比通用 zero-shot paper 更专注于 collision-aware continuous control，对 obstacle avoidance / recovery 支线有直接价值。

12. Enhancing Large Language Models with RAG for Visual Language Navigation in Continuous Environments
原因：问题相关，但目前更适合作为补充性尝试，不宜放在主方法参考的前列。
