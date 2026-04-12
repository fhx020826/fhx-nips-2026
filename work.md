# 当前进展

## 2026-04-12

### 本轮真实状态

1. 项目工作区持续固定在：
   - `/home/hxfeng/fhx-nips-2026`
2. Git 远程仍已正确关联：
   - `origin = https://github.com/fhx020826/fhx-nips-2026.git`
3. 论文执行顺序仍以：
   - `docs/paper_list_feishu_strict.md`
   为准
4. 单论文详细粗读持续落盘在：
   - `docs/paper_roughreads_full/`
5. 内部高质量列表持续维护在：
   - `docs/paper_quality_shortlist.md`
6. 本轮额外新增了“新版风格预览稿”工作流，用于在不覆盖旧稿的前提下先验证粗读写法是否符合当前要求。

### 已完成的关键资产

1. 已完成第 `1` 到第 `25` 篇单论文详细粗读卡片。
2. 已完成四批索引文档：
   - `docs/paper_roughread_full_list_batch1.md`
   - `docs/paper_roughread_full_list_batch2.md`
   - `docs/paper_roughread_full_list_batch3.md`
   - `docs/paper_roughread_full_list_batch4.md`
3. 本轮新增完成第 `16` 到第 `25` 篇：
   - `016_groundslow.md`
   - `017_navforesee.md`
   - `018_soranav.md`
   - `019_lavira.md`
   - `020_janusvln.md`
   - `021_vlnzero.md`
   - `022_gcvln.md`
   - `023_difnav.md`
   - `024_monodream.md`
   - `025_vpn.md`
4. `user.md` 中已经固定“每批粗读都要同步核查 shortlist 与外网事实层”的规则。
5. `coding.md` 已建立并作为后续代码规范文档保留。
6. 已确认并清理本轮临时目录：
   - `tmp/batch4_html/`
   - `tmp/batch4_pdf/`
7. 已启动第 `1` 篇论文 `P^3Nav` 的新版粗读预览重写，旧稿不覆盖，改为单独预览文件验证写法。
8. 已按用户新要求将第 `1` 篇 `P^3Nav` 正式稿直接重写并覆盖到：
   - `docs/paper_roughreads_full/001_p3nav.md`
9. 已完成主论文池的一轮重新筛查与扩充：
   - 将总表从“宽口径 continuous VLN 相关完整版”收紧为“连续具身地面导航主线”
   - 从旧版 `61` 篇总表中剔除 `11` 篇不再相关的论文
   - 新增补入 `25` 篇论文
   - 重构后的主表现为 `75` 篇
10. 已新增：
   - `docs/paper_list_new_additions_round2.md`
   用于承接下一轮新增论文粗读
11. 已删除不再属于主线的粗读正文：
   - `docs/paper_roughreads_full/011_airnav.md`
   - `docs/paper_roughreads_full/013_indooruav.md`
   - `docs/paper_roughreads_full/018_soranav.md`
   - `docs/paper_roughreads_full/025_vpn.md`
12. 已同步更新：
   - `docs/paper_quality_shortlist.md`
   - `docs/paper_roughread_full_list_batch3.md`
   - `docs/paper_roughread_full_list_batch4.md`
   - `project.md`
   - `user.md`

### 本轮新增的写作约束更新

1. 粗读仍需覆盖模板中的核心信息，但不再追求机械化模板复刻。
2. 成稿要保留飞书友好、结构清楚、证据可追溯的特点，同时根据不同论文的方法重点和实验重点调整组织方式。
3. 要减少过于生硬的“是否”字段，改为更自然的研究判断、可比性判断和复现判断。
4. 重点内容允许使用分点增强可读性，但不强制把所有部分都写成清单。
5. 用户进一步明确：新的粗读结果要更像“人类写的研究笔记”，强调高信息密度、重点明确、详略得当和独立分析，而不是模板化判断题。
6. 标题与小节命名也要更自然，减少“模板腔”，同时保持层级合理。

### 本轮 batch 4 已完成的事实校正

1. `Ground Slow, Move Fast`：
   - 已核到官方项目页、官方代码、Hugging Face 模型与数据
   - shortlist 中的“当前形态”已从单纯 `arXiv` 修正为更完整的资源状态
2. `NavForesee`：
   - 已核到 `arXiv v1 = 2025-12-01`
   - 当前仍未核到官方代码 / 项目页 / 模型页
3. `SoraNav`：
   - 已确认当前仍无正式公开代码仓
   - 更适合作为 UAV reasoning / deployment 子线参考
4. `LaViRA`：
   - 已明确其 simulator 结果来自 `VLN-CE val-unseen 100-episode subset`
   - 不能误记为标准完整 split 主榜结果
5. `JanusVLN`：
   - 已核到项目页、官方代码、ModelScope 权重与数据入口
   - 已确认 `Base / Extra` 数据路线需要分开理解
