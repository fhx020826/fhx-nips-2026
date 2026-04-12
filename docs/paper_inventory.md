# Continuous VLN / VLN-CE 论文总表

## 说明

从本版开始，本表只保留“重新检索得到”的论文条目，不再使用“继承上下文”来源。

补充说明：
- 当前项目的唯一主执行总表已经迁移到 `docs/paper_list_feishu_strict.md`。
- 本文件保留为历史宽口径候选池与检索缓存，不再作为后续粗读顺序或是否保留某篇论文的最终依据。

当前目标：

1. 先建立 `R2R-CE / RxR-CE / VLN-CE` 直接相关论文池。
2. 再扩展到强相关与可迁移方法。
3. 所有条目后续再逐步补齐到固定粗读模板。

## 状态定义

- `已核实`：本轮已联网核实标题、链接、基础设定
- `待深读`：已进入候选池，但还没展开完整粗读

## 字段

| 字段 | 含义 |
|---|---|
| 状态 | 已核实 / 待深读 |
| 年份 | 以 arXiv 首次提交或正式发表年份为准 |
| 论文 | 标题 |
| 类型 | 直接命中 / 强相关 / 可迁移 |
| 数据集/基准 | 重点写 R2R-CE / RxR-CE / VLN-CE 等 |
| 关键词 | 问题标签 |
| 方法范式 | 结构范式 |
| 作用 | 对本项目最直接的参考价值 |
| 来源 | 本轮已核实链接 |
| 当前判断 | 当前最重要的一句判断 |

---

## A. 直接命中 continuous VLN / VLN-CE

