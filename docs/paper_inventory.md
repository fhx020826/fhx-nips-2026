# Continuous VLN / VLN-CE 论文总表

## 目的

本表用于维护围绕 continuous VLN / VLN-CE，尤其是 `R2R-CE` / `RxR-CE` 的论文研究地图。

目标不是凑数量，而是支持后续：

- 选题判断
- 方法归纳
- baseline / codebase 侦察
- 实验设计

## 使用规则

1. 所有“最新、具体、易变”信息优先联网核实。
2. 若某条元信息本轮未稳定核实，明确标记为“待核实”。
3. 区分三类状态：
   - `已继承上下文`：来自已有项目讨论，但本轮未完整回填元信息
   - `本轮已联网核实`：标题、时间、链接等已做联网确认
   - `候补`：已进入候选池，但还未完成粗读

## 字段说明

| 字段 | 含义 |
|---|---|
| 状态 | 已继承上下文 / 本轮已联网核实 / 候补 |
| 年份 | 优先写 arXiv 首次提交年份或正式发表年份 |
| 论文 | 标题 |
| 任务关系 | 直接命中 / 强相关 / 可迁移 |
| 基准 | 是否涉及 R2R-CE / RxR-CE / VLN-CE |
| 关键词 | planning / history / reasoning / diffusion 等 |
| 范式 | hierarchical / end-to-end / topo planning / VLM+controller 等 |
| 启发价值 | baseline / high-level backbone / low-level expert / training recipe 等 |
| 链接 | 优先 paper 链接 |
| 备注 | 当前最重要判断 |

---

## A. 直接命中 VLN-CE / R2R-CE / RxR-CE

| 状态 | 年份 | 论文 | 任务关系 | 基准 | 关键词 | 范式 | 启发价值 | 链接 | 备注 |
|---|---:|---|---|---|---|---|---|---|---|
| 已继承上下文 | 2021 | Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments | 直接命中 | R2R-CE / RxR-CE / VLN-CE | task setup, continuous control | task definition | 必要起点 | 待补 | continuous VLN 起点论文 |
| 已继承上下文 | 2022 | Bridging the Gap Between Learning in Discrete and Continuous Environments for Vision-Language Navigation | 直接命中 | R2R-CE / RxR-CE | bridge, waypoint, latent goal | hierarchical bridge | bridge 设计参考 | 待补 | DualVLN 思想重要 |
| 已继承上下文 | 2024 | DAgger Diffusion Navigation: DAgger Boosted Diffusion Policy for Vision-Language Navigation | 直接命中 | R2R-CE / RxR-CE | diffusion, DAgger, control | diffusion policy | P0 baseline / codebase | 待补 | 最接近当前低层动作 expert 侦察对象 |
| 已继承上下文 | 2024 | StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling | 直接命中 | VLN / 连续场景相关 | history, streaming, memory | streaming backbone | history backbone | 待补 | history / memory 强参考 |
| 已继承上下文 | 2024 | Open-Nav: Exploring Zero-Shot Vision-and-Language Navigation in Continuous Environment with Open-Source LLMs | 直接命中 | R2R-CE / RxR-CE | zero-shot, reasoning, progress | VLM reasoning scaffold | reasoning 结构参考 | 待补 | 高层推理 scaffold 有价值 |
| 已继承上下文 | 2024 | NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation | 直接命中 | VLN / 连续导航相关 | video history, planning | VLM planner | high-level backbone | 待补 | video-based history 重要参考 |
| 已继承上下文 | 2024 | ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments | 直接命中 | R2R-CE / RxR-CE | topo map, planning, recovery | topo planning | 强 baseline / codebase | 待补 | topo planning 必须认真对待 |
| 本轮已联网核实 | 2024/2025 | Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments | 直接命中 | R2R-CE / RxR-CE | zero-shot, constraints, sub-instruction, progress | value-map + sub-instruction manager | 零样本 / progress / recovery 参考 | https://www.semanticscholar.org/paper/Constraint-Aware-Zero-Shot-Vision-Language-in-Chen-An/4d27c0905b46d06507ed1701a4baacc6c075be9b | TPAMI 2025，值得补完整粗读 |
| 本轮已联网核实 | 2025 | monoVLN: Bridging the Observation Gap between Monocular and Panoramic Vision and Language Navigation | 直接命中 | R2R-CE / RxR-CE | monocular, active perception, uncertainty | monocular VLN-CE | 传感器设定 / uncertainty 参考 | https://papers.cool/venue/Lu_monoVLN_Bridging_the_Observation_Gap_between_Monocular_and_Panoramic_Vision%40ICCV2025%40CVF | ICCV 2025，偏 monocular 但任务相关 |
| 本轮已联网核实 | 2025 | MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming | 直接命中 | R2R-CE / RxR-CE | monocular, history, latent future | latent supervision | monocular/history 参考 | https://www.sciencestack.ai/paper/2508.02549 | monocular VLN-CE 的新方向 |
| 本轮已联网核实 | 2025 | ETP-R1: Evolving Topological Planning with Reinforcement Fine-tuning for Vision-Language Navigation in Continuous Environments | 直接命中 | VLN-CE | topo planning, RFT, scaling | topo planning + RFT | topo 路线新进展 | https://huggingface.co/papers/2512.20940 | ETPNav 后续演进，需重点跟进 |
| 本轮已联网核实 | 2025 | Efficient-VLN: A Training-Efficient Vision-Language Navigation Model | 直接命中 | R2R-CE / RxR-CE | efficient memory, DAgger, training efficiency | memory + dynamic policy | history / training recipe 参考 | https://papers.cool/arxiv/2512.10310 | 训练效率与 memory 都相关 |
| 本轮已联网核实 | 2024 | Mind the Error! Detection and Localization of Instruction Errors in Vision-and-Language Navigation | 直接命中（扩展设定） | R2R-IE-CE | instruction error, robustness | error detection | robustness / benchmark 参考 | https://github.com/intelligolabs/R2RIE-CE | 扩展 benchmark，不是主线但可作为 robustness 支线 |