6. `VLN-Zero`：
   - 已确认官方仓库就是 `VLN-Zero/vln-zero.github.io`
   - README 明确包含可运行说明并依赖 `OPENAI_API_KEY`
   - 更适合作为 zero-shot deployment 参考，不应与训练型主 baseline 混写
7. `GC-VLN`：
   - 已确认 `CoRL 2025`
   - 有官方项目页与官方仓库
   - 但 README 仍写明完整代码稍后发布，因此当前不能记成成熟完整开源
8. `DifNav`：
   - 已确认官方仓库公开了 evaluation code 与 checkpoints
   - 但 online augmentation code 和训练代码仍未公开
   - 主实验是按 `Open Area / Narrow Space / Stairs` 做 scene-category 评测，不是标准完整 `R2R-CE val-unseen`
9. `MonoDream`：
   - 已确认其主实验直接覆盖 `R2R-CE / RxR-CE`
   - 并明确“不使用外部 web 数据，只用 simulator + 500K DAgger”
   - 目前仍未核到官方代码与项目页
10. `VPN`：
   - 已确认 `AAAI 2026`
   - 官方代码仓存在
   - 但它属于 `R2R-VP / R2R-CE-VP` 视觉提示导航变体任务，不是标准语言 VLN 主线 baseline

### 本轮对 shortlist 的更新结论

1. `Ground Slow, Move Fast` 继续保留在高位，并提升为“代码侦察高优先”候选。
2. `VLN-Zero` 与 `GC-VLN` 继续保留在“持续跟踪但非第一优先复现”分组中。
3. `MonoDream` 新增进入“持续跟踪但非第一优先复现”分组，原因是方法价值高，但公开生态不完整。

### 当前确认的流程约束

1. 每次批量粗读都必须同步做外网事实核查。
2. GitHub 仓库、README、项目页、模型页和数据页都属于必核查对象。
3. 外网命令统一优先走代理，推荐形式：
   - `bash -ic 'proxy >/dev/null; <command>'`
4. `sampled subset`、`pre-exploration`、额外数据、额外监督、额外传感器、benchmark 变体都必须显式标注。
5. 对“仓库存在但完整代码尚未发布”的论文，不能误写成“官方代码已完整开源”。

### 当前阻塞

1. 当前 shell 中 `conda` 仍不可用。
2. 因此如果下一步进入脚本开发、代码实现或需要正式运行 Python 工具链，仍需先修复 conda 初始化。

### 当前判断

1. 当前项目仍处于“粗读资产建设 + shortlist 校正 + baseline / codebase reconnaissance 前置侦察”阶段。
2. 现在的论文主池已经不再包含 UAV / aerial / prompt-only 变体和纯离散上游任务，后续粗读不会再沿旧口径继续扩散。
3. 当前 `16` 到 `25` 批次中，最值得后续优先精读的是：
   - `Ground Slow, Move Fast`
   - `NavForesee`
   - `JanusVLN`
   - `MonoDream`
   - `DAgger Diffusion Navigation`
4. 当前 `16` 到 `25` 批次中，最值得后续优先看代码的是：
   - `Ground Slow, Move Fast`
   - `JanusVLN`
   - `VLN-Zero`
5. 这一轮之后，更清晰的研究关注点仍然是：
   - explicit world representation
   - topo granularity / graph constraints
   - hierarchical planning / progress / recovery
   - streaming / compressed history
   - diffusion low-level expert
   - monocular latent imagination
6. 对于 `P^3Nav` 这类新论文，后续粗读要更强调：
   - 它到底补的是哪一层接口缺口
   - 图表和消融真正支持了什么判断
   - 与当前课题的接口价值，而不只是模板摘要
7. `P^3Nav` 预览稿需要继续升级为“研究笔记型”写法：
   - 先给高层结论
   - 再抓最关键的方法逻辑和图表证据
   - 再讲真正有启发的实验与消融
   - 最后给出值得继续投入的判断
8. `P^3Nav` 正式稿已完成覆盖；如果用户认可，这一写法将作为后续批量粗读的新标准。

### 下一步

1. 从 `docs/paper_list_new_additions_round2.md` 启动下一轮粗读，而不是沿旧版顺序继续。
2. 新增论文里建议优先粗读：
   - `PROSPECT`
   - `LatentPilot`
   - `NaVIDA`
   - `NavTrust`
   - `VLNVerse`
   - `SmartWay`
   - `InstructNav`
   - `Waypoint Models / LAW`
3. 每完成一批，继续同步复核 `docs/paper_quality_shortlist.md`。
4. 在粗读推进同时，逐步准备高优先级论文的 codebase reconnaissance，当前优先顺序建议先看：
   - `Ground Slow, Move Fast`
   - `JanusVLN`
   - `ETP-R1`
   - `CLASH`
   - `StreamVLN`
5. 在进入任何 Python 运行型任务前，先解决 conda 环境可用性问题。
