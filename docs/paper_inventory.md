# Continuous VLN / VLN-CE 论文总表

## 说明

从本版开始，本表只保留“重新检索得到”的论文条目，不再使用“继承上下文”来源。

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
| 已核实 | 2022 | Iterative Vision-and-Language Navigation in Continuous Environments | 直接命中（扩展设定） | IR2R-CE | persistent memory, iterative tours | memory-persistent VLN | memory 设定 / benchmark 扩展 | https://github.com/jacobkrantz/IVLN-CE | 如果后面要做长期记忆，这是重要旁支 |
| 已核实 | 2023 | DREAMWALKER: Mental Planning for Continuous Vision-Language Navigation | 直接命中 | VLN-CE | world model, planning, MCTS | world-model planning | planning 结构参考 | https://openaccess.thecvf.com/content/ICCV2023/papers/Wang_DREAMWALKER_Mental_Planning_for_Continuous_Vision-Language_Navigation_ICCV_2023_paper.pdf | 2023 年很关键的 planning 路线 |
| 已核实 | 2023 | GridMM: Grid Memory Map for Vision-and-Language Navigation | 直接命中 | R2R-CE | grid memory, history, map | grid memory map | history / map 参考 | https://arxiv.org/abs/2307.12907 | memory-map 路线代表作之一 |
| 已核实 | 2023 | Safe-VLN: Collision Avoidance for Vision-and-Language Navigation of Autonomous Robots Operating in Continuous Environments | 直接命中 | R2R-CE | collision avoidance, recovery | waypoint + collision mitigation | obstacle avoidance / recovery 参考 | https://arxiv.org/abs/2311.02817 | 明确把碰撞问题当主问题处理，与你的判断一致 |
| 已核实 | 2024 | Cog-GA: A Large Language Models-based Generative Agent for Vision-Language Navigation in Continuous Environments | 直接命中 | VLN-CE benchmarks | cognitive map, waypoint, reflection | LLM agent + waypoint | 高层 agent 结构参考 | https://arxiv.org/abs/2409.02522 | LLM 化 continuous VLN 的代表之一 |
| 已核实 | 2024 | Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments | 直接命中 | R2R-CE / RxR-CE | zero-shot, sub-instruction, constraints, progress | constraint-aware planner | zero-shot / progress / subgoal 参考 | https://arxiv.org/abs/2412.10137 | 很值得重点深读，和 progress / bridge 直接相关 |
| 已核实 | 2025 | NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments | 直接命中 | VLN-CE benchmarks | world model, evolution memory | self-evolving world model | world-model 路线新作 | https://arxiv.org/abs/2506.23468 | 2025 新增 world-model 方向，需重点跟踪 |
| 已核实 | 2025 | monoVLN: Bridging the Observation Gap between Monocular and Panoramic Vision and Language Navigation | 直接命中 | R2R-CE / RxR-CE | monocular, observation gap, uncertainty | monocular VLN | 单目设定与观测缺口参考 | https://papers.cool/venue/Lu_monoVLN_Bridging_the_Observation_Gap_between_Monocular_and_Panoramic_Vision%40ICCV2025%40CVF | 虽是单目设定，但对观测缺口问题有价值 |
| 已核实 | 2025 | MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming | 直接命中 | R2R-CE / RxR-CE | monocular, panoramic dreaming | monocular + latent panoramic completion | 观测补全 / latent bridge 参考 | https://www.sciencestack.ai/paper/2508.02549 | 单目 VLN-CE 新方向，需进一步核实正式页 |
| 已核实 | 2025 | Efficient-VLN: A Training-Efficient Vision-Language Navigation Model | 直接命中 | R2R-CE / RxR-CE | memory efficiency, training efficiency | efficient VLN | training recipe / efficient memory 参考 | https://papers.cool/arxiv/2512.10310 | 可能对“最小代价做强 baseline”有用 |
| 已核实 | 2025 | ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-Language Navigation in Continuous Environments | 直接命中 | VLN-CE | topo planning, reinforcement fine-tuning | topo planning + RFT | topo 路线后续工作 | https://huggingface.co/papers/2512.20940 | 是 ETP 路线的后续演进，值得持续关注 |
| 已核实 | 2026 | EmergeNav: Structured Embodied Inference for Zero-Shot Vision-and-Language Navigation in Continuous Environments | 直接命中 | VLN-CE | zero-shot, structure, dual-memory, progress | structured embodied inference | 2026 新工作，优先跟踪 | https://arxiv.org/abs/2603.16947 | 非常贴近“高层结构化执行”问题 |
| 已核实 | 2026 | Dynamic Topology Awareness: Breaking the Granularity Rigidity in Vision-Language Navigation | 直接命中 | R2R-CE / RxR-CE | topo density, dynamic granularity, graph adaptation | dynamic topo planning | topo granularity / graph management 参考 | https://arxiv.org/abs/2601.21751 | 直接针对 topo granularity rigidity，与你关心的问题高度一致 |
| 已核实 | 2026 | Let's Reward Step-by-Step: Step-Aware Contrastive Alignment for Vision-Language Navigation in Continuous Environments | 直接命中 | VLN-CE benchmarks | step reward, dense alignment, long-horizon credit assignment | step-aware alignment / reward shaping | 训练范式 / progress credit 参考 | https://arxiv.org/abs/2603.09740 | 对“长时 credit assignment”非常值得关注 |

---

## B. 强相关候选（已重新检索到，但仍需继续筛）

| 状态 | 年份 | 论文 | 类型 | 数据集/基准 | 关键词 | 方法范式 | 作用 | 来源 | 当前判断 |
|---|---:|---|---|---|---|---|---|---|---|
| 已核实 | 2024 | Enhancing Large Language Models with RAG for Visual Language Navigation in Continuous Environments | 强相关 | R2R-CE / RxR-CE | RAG, LLM, retrieval | LLM + retrieval | 外部知识注入路线参考 | https://www.mdpi.com/2079-9292/14/5/909/xml | 更像应用型增强，创新深度可能有限 |
| 已核实 | 2024 | Mind the Error! Detection and Localization of Instruction Errors in Vision-and-Language Navigation | 强相关 | R2R-IE-CE | error detection, robustness | instruction error handling | robustness / benchmark 扩展 | https://github.com/intelligolabs/R2RIE-CE | 不是主 benchmark，但可为 robustness 提供支线 |
| 已核实 | 2025 | GC-VLN: Instruction as Graph Constraints for Training-free Vision-and-Language Navigation | 强相关 | continuous environments | graph constraints, training-free, structure | graph constraint optimization | training-free / graph reasoning 参考 | https://openreview.net/forum?id=mjYKNIRqpy | 对“结构化约束”与“无需再训练”有启发 |

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

### C2. 第二梯队

1. Cross-modal Map Learning for Vision and Language Navigation
2. GridMM
3. Cog-GA
4. Efficient-VLN
5. ETP-R1

### C3. 扩展设定

1. Iterative Vision-and-Language Navigation in Continuous Environments
2. monoVLN
3. MonoDream
4. Mind the Error!

---

## D. 当前缺口

1. 还没有完成 `2023–2026` 全量扫表，特别是 2025–2026 可能还有遗漏。
2. 还没有把直接命中论文逐篇展开成固定粗读模板。
3. `monoVLN / MonoDream / Efficient-VLN / ETP-R1` 当前链接已检到，但仍需要进一步补齐正式发表信息、项目页、代码页。
