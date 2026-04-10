# 项目理解

## 项目目标

本项目目标是在 continuous VLN / VLN-CE 场景下，围绕 Habitat 中的 R2R-CE 为主、RxR-CE 为辅，找到具备顶会潜力的研究方向，并最终产出一篇有清晰问题定义、方法动机、实验逻辑和创新点的论文。

## 当前共识

1. 旧的 `NaviLLM + diffusion policy` 朴素端到端路线已经降级为失败的早期探索，不再作为主线。
2. 当前最重要的不是先押注方法，而是先构建高质量研究地图。
3. 当前核心方法学判断是：continuous VLN 中，高层语义/历史/进度理解与低层连续控制之间存在关键接口缺口。
4. 后续值得重点关注的问题包括：
   - history / memory
   - progress 建模
   - hierarchical planning-control
   - subgoal / latent bridge
   - obstacle avoidance
   - deadlock recovery
   - closed-loop stability

## 已有重点论文共识

当前已明确进入项目上下文的代表论文包括：

- Beyond the Nav-Graph
- Bridging the Gap Between Learning in Discrete and Continuous Environments for Vision-Language Navigation
- DAgger Diffusion Navigation
- Diffusion Policy
- Ground Slow, Move Fast
- StreamVLN
- DiffusionVLA
- pi0
- Open-Nav
- NaVid
- NaviLLM
- ETPNav

这些论文不是“待从零开始读”，而是已有基础理解，后续应在其上继续扩展和比较。

## 当前阶段任务

当前默认第一优先任务：

- 围绕 continuous VLN / VLN-CE，尤其是 R2R-CE / RxR-CE，建立约 50 篇论文的结构化总表。
- 时间重点：2023–2026，尤其是 2025–2026。
- 最终目标不是凑列表，而是形成支持选题决策的研究地图。

## 当前工程策略

1. 优先建立干净隔离的项目目录和环境。
2. 优先做 baseline reconnaissance / codebase viability / interface mapping。
3. 后续优先侦察对象：
   - P0: DAgger Diffusion Navigation
   - P1: StreamVLN
   - P2: Uni-NaVid
   - ETPNav: 强 baseline / codebase 候选

## 当前仓库状态

当前仓库是新建隔离工作区，尚未引入真实代码底座。`project.md` 后续需要随着真实代码结构和调研结论持续更新，而不是只追加新内容。
