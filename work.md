# 当前进展

## 2026-04-12

### 已完成内容

1. 已完成 `001-015` 共 15 篇论文的当前新风格粗读落盘，当前有效文件为：
   - `docs/paper_roughreads/001_latentpilot.md`
   - `docs/paper_roughreads/002_navtrust.md`
   - `docs/paper_roughreads/003_p3nav.md`
   - `docs/paper_roughreads/004_emergenav.md`
   - `docs/paper_roughreads/005_himemvln.md`
   - `docs/paper_roughreads/006_correctnav.md`
   - `docs/paper_roughreads/007_imaginav.md`
   - `docs/paper_roughreads/008_saca.md`
   - `docs/paper_roughreads/009_span_nav.md`
   - `docs/paper_roughreads/010_history_conditioned_token_pruning.md`
2. `003_p3nav.md` 继续作为当前唯一写作风格基准，后续粗读沿这一风格继续扩展。
3. 本轮对 `006-010` 做了外部事实核查，核查内容包括：
   - arXiv / venue / DOI / OpenAlex
   - 项目页、GitHub、模型页、数据页
   - benchmark 设置与主结果
   - 是否有真实机器人或跨平台实验
4. 已重新核查并更新：
   - `docs/paper_quality_shortlist.md`
5. 已将旧版 shortlist 判断全部作废，改为严格标准重筛。
6. 已继续完成 `011-015` 的粗读准备所需事实核查与正文落盘。

### 本轮新增的研究判断

1. `CorrectNav` 是很强的后训练与纠错机制论文：
   - `Self-correction Flywheel` 不是普通 hard example mining，而是持续的 error-mining 闭环
   - perception correction 和 action correction 的分拆很有启发
   - 但当前无代码、模型、数据入口，不能纳入严格 shortlist
2. `ImagiNav` 的价值主要在接口创新：
   - `subgoal -> imagined future video -> inverse dynamics`
   - 用开放世界 human egocentric video 替代机器人 demonstration 的方向非常值得记
   - 但当前主 benchmark 偏 `VLN-PE`，且代码、数据都未放出
3. `SACA` 是当前 batch 里最值得记的训练范式论文之一：
   - `PGSA auditor`
   - `Repair Resampling`
   - `All-Failure Rescue`
   - 从失败轨迹中提取 step-level dense supervision 的思路很强
   - 但当前仓库基本为空壳，且无正式录用与引用积累
4. `SPAN-Nav` 是空间先验方向上很强的一篇：
   - `occupancy prior -> single spatial token -> spatial CoT`
   - 跨任务实验非常完整
   - 但当前仍无代码、模型、数据释放，暂不入 shortlist
5. `History-Conditioned Spatio-Temporal Visual Token Pruning...` 更适合作为部署效率参考：
   - 重点是 current/history 分离的 pruning 设计
   - training-free、plug-and-play、真实 Go2 部署都很有价值
   - 但它是系统层优化，不是主线方法候选

### 新增的研究判断（011-015）

1. `PROSPECT` 是这一批里最值得记的 streaming spatial-predictive VLA 论文之一：
   - `SigLIP + CUT3R` 的 2D/3D 双流融合很清楚
   - `stream query tokens` 在 frozen teacher latent space 里做 2D/3D 下一步预测
   - prediction branch 只在训练时存在，推理时零额外开销
   - 中长程提升和 real-robot lighting robustness 很有说服力
   - 但当前只有“代码即将发布”的表述，没有实际项目与仓库
2. `Enhancing VLN with Multimodal Event Knowledge...` 的最大价值在数据和记忆接口：
   - 构建了 `YE-KG`，规模为 `86k+` 节点、`83k+` 边
   - 从真实 indoor tour video 中抽取 `semantic-action-effect` 事件
   - `STE-VLN` 用 coarse-to-fine retrieval 把 event/scene knowledge 接回导航器
   - 项目页确认数据可下载，但代码仍写着 `coming soon`