| 状态 | 年份 | 论文 | 类型 | 数据集/基准 | 关键词 | 方法范式 | 作用 | 来源 | 当前判断 |
|---|---:|---|---|---|---|---|---|---|---|
| 已核实 | 2020 | Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments | 直接命中 | VLN-CE / R2R-CE / RxR-CE | task setup, continuous control | 任务定义 | 必要起点 | https://arxiv.org/abs/2004.02857 | continuous VLN 的任务起点，必须保留 |
| 已核实 | 2022 | Cross-modal Map Learning for Vision and Language Navigation | 直接命中 | VLN-CE | map, waypoint, explicit spatial representation | cross-modal map + waypoint | map-based baseline / 空间表示参考 | https://arxiv.org/abs/2203.05137 | 早期明确把空间表示做显式化，值得保留 |
| 已核实 | 2022 | Sim-2-Sim Transfer for Vision-and-Language Navigation in Continuous Environments | 直接命中 | VLN-CE | transfer, discrete-to-continuous gap | sim-to-sim transfer | 任务范式迁移参考 | https://arxiv.org/abs/2204.09667 | 解释离散 VLN 到连续 VLN 性能鸿沟的重要工作 |
| 已核实 | 2022 | 1st Place Solutions for RxR-Habitat Vision-and-Language Navigation Competition (CVPR 2022) | 直接命中 | RxR-Habitat / VLN-CE | modular plan-control, waypoint, tryout, history | modular planner-controller | competition SOTA / 强 baseline 参考 | https://arxiv.org/abs/2206.11610 | 竞赛冠军方案，工程与结构都重要 |
| 已核实 | 2022 | Iterative Vision-and-Language Navigation in Continuous Environments | 直接命中（扩展设定） | IR2R-CE | persistent memory, iterative tours | memory-persistent VLN | memory 设定 / benchmark 扩展 | https://github.com/jacobkrantz/IVLN-CE | 如果后面要做长期记忆，这是重要旁支 |
| 已核实 | 2023 | Graph based Environment Representation for Vision-and-Language Navigation in Continuous Environments | 直接命中 | VLN-CE | graph environment representation, object relation | graph environment representation | graph-based env modeling 参考 | https://arxiv.org/abs/2301.04352 | 图式环境表达路线，不应遗漏 |
| 已核实 | 2023 | DREAMWALKER: Mental Planning for Continuous Vision-Language Navigation | 直接命中 | VLN-CE | world model, planning, MCTS | world-model planning | planning 结构参考 | https://openaccess.thecvf.com/content/ICCV2023/papers/Wang_DREAMWALKER_Mental_Planning_for_Continuous_Vision-Language_Navigation_ICCV_2023_paper.pdf | 2023 年很关键的 planning 路线 |
| 已核实 | 2023 | GridMM: Grid Memory Map for Vision-and-Language Navigation | 直接命中 | R2R-CE | grid memory, history, map | grid memory map | history / map 参考 | https://arxiv.org/abs/2307.12907 | memory-map 路线代表作之一 |
| 已核实 | 2023 | Safe-VLN: Collision Avoidance for Vision-and-Language Navigation of Autonomous Robots Operating in Continuous Environments | 直接命中 | R2R-CE | collision avoidance, recovery | waypoint + collision mitigation | obstacle avoidance / recovery 参考 | https://arxiv.org/abs/2311.02817 | 明确把碰撞问题当主问题处理，与你的判断一致 |
| 已核实 | 2023 | Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation | 直接命中 | VLN-CE | lookahead, neural radiance, exploration | lookahead exploration | 探索与未来观测建模参考 | https://arxiv.org/abs/2404.01943 | 代表一类“预测未来观测再决策”的路线 |
| 已核实 | 2024 | Cog-GA: A Large Language Models-based Generative Agent for Vision-Language Navigation in Continuous Environments | 直接命中 | VLN-CE benchmarks | cognitive map, waypoint, reflection | LLM agent + waypoint | 高层 agent 结构参考 | https://arxiv.org/abs/2409.02522 | LLM 化 continuous VLN 的代表之一 |
| 已核实 | 2024 | ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments | 直接命中 | R2R-CE / RxR-CE | topo planning, ghost node, tryout, recovery | topo planning | topo baseline / codebase 参考 | https://arxiv.org/abs/2304.03047 | topo 路线代表作，不能遗漏 |
| 已核实 | 2024 | NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation | 直接命中 | VLN-CE | video history, next-step planning | video-based VLM planner | history backbone 参考 | https://arxiv.org/abs/2402.15852 | video history 路线代表作 |
| 已核实 | 2024 | Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments | 直接命中 | R2R-CE / RxR-CE | zero-shot, sub-instruction, constraints, progress | constraint-aware planner | zero-shot / progress / subgoal 参考 | https://arxiv.org/abs/2412.10137 | 很值得重点深读，和 progress / bridge 直接相关 |
| 已核实 | 2024 | Open-Nav: Exploring Zero-Shot Vision-and-Language Navigation in Continuous Environment with Open-Source LLMs | 直接命中 | VLN-CE / real-world | zero-shot, CoT, progress estimation | open-source LLM reasoning | zero-shot reasoning scaffold 参考 | https://arxiv.org/abs/2409.18794 | open-source LLM zero-shot continuous VLN 的代表工作 |
| 已核实 | 2025 | Ground-level Viewpoint Vision-and-Language Navigation in Continuous Environments | 直接命中 | continuous VLN benchmarks | viewpoint gap, scale, embodied height | viewpoint adaptation | 低视角/真机视角缺口参考 | https://arxiv.org/abs/2502.19024 | 对真实机器人视角偏差问题重要 |
| 已核实 | 2025 | TRAVEL: Training-Free Retrieval and Alignment for Vision-and-Language Navigation | 直接命中 | R2R-Habitat | training-free, retrieval, alignment, topo map | modular retrieval-alignment | training-free / map-retrieval 路线参考 | https://arxiv.org/abs/2502.07306 | 虽依赖环境模型，但仍在同问题空间内 |
| 已核实 | 2025 | LaViRA: Language-Vision-Robot Actions Translation for Zero-Shot Vision Language Navigation in Continuous Environments | 直接命中 | VLN-CE | zero-shot, hierarchical control, robot action translation | hierarchical planner-controller | 真机部署 / 零样本 bridge 参考 | https://arxiv.org/abs/2510.19655 | 典型“大模型高层 + 小模型感知/控制”结构 |
| 已核实 | 2025 | NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments | 直接命中 | VLN-CE benchmarks | world model, evolution memory | self-evolving world model | world-model 路线新作 | https://arxiv.org/abs/2506.23468 | 2025 新增 world-model 方向，需重点跟踪 |
| 已核实 | 2025 | VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning | 直接命中 | VLN-CE benchmark | LVLM, RFT, time-decayed reward, long-short memory sampling | end-to-end LVLM + RFT | reasoning/RFT 路线参考 | https://arxiv.org/abs/2506.17221 | 直接把 RFT 用到连续 VLN，值得保留 |
| 已核实 | 2025 | StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling | 直接命中 | VLN-CE benchmarks | streaming, slow-fast memory, low latency | streaming VLN | history compression / streaming inference 参考 | https://arxiv.org/abs/2507.05240 | history 压缩与在线推理的重要新作 |
| 已核实 | 2025 | monoVLN: Bridging the Observation Gap between Monocular and Panoramic Vision and Language Navigation | 直接命中 | R2R-CE / RxR-CE | monocular, observation gap, uncertainty | monocular VLN | 单目设定与观测缺口参考 | https://papers.cool/venue/Lu_monoVLN_Bridging_the_Observation_Gap_between_Monocular_and_Panoramic_Vision%40ICCV2025%40CVF | 虽是单目设定，但对观测缺口问题有价值 |
| 已核实 | 2025 | MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming | 直接命中 | R2R-CE / RxR-CE | monocular, panoramic dreaming | monocular + latent panoramic completion | 观测补全 / latent bridge 参考 | https://www.sciencestack.ai/paper/2508.02549 | 单目 VLN-CE 新方向，需进一步核实正式页 |
| 已核实 | 2025 | DAgger Diffusion Navigation: DAgger Boosted Diffusion Policy for Vision-Language Navigation | 直接命中 | VLN-CE benchmarks | diffusion, DAgger, action expert | diffusion policy | diffusion baseline / codebase 参考 | https://arxiv.org/abs/2508.09444 | diffusion 路线的关键 direct-hit 论文 |
| 已核实 | 2025 | Efficient-VLN: A Training-Efficient Vision-Language Navigation Model | 直接命中 | R2R-CE / RxR-CE | memory efficiency, training efficiency | efficient VLN | training recipe / efficient memory 参考 | https://papers.cool/arxiv/2512.10310 | 可能对“最小代价做强 baseline”有用 |
| 已核实 | 2025 | ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-Language Navigation in Continuous Environments | 直接命中 | VLN-CE | topo planning, reinforcement fine-tuning | topo planning + RFT | topo 路线后续工作 | https://huggingface.co/papers/2512.20940 | 是 ETP 路线的后续演进，值得持续关注 |
| 已核实 | 2025 | NavForesee: A Unified Vision-Language World Model for Hierarchical Planning and Dual-Horizon Navigation Prediction | 直接命中 | R2R-CE / RxR-CE | unified world model, hierarchical planning, dual-horizon prediction | planner + world model | 高层规划与局部预测统一参考 | https://arxiv.org/abs/2512.01550 | 2025 年很值得跟踪的统一 world-model 路线 |
| 已核实 | 2025 | Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation | 直接命中 | VLN benchmarks（含连续场景） | dual-system, waypoint reasoning, diffusion control | global planner + local diffusion policy | DualVLN，关键工作，不能遗漏 | https://arxiv.org/abs/2512.08186 | 这是你点名漏掉的关键工作，已补入 |
| 已核实 | 2025 | CLASH: Collaborative Large-Small Hierarchical Framework for Continuous Vision-and-Language Navigation | 直接命中 | VLN-CE leaderboard | large-small collaboration, hierarchy, uncertainty fusion | large-small hierarchical collaboration | 2025 SOTA / leaderboard 参考 | https://arxiv.org/abs/2512.10360 | 明确宣称 VLN-CE leaderboard 1st，需要重点跟踪 |
| 已核实 | 2026 | EmergeNav: Structured Embodied Inference for Zero-Shot Vision-and-Language Navigation in Continuous Environments | 直接命中 | VLN-CE | zero-shot, structure, dual-memory, progress | structured embodied inference | 2026 新工作，优先跟踪 | https://arxiv.org/abs/2603.16947 | 非常贴近“高层结构化执行”问题 |
| 已核实 | 2026 | Dynamic Topology Awareness: Breaking the Granularity Rigidity in Vision-Language Navigation | 直接命中 | R2R-CE / RxR-CE | topo density, dynamic granularity, graph adaptation | dynamic topo planning | topo granularity / graph management 参考 | https://arxiv.org/abs/2601.21751 | 直接针对 topo granularity rigidity，与你关心的问题高度一致 |
| 已核实 | 2026 | Let's Reward Step-by-Step: Step-Aware Contrastive Alignment for Vision-Language Navigation in Continuous Environments | 直接命中 | VLN-CE benchmarks | step reward, dense alignment, long-horizon credit assignment | step-aware alignment / reward shaping | 训练范式 / progress credit 参考 | https://arxiv.org/abs/2603.09740 | 对“长时 credit assignment”非常值得关注 |
| 已核实 | 2026 | SpatialNav: Leveraging Spatial Scene Graphs for Zero-Shot Vision-and-Language Navigation | 直接命中 | R2R-CE / RxR-CE | scene graph, global map, zero-shot reasoning | spatial scene graph + MLLM | global map / spatial reasoning 参考 | https://arxiv.org/abs/2601.06806 | zero-shot 连续 VLN 的空间图路线 |

