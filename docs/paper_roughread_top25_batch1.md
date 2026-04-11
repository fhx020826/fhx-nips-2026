# Top 25 粗读卡片（Batch 1）

说明：

- 本文档用于把 strict 核心集 / Top 25 从“列表层”推进到“论文卡片层”。
- 当前只做第一批最影响 baseline / codebase reconnaissance 的 5 篇。
- 只记录已联网核实的信息；带“判断”的部分会明确写成“当前判断”。
- 默认关注：
  - 是否直接可比 `R2R-CE / RxR-CE`
  - 是否依赖额外数据 / 额外监督 / 额外传感器
  - 是否已有可复现代码 / checkpoint / 项目页
  - 是否值得纳入后续 baseline / codebase 侦察优先队列

---

## 1. ETPNav

### 基本信息

- 论文：ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments
- arXiv v1：2023-04-06
- 代码仓库：`MarSaKi/ETPNav`
- 仓库声明状态：官方 repo 标注为 `[TPAMI 2024]`
- 相关链接：
  - arXiv: https://arxiv.org/abs/2304.03047
  - code: https://github.com/MarSaKi/ETPNav

### 任务身份与 benchmark

- 直接命中 continuous VLN / VLN-CE。
- 论文摘要明确声称主实验覆盖 `R2R-CE` 与 `RxR-CE`。
- repo 提供 `run_r2r/` 与 `run_rxr/` 训练/评测入口。

### 方法骨架

- 在线拓扑建图。
- 高层 cross-modal planner 负责长程规划。
- 低层 obstacle-avoiding controller + tryout heuristic 负责连续控制与脱困。
- 本质上是很典型的“高层规划 / 低层控制”分解式 continuous VLN baseline。

### 复现生态

- 代码已公开，且 repo TODO 显示：
  - R2R-CE fine-tuning code 已放出
  - RxR-CE fine-tuning code 已放出
  - pretraining code 已放出
  - checkpoint 已放出
- 环境较旧：
  - Python 3.6
  - habitat-sim / habitat-lab `v0.1.7`
  - `torch 1.9.1 + cu111`
- 依赖额外资源：
  - waypoint predictor 权重
  - processed data / pretrained / finetuned weights
  - repo 明确写到 pretraining data 使用与 `DUET` 相同的数据

### 可比性与注意点

- 是当前最强的“拓扑规划主线 baseline / codebase 候选”之一。
- 但它不是“轻量纯 benchmark 复现”：
  - 需要额外 waypoint predictor
  - 需要预训练数据与特征
  - 依赖较旧 Habitat 栈
- 当前判断：
  - 适合作为 P0 级 baseline reconnaissance 对象
  - 更适合学结构与工程接口，不适合第一步就原样全量重训

### 对本项目最有价值的点

- 它直接把你当前最关心的接口问题拆开了：
  - 高层语义 / 历史 / 规划
  - 低层连续控制 / obstacle avoidance / recovery
- 后续凡是做 hierarchical planning-control、subgoal bridge、deadlock recovery，都绕不过它。

---

## 2. RxR-Habitat 2022 冠军方案

### 基本信息

- 论文：1st Place Solutions for RxR-Habitat Vision-and-Language Navigation Competition (CVPR 2022)
- arXiv v1：2022-06-23
- 相关链接：
  - arXiv: https://arxiv.org/abs/2206.11610
  - challenge page: https://ai.google.com/research/rxr/habitat
  - 官方 starter branch: https://github.com/jacobkrantz/VLN-CE/tree/rxr-habitat-challenge

### 任务身份与 benchmark

- 这是 `RxR-Habitat` continuous challenge 的冠军技术报告，不是通用 `R2R-CE + RxR-CE` 双 benchmark 论文。
- challenge 官方页明确了标准配置：
  - `480x640 RGBD`
  - `30° turn`
  - `30° look up / down`
  - `0.25m` step size
- 结果汇报在 `RxR Test-Challenge split` 上。

### 方法骨架

- 模块化 plan-and-control：
  - Candidate Waypoints Predictor (CWP)
  - History-enhanced planner
  - Tryout controller
- 额外增强：
  - synthetic pretraining
  - environment-level augmentation
  - snapshot ensemble

### 复现生态

