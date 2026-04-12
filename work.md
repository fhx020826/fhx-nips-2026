# 当前进展

## 2026-04-12

### 已完成内容

1. 已完成 `001-010` 共 10 篇论文的当前新风格粗读落盘，当前有效文件为：
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

### 高质量论文列表的最新状态

1. 这轮按更严格标准重新筛选后，`docs/paper_quality_shortlist.md` 当前为空。
2. 清空的原因不是论文不值得读，而是已完成粗读的 `001-010` 还没有论文同时满足以下全部条件：
   - 相对较新但已有明显引用积累
   - 顶会 / 顶刊正式录用
   - 主实验充分
   - 代码、模型、数据整体开放
3. `CorrectNav` 虽然已经 `AAAI 2026` 录用且实验扎实，但由于当前没有代码 / 模型 / 数据入口，且引用为 `0`，仍未通过严格筛选。
4. `001-005` 之前进入 shortlist 的旧判断已全部作废，不再沿用。

### 当前有效资产

1. 主论文总表：
   - `docs/paper_list_feishu_strict.md`
2. 粗读正文目录：
   - `docs/paper_roughreads/`
3. 严格高质量论文列表：
   - `docs/paper_quality_shortlist.md`

### 环境与执行说明

1. 本轮外网检索通过当前 shell 环境中的代理变量完成，已确认存在：
   - `HTTP_PROXY`
   - `HTTPS_PROXY`
   - `ALL_PROXY`
2. 因此后续终端中的 `curl / GitHub API / OpenAlex` 请求会默认走代理，不需要额外手动包装。
3. 本轮没有进行代码开发、训练或推理执行，因此未涉及新的 conda 环境创建与实验脚本运行。

### 下一步

1. 继续按总表顺序推进 `011-015` 的粗读。
2. 保持当前人类研究笔记式写法，不回到死板模板。
3. 继续按严格标准维护 shortlist，不为了“先有内容”而放宽要求。
4. 在后续批次中重点关注更有希望满足 strict shortlist 条件的较早、已正式发表且开源完整的论文。