---

## B. 强相关候选（已重新检索到，但仍需继续筛）

| 状态 | 年份 | 论文 | 类型 | 数据集/基准 | 关键词 | 方法范式 | 作用 | 来源 | 当前判断 |
|---|---:|---|---|---|---|---|---|---|---|
| 已核实 | 2024 | Enhancing Large Language Models with RAG for Visual Language Navigation in Continuous Environments | 强相关 | R2R-CE / RxR-CE | RAG, LLM, retrieval | LLM + retrieval | 外部知识注入路线参考 | https://www.mdpi.com/2079-9292/14/5/909/xml | 更像应用型增强，创新深度可能有限 |
| 已核实 | 2024 | Mind the Error! Detection and Localization of Instruction Errors in Vision-and-Language Navigation | 强相关 | R2R-IE-CE | error detection, robustness | instruction error handling | robustness / benchmark 扩展 | https://github.com/intelligolabs/R2RIE-CE | 不是主 benchmark，但可为 robustness 提供支线 |
| 已核实 | 2025 | GC-VLN: Instruction as Graph Constraints for Training-free Vision-and-Language Navigation | 强相关 | continuous environments | graph constraints, training-free, structure | graph constraint optimization | training-free / graph reasoning 参考 | https://openreview.net/forum?id=mjYKNIRqpy | 对“结构化约束”与“无需再训练”有启发 |
| 已核实 | 2025 | HA-VLN: A Benchmark for Human-Aware Navigation in Discrete–Continuous Environments with Dynamic Multi-Human Interactions, Real-World Validation, and an Open Leaderboard | 强相关（benchmark） | HA-VLN / dynamic humans | benchmark, human-aware navigation | benchmark / dataset | 动态人类交互 benchmark 参考 | https://arxiv.org/abs/2503.14229 | benchmark 工作不能遗漏 |
| 已核实 | 2026 | SeqWalker: Sequential-Horizon Vision-and-Language Navigation with Hierarchical Planning | 强相关（扩展设定） | SH IR2R-CE | long-horizon, hierarchical planning, sequential instructions | hierarchical planning | 长序列指令连续导航参考 | https://arxiv.org/abs/2601.04699 | 长程 instruction following 的新 benchmark/方法结合体 |
| 已核实 | 2025 | VPN: Visual Prompt Navigation | 强相关（benchmark） | R2R-VP / R2R-CE-VP | visual prompt, benchmark extension | new task + baseline | benchmark/setting 扩展参考 | https://arxiv.org/abs/2508.01766 | 虽不再是语言指令，但连续导航 benchmark 扩展应保留 |
| 已核实 | 2024 | Human-Aware Vision-and-Language Navigation: Bridging Simulation to Reality with Dynamic Human Interactions | 强相关（benchmark） | HA-R2R / HA3D | dynamic humans, sim2real, benchmark | new simulator + benchmark + baselines | 动态人类场景 benchmark 起点 | https://arxiv.org/abs/2406.19236 | 是 HA-VLN 的前置工作，不能漏 |
| 已核实 | 2026 | NavTrust: Benchmarking Trustworthiness for Embodied Navigation | 强相关（benchmark） | NavTrust | robustness, corruptions, trustworthiness | benchmark | continuous VLN robustness benchmark 参考 | https://arxiv.org/abs/2603.19229 | 虽非纯 VLN-CE 专用，但对鲁棒性评测很重要 |
| 已核实 | 2024 | RoomTour3D: Geometry-Aware Video-Instruction Tuning for Embodied Navigation | 强相关（dataset） | RoomTour3D | dataset, video instruction, geometry-aware tuning | dataset / pretraining corpus | 数据与 video-instruction tuning 参考 | https://arxiv.org/abs/2412.08591 | 数据和预训练资源层面的重要补充 |
| 已核实 | 2023 | Towards Learning a Generalist Model for Embodied Navigation | 强相关（foundation） | multi-task embodied navigation | generalist, schema instruction, unified interface | generalist embodied navigation | foundation navigation 参考 | https://arxiv.org/abs/2312.02010 | foundation 路线不能遗漏 |
| 已核实 | 2025 | IndoorUAV: Benchmarking Vision-Language UAV Navigation in Continuous Indoor Environments | 强相关（benchmark） | IndoorUAV-VLN / IndoorUAV-VLA | benchmark, indoor UAV, continuous indoor VLN | benchmark + method | 连续室内 VLN benchmark 扩展 | https://arxiv.org/abs/2512.19024 | 虽是 UAV，但属于同问题空间的连续 VLN 扩展 |
| 已核实 | 2025 | DyNaVLM: Zero-Shot Vision-Language Navigation System with Dynamic Viewpoints and Self-Refining Graph Memory | 强相关（zero-shot） | GOAT / ObjectNav / real-world | dynamic viewpoint, graph memory, training-free | graph memory + VLM | zero-shot memory / graph 参考 | https://arxiv.org/abs/2506.15096 | 虽非主 benchmark，但与 zero-shot continuous navigation 很贴近 |
| 已核实 | 2025 | VLN-Zero: Rapid Exploration and Cache-Enabled Neurosymbolic Vision-Language Planning for Zero-Shot Transfer in Robot Navigation | 强相关（zero-shot） | robot navigation benchmarks | neurosymbolic planning, cache, zero-shot | scene graph + planner | zero-shot planning 参考 | https://arxiv.org/abs/2509.18592 | 零样本 neurosymbolic 路线值得保留 |
| 已核实 | 2025 | JanusVLN: Decoupling Semantics and Spatiality with Dual Implicit Memory for Vision-Language Navigation | 强相关（memory） | VLN benchmarks | dual implicit memory, semantic-spatial decoupling | implicit memory | memory 新范式参考 | https://arxiv.org/abs/2509.22548 | 2025 memory 路线很新的代表作 |
| 已核实 | 2025 | InternVLA-N1: An Open Dual-System Vision-Language Navigation Foundation Model with Learned Latent Plans | 强相关（foundation） | navigation foundation benchmarks | dual-system, latent plans | foundation model | foundation navigation 参考 | https://internrobotics.github.io/internvla-n1.github.io/static/pdfs/InternVLA_N1.pdf | 双系统 foundation 导航工作，需重点关注 |
| 已核实 | 2026 | HiMemVLN: Enhancing Reliability of Open-Source Zero-Shot Vision-and-Language Navigation with Hierarchical Memory System | 强相关（zero-shot） | simulated + real-world VLN | hierarchical memory, open-source LLM, reliability | hierarchical memory system | open-source zero-shot memory 参考 | https://arxiv.org/abs/2603.14807 | 2026 新增 memory/reliability 路线 |
| 已核实 | 2020 | RxR: Multilingual Guided Vision-and-Language Navigation via Benchmark Translation | 强相关（benchmark lineage） | RxR | multilingual instruction benchmark | dataset / benchmark | RxR-CE 的语言数据来源 | https://arxiv.org/abs/2010.07954 | 连续 RxR-CE 的上游 benchmark，必须保留 |
| 已核实 | 2018 | Room-to-Room: Vision-and-Language Navigation with Matterport3D | 强相关（benchmark lineage） | R2R | benchmark, instruction following | dataset / benchmark | R2R-CE 的上游 benchmark | https://arxiv.org/abs/1711.07280 | 整个赛道的起点之一 |
| 已核实 | 2019 | Habitat: A Platform for Embodied AI Research | 强相关（platform） | Habitat | simulator, embodied platform | simulator / platform | continuous VLN-CE 所依赖的平台基础 | https://arxiv.org/abs/1904.01201 | continuous 环境实验平台基础工作 |
| 已核实 | 2021 | Habitat 2.0: Training Home Assistants to Rearrange their Habitat | 强相关（platform） | Habitat 2.0 | simulator, embodied benchmark | simulator / platform | Habitat 平台演进背景 | https://arxiv.org/abs/2106.14405 | 虽非 VLN 专属，但平台演进相关 |