- 已确认有 challenge 官方 starter code，但未检索到这篇技术报告单独的官方代码仓。
- 当前更合理的判断是：
  - 它的工程血缘在 `VLN-CE` / `rxr-habitat-challenge` 分支
  - 后续公开工程实现更像是被 `ETPNav` 体系吸收并系统化

### 可比性与注意点

- 对 `RxR-Habitat` challenge 非常关键。
- 但它不是最理想的“统一 baseline”：
  - 任务聚焦 `RxR-Habitat` challenge
  - 使用较强工程 recipe 与 ensemble
  - 更像 challenge system report，而不是简洁学术 baseline
- 当前判断：
  - 非常值得读清楚其 planner / tryout / history 设计
  - 但 baseline/codebase 侦察时应优先落到 `ETPNav` 代码仓，而不是停留在 report

### 对本项目最有价值的点

- 它把 continuous VLN 中最实用的一套工程分解讲得很清楚：
  - waypoint 缩减动作空间
  - history 追踪进度
  - tryout 负责避障与脱困
- 这套结构与当前你的方法学判断高度一致。

---

## 3. CA-Nav

### 基本信息

- 论文：Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments
- arXiv v1：2024-12-13
- 代码仓库：`Chenkehan21/CA-Nav-code`
- 仓库声明状态：repo 中给出 `TPAMI 2025` citation
- 相关链接：
  - arXiv: https://arxiv.org/abs/2412.10137
  - project: https://chenkehan21.github.io/CA-Nav-project/
  - code: https://github.com/Chenkehan21/CA-Nav-code

### 任务身份与 benchmark

- 直接命中 zero-shot continuous VLN。
- 摘要与项目页都明确主实验覆盖 `R2R-CE` 与 `RxR-CE`。
- 还展示了 real-world robot deployment。

### 方法骨架

- 把 zero-shot VLN-CE 重写成 sequential sub-instruction completion。
- 两个核心模块：
  - Constraint-aware Sub-instruction Manager (CSM)
  - Constraint-aware Value Mapper (CVM)
- CVM 基于当前约束和观测生成 value map，再用 superpixel clustering 提升稳定性。

### 复现生态

- 代码、项目页、真实机器人演示都已公开。
- 但它的外部依赖明显比普通 baseline 重：
  - BLIP2-ITM
  - BLIP2-VQA
  - Grounded-SAM
  - LLM replies
- 环境同样偏老：
  - Python 3.8
  - habitat `v0.1.7`
  - `torch 1.10.0 + cu111`
- repo 还要求手改 Grounded-SAM 的 `phrases2classes` 逻辑。

### 可比性与注意点

- 这是高价值方法参考，但不是“轻量一键复现 baseline”。
- 如果后续目标是：
  - progress 建模
  - subgoal / latent bridge
  - zero-shot scaffold
  - real-world transfer
  那它非常值得精读。
- 当前判断：
  - 应列入“高层结构参考”的第一梯队
  - 但不适合当作第一个落地 baseline codebase

### 对本项目最有价值的点

- 它直接把 `progress / sub-instruction switching / constraint tracking` 做成了方法核心，而不是附属模块。
- 这和你当前判断中的“高层语义 / 历史 / 进度 到低层控制之间的接口缺口”是正面对应的。

---

## 4. DAgger Diffusion Navigation / DifNav

### 基本信息

- 论文：DAgger Diffusion Navigation: DAgger Boosted Diffusion Policy for Vision-Language Navigation
- arXiv v1：2025-08-13
- 代码仓库：`Tokishx/DifNav`
- 相关链接：
  - arXiv: https://arxiv.org/abs/2508.09444
  - code: https://github.com/Tokishx/DifNav

### 任务身份与 benchmark

- 直接命中 continuous VLN。
- 论文摘要明确是 `VLN-CE` end-to-end diffusion policy。
- 目前公开代码仓的目录与说明里，只明确给出 `R2R_VLNCE_v1-2_preprocessed_BERTidx` 和 `run_r2r/main.bash`。
- 当前未看到同等清晰的 `RxR-CE` 公开训练/评测入口。

### 方法骨架

- 把传统两阶段：
  - waypoint generation
  - planner
  合并成单一 diffusion policy。
- 用 DAgger 做在线数据聚合，缓解 compounding error。
- 强调直接在连续动作空间上建模 multi-modal action distribution。

### 复现生态

- repo 目前只完成：
  - evaluation code
  - checkpoints