---

## B. 强相关 VLN / Embodied Navigation / Foundation Navigation

| 状态 | 年份 | 论文 | 任务关系 | 基准 | 关键词 | 范式 | 启发价值 | 链接 | 备注 |
|---|---:|---|---|---|---|---|---|---|---|
| 已继承上下文 | 2024 | Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation | 强相关 | VLN | slow-fast, dual-system | planner + executor | 系统分层参考 | 待补 | 高层慢系统 + 低层快系统 |
| 已继承上下文 | 2024 | Towards Learning a Generalist Model for Embodied Navigation (NaviLLM) | 强相关 | embodied navigation | generalist, schema instruction | unified navigation model | 多任务 / schema 参考 | 待补 | 不是当前主骨架 |

---

## C. 可迁移方法论文（robotics / VLA / control / memory）

| 状态 | 年份 | 论文 | 任务关系 | 基准 | 关键词 | 范式 | 启发价值 | 链接 | 备注 |
|---|---:|---|---|---|---|---|---|---|---|
| 已继承上下文 | 2023 | Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | 可迁移 | manipulation | diffusion, action chunking | diffusion policy | 低层动作专家参考 | 待补 | 低层连续动作经典参考 |
| 已继承上下文 | 2025 | DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression | 可迁移 | VLA | reasoning injection, bridge | unified VLA | reasoning-to-policy bridge | 待补 | 价值在 bridge，不在简单拼接 |
| 已继承上下文 | 2024 | π₀: A Vision-Language-Action Flow Model for General Robot Control | 可迁移 | VLA / robotics | flow matching, chunked action | flow policy | 低层 flow-matching 备选 | 待补 | 高层 backbone + 低层 flow expert 的范式支撑 |

---

## D. 后续待补优先队列

### D1. 直接命中优先补齐

1. DAgger Diffusion Navigation
2. StreamVLN
3. Open-Nav
4. NaVid
5. ETPNav
6. Constraint-Aware Zero-Shot VLN-CE
7. Efficient-VLN
8. ETP-R1
9. monoVLN
10. MonoDream

### D2. 强相关候选待继续检索

- 2025–2026 的 VLN-CE / monocular VLN-CE / memory-efficient VLN
- 与 `history compression / recursive memory / streaming inference / recovery / obstacle avoidance` 明确相关的工作
- 具身 foundation navigation / VLM planner + controller 方向

### D3. 可迁移候选待继续检索

- action chunking / flow matching / latent goal conditioning
- world-model-like planning for embodied control
- hierarchical planning-control with long-horizon instruction following

---

## 当前缺口

1. 还没有完成 2025–2026 候选池的系统扫全。
2. 目前表中很多“已继承上下文”条目还未补全正式链接和元信息。
3. 还没有把每篇论文展开成固定粗读模板。