---

## B3. VLN 方法演进链（离散/上游，但与当前任务高度相关）

| 状态 | 年份 | 论文 | 类型 | 数据集/基准 | 关键词 | 方法范式 | 作用 | 来源 | 当前判断 |
|---|---:|---|---|---|---|---|---|---|---|
| 已核实 | 2018 | Speaker-Follower Models for Vision-and-Language Navigation | 强相关（method lineage） | R2R | speaker-follower, search | seq2seq + speaker reranking | 早期经典 baseline | https://arxiv.org/abs/1806.02724 | 经典祖先工作，必须保留 |
| 已核实 | 2019 | Robust Navigation with Language Pretraining and Stochastic Sampling | 强相关（method lineage） | R2R | pretraining, stochastic sampling | pretrained navigation | 预训练路线早期代表 | https://arxiv.org/abs/1909.02244 | strong baseline，后续常被比较 |
| 已核实 | 2020 | Towards Learning a Generic Agent for Vision-and-Language Navigation via Pre-Training | 强相关（method lineage） | R2R / RxR | pretraining | PREVALENT | 预训练范式关键工作 | https://arxiv.org/abs/2002.10638 | 后续许多工作都会对比 |
| 已核实 | 2020 | Active Visual Information Gathering for Vision-Language Navigation | 强相关（method lineage） | R2R | active exploration, uncertainty | active exploration | exploration / recovery 参考 | https://arxiv.org/abs/2007.08037 | 与 continuous 中探索和恢复相关 |
| 已核实 | 2020 | Vision-Language Navigation with Self-Supervised Auxiliary Reasoning Tasks | 强相关（method lineage） | R2R | auxiliary reasoning, progress | auxiliary reasoning | progress / reasoning 参考 | https://openaccess.thecvf.com/content_CVPR_2020/papers/Zhu_Vision-Language_Navigation_With_Self-Supervised_Auxiliary_Reasoning_Tasks_CVPR_2020_paper.pdf | progress 学习链条应保留 |
| 已核实 | 2020 | Improving Vision-and-Language Navigation with Image-Text Pairs from the Web | 强相关（method lineage） | R2R | web data, grounding | web pretraining | 数据扩展思路参考 | https://arxiv.org/abs/2004.14973 | 数据增强链条重要一环 |
| 已核实 | 2020 | Hierarchical Cross-Modal Agent for Robotics Vision-and-Language Navigation | 强相关（method lineage） | robotics VLN | hierarchical, subgoal, low-level control | hierarchical agent | 连续 VLN 双层架构早期代表 | https://arxiv.org/abs/2104.10674 | 与当前问题定义高度契合 |
| 已核实 | 2021 | VLN-BERT: A Recurrent Vision-and-Language BERT for Navigation | 强相关（method lineage） | R2R | recurrent VLN-BERT | recurrent transformer | VLN backbone 关键工作 | https://openaccess.thecvf.com/content/CVPR2021/papers/Hong_VLN_BERT_A_Recurrent_Vision-and-Language_BERT_for_Navigation_CVPR_2021_paper.pdf | backbone 链条重要工作 |
| 已核实 | 2021 | History Aware Multimodal Transformer for Vision-and-Language Navigation | 强相关（method lineage） | R2R / RxR | history transformer, multimodal memory | HAMT | history 建模经典工作 | https://proceedings.neurips.cc/paper/2021/file/2e5c2cb8d13e8fba78d95211440ba326-Paper.pdf | history / memory 祖先工作 |
| 已核实 | 2021 | SOAT: A Scene- and Object-Aware Transformer for Vision-and-Language Navigation | 强相关（method lineage） | R2R | scene/object aware transformer | transformer + object awareness | scene/object modeling 参考 | https://arxiv.org/abs/2110.14143 | solid transformer baseline |
| 已核实 | 2021 | The Road to Know-Where: An Object-and-Room Informed Sequential BERT for Indoor Vision-Language Navigation | 强相关（method lineage） | R2R | room/object reasoning | ORIST | room-object reasoning 参考 | https://openaccess.thecvf.com/content/ICCV2021/papers/Qi_The_Road_To_Know-Where_An_Object-and-Room_Informed_Sequential_BERT_for_ICCV_2021_paper.pdf | room/object 结构化先验代表 |
| 已核实 | 2021 | Vision-Language Navigation with Random Environmental Mixup | 强相关（method lineage） | R2R | augmentation, generalization | environment mixup | 泛化增强链条参考 | https://openaccess.thecvf.com/content/ICCV2021/papers/Liu_Vision-Language_Navigation_With_Random_Environmental_Mixup_ICCV_2021_paper.pdf | 泛化相关工作 |
| 已核实 | 2022 | HOP: History-and-Order Aware Pre-Training for Vision-and-Language Navigation | 强相关（method lineage） | R2R / RxR | history, order-aware pretraining | pretraining | history pretraining 代表作 | https://ieeexplore.ieee.org/document/9880046 | history 预训练路线重要工作 |
| 已核实 | 2022 | LOViS: Learning Orientation and Visual Signals for Vision and Language Navigation | 强相关（method lineage） | R2R | orientation, visual signals | orientation-aware model | 朝向建模参考 | https://aclanthology.org/2022.coling-1.505.pdf | orientation 建模链条 |
| 已核实 | 2022 | Visual-Language Navigation Pretraining via Prompt-based Environmental Self-exploration | 强相关（method lineage） | R2R / RxR | prompt, self-exploration | prompt-based pretraining | 环境自探索预训练 | https://arxiv.org/abs/2203.04006 | pretraining 思路补充 |
| 已核实 | 2022 | Target-Driven Structured Transformer Planner for Vision-Language Navigation | 强相关（method lineage） | R2R | structured planner | structured transformer planner | planner 设计参考 | https://arxiv.org/abs/2207.11201 | structured planning 路线 |
| 已核实 | 2022 | CLIP-Nav: Using CLIP for Zero-Shot Vision-and-Language Navigation | 强相关（method lineage） | R2R | CLIP, zero-shot | CLIP-based zero-shot | zero-shot 链条前置参考 | https://arxiv.org/abs/2211.16649 | zero-shot continuous work 的上游参考 |
| 已核实 | 2022 | Diagnosing Vision-and-Language Navigation: What Really Matters | 强相关（analysis） | R2R | diagnosis, evaluation | analysis | 误差分析与评价参考 | https://aclanthology.org/2022.naacl-main.438.pdf | 评价分析工作不能漏 |
| 已核实 | 2023 | Adaptive Zone-aware Hierarchical Planner for Vision-Language Navigation | 强相关（method lineage） | R2R | hierarchical planner | zone-aware hierarchical planning | hierarchical planning 参考 | https://openaccess.thecvf.com/content/CVPR2023/papers/Gao_Adaptive_Zone-Aware_Hierarchical_Planner_for_Vision-Language_Navigation_CVPR_2023_paper.pdf | 与 continuous 分层控制直接相关 |
| 已核实 | 2023 | Bird's-Eye-View Scene Graph for Vision-Language Navigation | 强相关（method lineage） | R2R | BEV scene graph | scene graph | spatial graph 参考 | https://arxiv.org/abs/2308.04758 | 与 SpatialNav / topo 路线相关 |
| 已核实 | 2023 | Masked Path Modeling for Vision-and-Language Navigation | 强相关（method lineage） | R2R | masked path | masked modeling | path modeling 参考 | https://arxiv.org/abs/2305.14268 | 路径建模工作 |
| 已核实 | 2023 | Improving Vision-and-Language Navigation by Generating Future-View Image Semantics | 强相关（method lineage） | R2R | future view semantics | future prediction | future-view 链条前置工作 | https://arxiv.org/abs/2304.04907 | 与 lookahead / imagination 路线直接相关 |
| 已核实 | 2023 | A New Path: Scaling Vision-and-Language Navigation with Synthetic Instructions and Imitation Learning | 强相关（method lineage） | R2R / RxR | synthetic instruction, scaling | scaling with synthetic data | 数据扩展与规模化训练 | https://arxiv.org/abs/2210.03112 | scale 路线参考 |
| 已核实 | 2023 | Lana: A Language-Capable Navigator for Instruction Following and Generation | 强相关（method lineage） | R2R | follow and generate | navigator-generator | 指令生成/跟随统一 | https://arxiv.org/abs/2303.08409 | follow+generate 路线 |
| 已核实 | 2023 | KERM: Knowledge Enhanced Reasoning for Vision-and-Language Navigation | 强相关（method lineage） | R2R | knowledge reasoning | knowledge enhanced reasoning | reasoning 路线参考 | https://openaccess.thecvf.com/content/CVPR2023/papers/Li_KERM_Knowledge_Enhanced_Reasoning_for_Vision-and-Language_Navigation_CVPR_2023_paper.pdf | reasoning 增强工作 |
| 已核实 | 2023 | PASTS: Progress-Aware Spatio-Temporal Transformer Speaker for Vision-and-Language Navigation | 强相关（method lineage） | R2R | progress-aware, speaker | progress-aware speaker | progress 路线延伸 | https://arxiv.org/abs/2305.11918 | progress 相关工作 |
| 已核实 | 2018 | Reinforced Cross-Modal Matching and Self-Supervised Imitation Learning for Vision-Language Navigation | 强相关（method lineage） | R2R | cross-modal matching, SIL | RL + self-supervised imitation | 经典强化学习/匹配路线 | https://arxiv.org/abs/1811.10092 | 早期高影响力 VLN 方法 |
| 已核实 | 2019 | Self-Monitoring Navigation Agent via Auxiliary Progress Estimation | 强相关（method lineage） | R2R | progress estimation, self-monitoring | progress monitor | progress 建模经典工作 | https://arxiv.org/abs/1901.03035 | progress 线的关键祖先 |
| 已核实 | 2019 | Tactical Rewind: Self-Correction via Backtracking in Vision-and-Language Navigation | 强相关（method lineage） | R2R | backtracking, search | FAST navigator | self-correction / search 经典工作 | https://arxiv.org/abs/1903.02547 | backtracking/FAST 不能遗漏 |
| 已核实 | 2019 | Learning to Navigate Unseen Environments: Back Translation with Environmental Dropout | 强相关（method lineage） | R2R | back-translation, env dropout | augmentation + back-translation | 泛化增强经典工作 | https://arxiv.org/abs/1904.04195 | EnvDrop 是重要上游方法 |
| 已核实 | 2019 | Stay on the Path: Instruction Fidelity in Vision-and-Language Navigation | 强相关（benchmark/analysis） | R4R | instruction fidelity, metric | benchmark / metric | R4R 与 CLS 指标来源 | https://arxiv.org/abs/1905.12255 | 长路径与 fidelity 评价关键工作 |
| 已核实 | 2019 | Vision-and-Dialog Navigation | 强相关（benchmark） | CVDN / NDH | dialog history, cooperative navigation | benchmark / task | dialog-based VLN 重要支线 | https://arxiv.org/abs/1907.04957 | 长历史/多轮指令相关 |
| 已核实 | 2019 | REVERIE: Remote Embodied Visual Referring Expression in Real Indoor Environments | 强相关（benchmark） | REVERIE | object grounding, embodied referring | benchmark / task | object-oriented VLN 支线 | https://arxiv.org/abs/1904.10151 | 上游相关 benchmark |
| 已核实 | 2019 | Learning To Follow Directions in Street View | 强相关（benchmark） | StreetNav | street-scale navigation | benchmark / task | open-world navigation 早期工作 | https://arxiv.org/abs/1903.00401 | 更广义导航任务支线 |
| 已核实 | 2018 | Touchdown: Natural Language Navigation and Spatial Reasoning in Visual Street Environments | 强相关（benchmark） | Touchdown | street-scale, spatial reasoning | benchmark / task | open-world language navigation 支线 | https://arxiv.org/abs/1811.12354 | spatial reasoning benchmark |
| 已核实 | 2020 | Evolving Graphical Planner: Contextual Global Planning for Vision-and-Language Navigation | 强相关（method lineage） | R2R | global planning, graph planner | graphical planner | graph planning 经典工作 | https://arxiv.org/abs/2007.05655 | topo / graph 路线前置工作 |
| 已核实 | 2021 | SOON: Scenario Oriented Object Navigation with Graph-based Exploration | 强相关（benchmark） | SOON / FAO | object navigation, graph exploration | benchmark + GBE | object-oriented navigation 支线 | https://arxiv.org/abs/2103.17138 | 与图探索和从任意点导航相关 |
| 已核实 | 2021 | Core Challenges in Embodied Vision-Language Planning | 强相关（survey） | EVLP | survey, taxonomy, challenges | survey | 全貌归纳参考 | https://arxiv.org/abs/2106.13948 | 构建研究地图时应保留 |
| 已核实 | 2021 | Scene-Intuitive Agent for Remote Embodied Visual Grounding | 强相关（method lineage） | REVERIE | memory-augmented grounding | memory + grounding | object grounding 路线参考 | https://arxiv.org/abs/2103.12944 | REVERIE 方法线参考 |
| 已核实 | 2022 | Aerial Vision-and-Dialog Navigation | 强相关（benchmark） | AVDN | aerial dialog navigation | benchmark / task | 连续 aerial VLN 支线 | https://arxiv.org/abs/2205.12219 | 连续对话导航扩展 |
| 已核实 | 2022 | Reinforced Structured State-Evolution for Vision-Language Navigation | 强相关（method lineage） | R2R / R4R | graph state, layout reasoning | structured state evolution | graph state 参考 | https://arxiv.org/abs/2204.09280 | graph / structured state 路线 |
| 已核实 | 2025 | PanoGen++: Domain-Adapted Text-Guided Panoramic Environment Generation for Vision-and-Language Navigation | 强相关（data augmentation） | R2R / R4R / CVDN | generation, augmentation, diffusion | environment generation | 数据增强与环境扩展 | https://arxiv.org/abs/2503.09938 | 用生成环境增强 VLN 的路线 |
| 已核实 | 2024 | Volumetric Environment Representation for Vision-Language Navigation | 强相关（method lineage） | R2R / REVERIE / R4R | 3D occupancy, volumetric memory | volumetric environment representation | 3D scene理解与环境建模参考 | https://arxiv.org/abs/2403.14158 | continuous 3D 场景建模很有借鉴意义 |
| 已核实 | 2020 | Language and Visual Entity Relationship Graph for Agent Navigation | 强相关（method lineage） | R2R / R4R | entity relationship graph | graph message passing | 图关系建模参考 | https://arxiv.org/abs/2010.09304 | 图关系推理路线应保留 |
| 已核实 | 2019 | Stay on the Path: Instruction Fidelity in Vision-and-Language Navigation | 强相关（benchmark） | R4R | CLS, instruction fidelity, long path | benchmark / metric | R4R 与 CLS 指标来源 | https://arxiv.org/abs/1905.12255 | 长路径与 fidelity 评价关键工作 |
| 已核实 | 2019 | Chasing Ghosts: Instruction Following as Bayesian State Tracking | 强相关（method lineage） | R2R | Bayesian state tracking, semantic map | Bayes filter + mapper | explainable state-tracking 路线 | https://arxiv.org/abs/1907.02022 | map/state tracking 经典工作 |
| 已核实 | 2020 | The RobotSlang Benchmark: Dialog-guided Robot Localization and Navigation | 强相关（benchmark） | RobotSlang / NDH | dialog-guided navigation | benchmark / task | dialog history 导航支线 | https://arxiv.org/abs/2010.12639 | dialog-based导航扩展，应保留 |
| 已核实 | 2023 | Target-Grounded Graph-Aware Transformer for Aerial Vision-and-Dialog Navigation | 强相关（challenge winner） | AVDN Challenge | graph-aware transformer, aerial dialog | challenge winner | aerial dialog challenge 方案 | https://arxiv.org/abs/2308.11561 | aerial连续导航支线工作 |
| 已核实 | 2022 | Vision-and-Language Navigation: A Survey of Tasks, Methods, and Future Directions | 强相关（survey） | VLN field | survey, taxonomy | survey | 全貌梳理直接参考 | https://arxiv.org/abs/2203.12667 | 做研究地图必须保留 |
| 已核实 | 2024 | Vision-Language Navigation with Embodied Intelligence: A Survey | 强相关（survey） | VLN field | survey, embodied intelligence | survey | embodied VLN survey | https://arxiv.org/abs/2402.14304 | 更贴近 embodied 视角 |
| 已核实 | 2024 | Vision-and-Language Navigation Today and Tomorrow: A Survey in the Era of Foundation Models | 强相关（survey） | VLN field | survey, foundation models | survey | foundation model 时代综述 | https://arxiv.org/abs/2407.07035 | 近年 foundation 方向综述 |