- repo TODO 仍未完成：
  - online data augmentation code
  - training data and code
- README 明确依赖：
  - Habitat
  - Matterport3D
  - ETPNav
  - NoMaD

### 可比性与注意点

- 它是当前最贴近“低层连续控制主线”的 direct-hit 新工作之一。
- 但从公开生态看，当前更像“半开放复现状态”：
  - 有推理/评测
  - 没完整训练闭环
  - 还继承上游 ETPNav / NoMaD 依赖
- 当前判断：
  - 非常值得做 paper-level 与 interface-level reconnaissance
  - 但目前不该把它当作最稳定的首个复现底座

### 对本项目最有价值的点

- 它正面回答了你之前那条失败主线遗留的问题：
  - diffusion 在 continuous VLN 里到底能不能不依赖 waypoint 两阶段框架
- 这篇应该被当作“低层动作专家路线”的关键对照组，而不是默认主线。

---

## 5. StreamVLN

### 基本信息

- 论文：StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling
- arXiv v1：2025-07-07
- 代码仓库：`OpenRobotLab/StreamVLN`
- repo 声明状态：README 标注 `[ICRA 2026]`
- 相关链接：
  - arXiv: https://arxiv.org/abs/2507.05240
  - project: https://streamvln.github.io/
  - code: https://github.com/OpenRobotLab/StreamVLN

### 任务身份与 benchmark

- 直接命中 continuous VLN。
- 项目页明确主 benchmark 是 `R2R-CE` 与 `RxR-CE`。
- 还包含 real-world deployment 到 Unitree Go2 机器狗。

### 方法骨架

- 基于 `LLaVA-Video` 的 streaming VLN。
- 核心是 slow-fast context modeling：
  - fast-streaming dialogue context
  - slow-updating memory via token pruning
- 强调 bounded context size、KV cache reuse、低时延。

### 复现生态

- 代码、项目页、数据入口、checkpoint、slurm 脚本都比较完整。
- 但它不是纯 benchmark 内闭环：
  - navigation oracle clips 450K
  - DAgger 样本 240K
  - 额外 ScaleVLN subset
  - 额外 LLaVA-Video-178K / ScanQA / MMC4
- 环境较新：
  - Python 3.9
  - habitat-sim / habitat-lab `v0.2.4`
  - `torch 2.1.2`

### 可比性与注意点

- 这是非常值得重点跟踪的新主线，但 apples-to-apples 可比性要单独标记。
- 原因：
  - 它不是“只吃 VLN-CE 标准训练集”的方法
  - 使用了大量额外导航和通用多模态数据
  - 目标本身也更偏 streaming / deployment-ready VLN
- 当前判断：
  - 它适合做 history / memory / streaming inference 的结构参考
  - 不适合直接当作“纯 benchmark baseline”来和 ETPNav 一对一比较

### 对本项目最有价值的点

- 它非常直接地对应你当前最关心的 `history / memory / closed-loop stability`。
- 如果后面要做“高层记忆压缩 + 低层连续执行”的接口设计，这篇是必读新作。

---

## 当前阶段结论

### 更适合优先做 codebase reconnaissance 的

1. `ETPNav`
2. `VLN-CE / rxr-habitat-challenge` 官方 starter

### 更适合优先做结构借鉴而不是首个复现底座的

1. `CA-Nav`
2. `StreamVLN`
3. `DifNav`

### 当前最重要的工程判断

1. `ETPNav` 仍然是当前最稳的 continuous VLN 结构基线。
2. `RxR-Habitat 2022` 冠军报告更像 `ETPNav` 的前身工程 recipe。
3. `CA-Nav` 证明 progress / constraint / sub-instruction bridge 是强主线。
4. `DifNav` 对“diffusion 是否能真正替代 waypoint 两阶段”很关键，但公开训练生态还不成熟。
5. `StreamVLN` 是 history / streaming / deployment 路线的高价值新主线，但要和标准 benchmark baseline 分开比较。

---

## 下一步建议

1. 第二批继续补：
   - `Ground Slow, Move Fast`
   - `NavForesee`
   - `NaVid`
   - `DREAMWALKER`
   - `Open-Nav`
2. 然后单独整理一页 `baseline / codebase reconnaissance`，只面向：
   - 仓库是否可跑
   - 依赖栈是否过旧
   - 数据/权重是否可得
   - 是否适合本项目做最小可验证起点
