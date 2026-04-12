# 当前进展

## 2026-04-12

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

### 本轮结构重置目标

这轮不是继续粗读，而是先把文档结构收干净，避免旧资产继续污染后续流程。

要达到的状态是：
- 只保留一份完整论文总表
- 只保留一个粗读正文目录
- 只保留一份动态维护的高质量论文列表
- 删除旧 batch 索引、旧 roughread 目录和历史候选缓存

### 当前有效资产

1. 完整论文总表：
   - `docs/paper_list_feishu_strict.md`
2. 粗读正文目录：
   - `docs/paper_roughreads/`
3. 高质量论文列表：
   - `docs/paper_quality_shortlist.md`

### 当前有效粗读

1. 当前新目录下保留的唯一有效粗读是：
   - `docs/paper_roughreads/003_p3nav.md`
2. 这篇稿子将作为后续所有论文粗读的风格基准。

### 当前高质量论文列表状态

1. 旧版 shortlist 已作废。
2. 新版 shortlist 已重置。
3. 当前仅同步纳入：
   - `P^3Nav`
4. 后续每完成一批新的粗读，再动态决定是否纳入更多论文。

### 当前阻塞

1. `conda` 仍不可直接使用。
2. 如果后续要进入脚本开发、自动整理工具或实验代码执行，仍需先修复环境初始化。

### 下一步

1. 确认这轮目录和文档清理后的结构没有问题。
2. 然后从新总表继续正式粗读。
3. 粗读时直接写入 `docs/paper_roughreads/`，不再恢复旧目录和旧 batch 文档。
4. 每完成一批粗读，就同步更新 `docs/paper_quality_shortlist.md`。