---

## C. 下一步优先深读顺序

### C1. 最优先

1. Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments
2. DREAMWALKER
3. Safe-VLN
4. NavMorph
5. EmergeNav
6. Dynamic Topology Awareness
7. Step-Aware Contrastive Alignment
8. ETPNav
9. NaVid
10. NavForesee
11. DualVLN
12. SpatialNav
13. LaViRA
14. StreamVLN
15. DAgger Diffusion Navigation
16. Open-Nav
17. CLASH

### C4. benchmark / dataset / setting 扩展

1. HA-VLN
2. Human-Aware Vision-and-Language Navigation
3. VPN / R2R-CE-VP
4. NavTrust
5. SeqWalker / SH IR2R-CE
6. RoomTour3D
7. RxR / R2R
8. Habitat / Habitat 2.0
9. DyNaVLM / VLN-Zero / HiMemVLN
10. InternVLA-N1 / JanusVLN

### C2. 第二梯队

1. Cross-modal Map Learning for Vision and Language Navigation
2. GridMM
3. Cog-GA
4. Efficient-VLN
5. ETP-R1
6. Sim-2-Sim Transfer
7. RxR-Habitat Competition Winner
8. Graph based Environment Representation
9. VLN-R1
10. TRAVEL

### C3. 扩展设定

1. Iterative Vision-and-Language Navigation in Continuous Environments
2. monoVLN
3. MonoDream
4. Mind the Error!

---

## D. 当前缺口

1. 还没有完成 `2023–2026` 全量扫表，特别是 2025–2026 可能还有遗漏。
2. 还没有把直接命中论文逐篇展开成固定粗读模板。
3. `monoVLN / MonoDream / Efficient-VLN / ETP-R1 / NavForesee / DualVLN / SpatialNav / LaViRA / StreamVLN / Open-Nav / DAgger Diffusion Navigation / RoomTour3D` 当前仍需进一步补齐正式发表信息、项目页、代码页。
