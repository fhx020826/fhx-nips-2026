# 项目理解

## 项目目标

本项目目标是在 continuous VLN / VLN-CE 场景下，围绕 Habitat 中的 `R2R-CE` 为主、`RxR-CE` 为辅，建立高质量研究地图、完成结构化论文粗读与代码侦察，并在此基础上筛选出具备顶会潜力的研究方向，最终支撑方法设计与论文产出。

## 当前项目阶段

当前项目仍处于“研究地图与粗读资产建设阶段”，尚未进入正式方法实现和实验复现实装阶段。仓库目前是：
- 文档优先
- 论文调研优先
- baseline / codebase reconnaissance 前置

也就是说，当前真实主线不是训练模型，而是先把：
- 论文事实层信息
- benchmark 可比性
- 复现生态
- 内部高质量 shortlist

建立扎实。

## 当前核心研究判断

当前已经比较明确的核心方法学判断是：
- continuous VLN 中存在高层语义理解与低层连续控制之间的关键接口缺口

围绕这个判断，当前最值得持续跟踪的核心问题包括：
- history / memory
- progress 建模
- hierarchical planning-control
- subgoal / latent bridge
- obstacle avoidance
- deadlock recovery
- closed-loop stability

## 当前论文资产状态

仓库中已经形成以下主要论文资产：
- `docs/paper_list_feishu_strict.md`
  说明：当前唯一执行总表，已按“连续具身地面导航主线”重构，现共 `75` 篇
- `docs/paper_list_new_additions_round2.md`
  说明：相对旧版总表新增纳入的 `25` 篇论文清单，作为下一轮粗读入口
- `docs/paper_quality_shortlist.md`
  说明：内部高质量论文列表，按优先级分层维护
- `docs/paper_roughreads_full/`
  说明：按单论文单文件落盘的详细粗读卡片

截至目前，已完成前 `25` 篇粗读卡片中的主线部分；由于总表口径收紧，以下 `4` 篇已从主线资产中移除并删除正文文件：
- `011_airnav.md`
- `013_indooruav.md`
- `018_soranav.md`
- `025_vpn.md`

当前仍保留并持续维护的详细粗读卡片共 `21` 篇，对应：
- `001` 到 `010`
- `012`
- `014` 到 `017`
- `019` 到 `024`

并已生成四批索引文档：
- `docs/paper_roughread_full_list_batch1.md`
- `docs/paper_roughread_full_list_batch2.md`
- `docs/paper_roughread_full_list_batch3.md`
- `docs/paper_roughread_full_list_batch4.md`

## 当前粗读流程

当前已经固定下来的粗读流程是：
1. 从 `docs/paper_list_feishu_strict.md` 按顺序取下一批论文
2. 逐篇进行外网事实核查
3. 生成可直接复制到飞书的详细 Markdown 粗读卡片
4. 同步检查是否应纳入 `docs/paper_quality_shortlist.md`
5. 如果已在 shortlist 中，则同步复核其定位与描述是否仍准确

特别注意：
- GitHub 仓库、README、项目页、模型页、publisher 页面都属于事实核查范围
- `sampled subset`、`pre-exploration`、额外传感器、扩展 benchmark 等限制必须显式标注

## 当前仓库代码状态

当前仓库还没有正式引入某个 continuous VLN baseline 代码底座。现有代码主要是调研辅助脚本，例如：
- `scripts/collect_arxiv_dates.py`
- `scripts/fetch_arxiv_abs_dates.py`
- `scripts/prepare_roughread_queue.py`
- `scripts/proxy_exec.sh`

因此 `project.md` 当前更多反映的是“研究基础设施与文档状态”，而不是模型实现结构。

## 当前优先级

当前默认第一优先任务是：
- 先按新口径维护 `75` 篇主表与新增论文清单
- 优先从 `docs/paper_list_new_additions_round2.md` 开始补新一轮粗读
- 每一批同步核查 shortlist
- 在粗读推进中逐渐明确最值得优先侦察的代码底座

在代码侦察优先级上，目前仍然优先关注：
- `ETPNav`
- `Dynamic Topology Awareness`
- `SeqWalker`
- 后续的 `StreamVLN`
- 后续的 `DAgger Diffusion Navigation`

## 当前风险与边界

1. 当前 shell 中 `conda` 命令尚未直接可用，因此如果下一步要进入 Python 开发或运行，需要先解决环境初始化问题。
2. 仓库内已有较多临时论文缓存，后续需要持续评估清理。
3. 当前主产物是文档，不应过早把仓库做成杂乱的脚本集合。

## 项目当前定位总结

这个仓库当前不是“训练代码仓”，而是：
- continuous VLN 研究地图仓
- 结构化粗读资产仓
- shortlist 与 baseline 侦察的前置工作区

后续如果真正引入 baseline 代码或实验实现，再同步更新本文件，使其反映真实代码结构与方法进度。