3. `One Agent to Guide Them All` 的核心贡献不是更强的 MLLM，而是 `explicit world representation`：
   - `TSDF + topo graph` 组成 interactive metric world representation
   - decouple spatial modeling from semantic reasoning
   - 真实机器人覆盖 `TurtleBot 4` 和自制无人机，跨 embodiment 证据很强
   - 但主结果里 `RxR-CE` 使用 sampled subset，需要注意和 full-split 工作的可比性
4. `BudVLN` 非常值得记住它提出的 `Instruction-State Misalignment`：
   - DAgger-style 从错态直接学 recovery action， supervision 自己就可能脏
   - `greedy probe -> 动态路由 -> GRPO / retrospective rectification`
   - 和 DAgger 相比，结果更好且训练时间更短（`27h vs 114h`）
   - 目前仍无项目、代码、模型页
5. `DGNav` 是当前 batch 里复现生态最完整的工作：
   - GitHub 仓库公开，训练/评测脚本完整
   - waypoint predictor 与部分 pretrain 权重已给下载链接
   - `Scene-Aware Adaptive Strategy + Dynamic Graph Transformer` 的方法主线清晰
   - 但它仍是 arXiv，引用为 `0`，且最终 fine-tuned weight / processed data 未完全公开

### 高质量论文列表的最新状态

1. 这轮按更严格标准重新筛选后，`docs/paper_quality_shortlist.md` 当前为空。
2. 清空的原因不是论文不值得读，而是已完成粗读的 `001-015` 还没有论文同时满足以下全部条件：
   - 相对较新但已有明显引用积累
   - 顶会 / 顶刊正式录用
   - 主实验充分
   - 代码、模型、数据整体开放
3. `CorrectNav` 虽然已经 `AAAI 2026` 录用且实验扎实，但由于当前没有代码 / 模型 / 数据入口，且引用为 `0`，仍未通过严格筛选。
4. `001-005` 之前进入 shortlist 的旧判断已全部作废，不再沿用。
5. `011-015` 中目前最接近 shortlist 门槛的是：
   - `012 STE-VLN`：数据已开放，但代码未开放；
   - `015 DGNav`：代码和部分权重开放，但无正式录用、无引用积累。

### 当前有效资产

1. 主论文总表：
   - `docs/paper_list_feishu_strict.md`
2. 粗读正文目录：
   - `docs/paper_roughreads/`
3. 严格高质量论文列表：
   - `docs/paper_quality_shortlist.md`
4. 当前已完成粗读文件：
   - `docs/paper_roughreads/001_latentpilot.md`
   - `docs/paper_roughreads/002_navtrust.md`
   - `docs/paper_roughreads/003_p3nav.md`
   - `docs/paper_roughreads/004_emergenav.md`
   - `docs/paper_roughreads/005_himemvln.md`
   - `docs/paper_roughreads/006_correctnav.md`
   - `docs/paper_roughreads/007_imaginav.md`
   - `docs/paper_roughreads/008_saca.md`
   - `docs/paper_roughreads/009_span_nav.md`
   - `docs/paper_roughreads/010_history_conditioned_token_pruning.md`
   - `docs/paper_roughreads/011_prospect.md`
   - `docs/paper_roughreads/012_ste_vln.md`
   - `docs/paper_roughreads/013_gta_explicit_world_representation.md`
   - `docs/paper_roughreads/014_budvln.md`
   - `docs/paper_roughreads/015_dgnav.md`

### 环境与执行说明

1. 本轮外网检索通过当前 shell 环境中的代理变量完成，已确认存在：
   - `HTTP_PROXY`
   - `HTTPS_PROXY`
   - `ALL_PROXY`
2. 因此后续终端中的 `curl / GitHub API / OpenAlex` 请求会默认走代理，不需要额外手动包装。
3. 本轮没有进行代码开发、训练或推理执行，因此未涉及新的 conda 环境创建与实验脚本运行。

### 下一步

1. 继续按总表顺序推进 `016-020` 的粗读。
2. 保持当前人类研究笔记式写法，不回到死板模板。
3. 继续按严格标准维护 shortlist，不为了“先有内容”而放宽要求。
4. 在后续批次中重点关注更有希望满足 strict shortlist 条件的较早、已正式发表且开源完整的论文。
