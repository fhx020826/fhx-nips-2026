# 当前进展

## 2026-04-12

### 第一批粗读已完成

1. 已按新的唯一执行总表顺序，完成前 5 篇中的 4 篇新增粗读落盘：
   - `docs/paper_roughreads/001_latentpilot.md`
   - `docs/paper_roughreads/002_navtrust.md`
   - `docs/paper_roughreads/004_emergenav.md`
   - `docs/paper_roughreads/005_himemvln.md`
2. 现有 `docs/paper_roughreads/003_p3nav.md` 保持不变，继续作为当前唯一写作风格基准。
3. 本轮粗读过程中，已重新核对第一批论文的关键事实层信息，包括：
   - arXiv v1 日期
   - 项目页 / GitHub 是否真实存在
   - 代码、权重、README、release 状态
   - benchmark 设定与主要结果的可比性边界
4. 已完成第一批对应的高质量论文筛选，并更新：
   - `docs/paper_quality_shortlist.md`
5. 当前 shortlist 已纳入：
   - `LatentPilot`
   - `NavTrust`
   - `P^3Nav`
   - `EmergeNav`
   - `HiMemVLN`

### 本轮新增的判断结论

1. `LatentPilot` 是当前非常值得持续投入的一篇：
   - 训练期 future-privileged supervision 和 inference-time causal policy 的接口设计很强
   - 代码已公开但模型和数据脚本未放出，适合继续做代码侦察
2. `NavTrust` 应作为后续所有 baseline 比较的 benchmark 约束保留：
   - 不能再只看 clean 主榜
   - RGB / depth / instruction corruption 与 mitigation protocol 都很有现实意义
3. `EmergeNav` 的工程生态较弱，但结构判断价值高：
   - `Plan-Solve-Transition`
   - GIPE
   - dual-memory
   - role-separated sensing
4. `HiMemVLN` 对 open-source zero-shot continuous VLN 很关键：
   - `Navigation Amnesia` 问题定义成立
   - `Localer / Globaler` 分工对 memory 主线很有参考价值
   - 仓库已公开，但 README 和 release 仍明显不完整

### 本轮完成

1. 已确认新的论文资产保留原则：
   - 只保留连续具身地面导航主线论文
   - UAV / aerial / drone、纯离散 VLN、视觉提示替代语言指令的变体任务不再进入主执行总表
2. 已保留当前唯一主论文列表：
   - `docs/paper_list_feishu_strict.md`
3. 已确定新的唯一粗读目录：
   - `docs/paper_roughreads/`
4. 已确定新的唯一高质量论文列表：
   - `docs/paper_quality_shortlist.md`
5. `P^3Nav` 的最新粗读结果被作为新风格基准保留，不再重写。

### 结构状态说明

上一轮目录重置已经完成，当前项目已经从“清理旧资产”阶段进入“按新总表正式粗读”阶段。

当前结构目标已经稳定为：
- 只保留一份完整论文总表
- 只保留一个粗读正文目录
- 只保留一份动态维护的高质量论文列表
- 不再恢复旧 batch 索引、旧 roughread 目录和历史候选缓存

### 当前有效资产

1. 完整论文总表：
   - `docs/paper_list_feishu_strict.md`
2. 粗读正文目录：
   - `docs/paper_roughreads/`
3. 高质量论文列表：
   - `docs/paper_quality_shortlist.md`

### 当前有效粗读

1. 当前有效粗读共有 5 篇：
   - `docs/paper_roughreads/001_latentpilot.md`
   - `docs/paper_roughreads/002_navtrust.md`
   - `docs/paper_roughreads/003_p3nav.md`
   - `docs/paper_roughreads/004_emergenav.md`
   - `docs/paper_roughreads/005_himemvln.md`
2. 其中 `003_p3nav.md` 仍作为当前写作风格基准，其余论文已经按这一风格继续扩展。

### 当前高质量论文列表状态

1. 旧版 shortlist 已作废。
2. 新版 shortlist 已建立并开始动态维护。
3. 当前已同步纳入：
   - `LatentPilot`
   - `NavTrust`
   - `P^3Nav`
   - `EmergeNav`
   - `HiMemVLN`
4. 后续每完成一批新的粗读，继续增量更新，不再单独维护旧 shortlist。

### 当前阻塞

1. `conda` 仍不可直接使用。
2. 如果后续要进入脚本开发、自动整理工具或实验代码执行，仍需先修复环境初始化。

### 下一步

1. 继续按主总表顺序推进下一批论文粗读。
2. 下一轮从第 `6-10` 篇开始。
3. 保持当前写作风格，不再回到旧模板化写法。
4. 每批完成后继续同步更新 `docs/paper_quality_shortlist.md` 与 `work.md`。
