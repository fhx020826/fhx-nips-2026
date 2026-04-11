# 会话日志

## 2026-04-10

- 创建项目目录 `/home/hxfeng/fhx-nips-2026`
- 初始化 Git 仓库并添加 `origin`
- 创建基础目录结构
- 读取并确认代理函数定义
- 验证 Clash 正在运行
- 验证 GitHub 可通过代理访问
- 首次 `conda create` 因未走代理而中断
- 已验证 `fhx-nips-2026` 环境可正常运行 Python 3.10.20
- 新增 `scripts/proxy_exec.sh` 统一代理执行入口
- 新增 `docs/hpc_handbook.md`，整理 HPC 关键命令、注意事项和 FAQ
- 更新 `user.md`，明确当前是 Windows 到 Linux HPC 的远程开发模式
- 新建 `docs/paper_inventory.md`
- 第一批新增 VLN-CE / monocular VLN / topo-RFT / efficient VLN 论文已登记入总表
- 按用户要求移除“继承上下文”式写法，改为纯重新检索版论文总表
- 新增 2026 方向：dynamic topology 与 step-aware reward shaping
- 新增 `docs/paper_list_feishu.md` 作为飞书可直接粘贴列表
- 补回 DualVLN 与 benchmark/setting 扩展条目，当前飞书列表扩至 31 条
- 继续补回 Open-Nav / StreamVLN / DifNav / RoomTour3D / NaviLLM，当前飞书列表扩至 34 条
- 新增 Sim-2-Sim / RxR-Habitat 竞赛方案 / graph env representation / CLASH，当前飞书列表扩至 40 条
- 新增 R2R / RxR / Habitat / Habitat 2.0 血缘线论文，当前飞书列表扩至 46 条
- 新增大批 VLN 方法演进链相关论文，当前飞书列表扩至 77 条
- 继续补 benchmark / survey / graph / volumetric 等相关工作，当前飞书列表扩至 102 条
- 新增 `paper_list_feishu_strict.md` 和正式排序版 `paper_quality_shortlist.md`
- 对 strict 列表做边界清洗，只保留“continuous VLN 是主任务身份”的论文
- 新增 `scripts/collect_arxiv_dates.py` 与 `scripts/fetch_arxiv_abs_dates.py`
- 已逐篇核对 strict 核心集的 arXiv 首发日期并做逐日倒序重排
- strict 飞书终版收敛为 39 篇
- 内部高质量 shortlist 已改写为飞书可直接粘贴的 Top 25 优先级表
