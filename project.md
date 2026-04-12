# 项目理解

## 项目目标

本项目当前的核心目标，不是直接进入方法实现，而是先把 continuous embodied navigation 这条线的研究资产收紧、整理并标准化。具体来说，是围绕 `R2R-CE / RxR-CE / VLN-CE` 主线建立：
- 唯一可信的完整论文总表
- 与总表一一对应的详细粗读卡片
- 基于真实粗读结论动态更新的高质量论文列表

在这套资产稳定之后，再进入 baseline 侦察、codebase reconnaissance 和方法设计。

## 当前项目阶段

当前仍处于“研究地图与粗读资产重建阶段”。

仓库当前真实主线是：
- 论文筛选
- 外网事实核查
- 粗读资产建设
- 高质量论文池逐步筛选

尚未进入正式的模型训练、实验复现或新方法实现阶段。

## 当前核心研究判断

当前最明确的研究判断仍然是：
- continuous VLN 中存在高层语义理解与低层连续控制之间的关键接口缺口

围绕这个判断，项目持续关注的问题包括：
- history / memory
- progress
- hierarchical planning-control
- subgoal / latent bridge
- obstacle avoidance
- deadlock recovery
- closed-loop stability

## 当前论文资产结构

当前论文相关资产已经收敛到三部分：

1. `docs/paper_list_feishu_strict.md`
说明：
- 当前唯一执行总表
- 共 `75` 篇
- 只保留连续具身地面导航主线相关论文

2. `docs/paper_roughreads/`
说明：
- 当前唯一有效的粗读正文目录
- 后续所有新的粗读都只写到这里
- 当前已保留的唯一种子稿为：
  - `003_p3nav.md`

3. `docs/paper_quality_shortlist.md`
说明：
- 当前唯一有效的高质量论文列表
- 不再继承旧版 ranking
- 只根据已经完成的新风格粗读实时更新

## 当前粗读流程

后续固定流程如下：

1. 从 `docs/paper_list_feishu_strict.md` 取论文
2. 做外网事实核查
3. 按 `P^3Nav` 最新稿风格写入 `docs/paper_roughreads/`
4. 完成后判断是否进入 `docs/paper_quality_shortlist.md`

需要特别强调：
- 事实核查必须覆盖 arXiv / publisher / project page / GitHub / model / data 等外部入口
- `sampled subset`、`extra data`、`extra supervision`、`extra sensor`、benchmark 变体等信息都必须显式写出

## 当前代码与环境状态

当前仓库还没有正式引入某个 continuous VLN baseline 代码底座。
现有代码主要是调研辅助脚本，例如：
- `scripts/collect_arxiv_dates.py`
- `scripts/fetch_arxiv_abs_dates.py`
- `scripts/prepare_roughread_queue.py`
- `scripts/proxy_exec.sh`

另外，当前 shell 中 `conda` 仍不可直接使用。如果下一步进入 Python 工具开发或实验代码执行，需要先修复环境初始化。

## 当前优先级

当前第一优先任务是：
- 以新总表为唯一论文池
- 按新风格持续重建粗读资产
- 在粗读过程中逐步筛出真正值得持续投入的高质量论文

## 项目当前定位总结

这个仓库当前首先是：
- continuous embodied navigation 研究地图仓
- 详细粗读资产仓
- 高质量论文筛选仓

只有在这三部分稳定后，才会自然进入 baseline 代码侦察与方法实现阶段。
