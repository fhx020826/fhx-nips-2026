# 项目交接总览（新对话继承用）

本文档用于在开启新对话时，快速把当前项目的真实状态、已完成资产、当前进度、未完成事项和下一步安排完整传递给新的代理。  
默认以本文档为最高优先级的项目状态摘要；如与其他文档存在细节冲突，以最新修改时间更晚的原始文档为准，并优先回查：

- `coding.md`
- `user.md`
- `work.md`
- `findings.md`
- `docs/hpc_handbook.md`

---

## 1. 项目基本信息

- 项目目录：`/home/hxfeng/fhx-nips-2026`
- GitHub 远程：`fhx020826/fhx-nips-2026`
- 当前工作环境：
  - 本机：Windows
  - 当前机器：远端 Linux HPC
- Python / conda 环境：`fhx-nips-2026`
- 网络规则：
  - `clash` / `proxy` 是 shell function，不是独立可执行文件
  - 非交互 shell 下访问外网必须优先使用：

```bash
bash -ic 'proxy >/dev/null; <command>'
```

- HPC 约束：
  - 登录节点不要跑重负载任务
  - 重计算统一走 SLURM / 计算节点

---

## 2. 项目目标与当前主线

本项目聚焦 `continuous VLN / VLN-CE`，主要 benchmark 是 Habitat 环境下的：

- `R2R-CE`
- `RxR-CE`

当前目标不是直接押注某个方法，而是先建立高质量研究地图，再支撑后续：

1. 选题
2. baseline / codebase reconnaissance
3. 方法设计
4. 代码实现与验证

当前已经明确的研究共识：

1. 旧的 `NaviLLM + diffusion policy` 朴素端到端路线，已被降级为失败的早期探索，不再作为默认主线。
2. 当前最重要的是构建高质量研究地图，而不是继续盲目扩论文数量。
3. 当前核心方法学判断是：
   - 在 continuous VLN 中，高层语义 / 历史 / 进度理解，与低层连续控制之间存在关键接口缺口。
4. 当前重点关注的问题包括：
   - history / memory
   - progress 建模
   - hierarchical planning-control
   - subgoal / latent bridge
   - obstacle avoidance
   - deadlock recovery
   - closed-loop stability

---

## 3. 当前仓库内已经完成的核心资产

### 3.1 项目治理与环境文档

- `coding.md`
  - 统一代码规范、目录约定、中文注释、实验记录规范、清理原则
- `user.md`
  - 用户偏好、代理方式、工作区边界、远程开发限制
- `work.md`
  - 当前进展、阻塞、下一步安排
- `findings.md`
  - 关键经验和调研发现
- `docs/hpc_handbook.md`
  - HPC 使用摘要

### 3.2 论文列表与研究地图

- `docs/paper_list_feishu_strict.md`
  - 当前对外主执行列表
  - 实际上已经不是最窄 strict，而是按用户要求扩展后的 `continuous VLN / VLN-CE 相关完整版`
  - 按首次公开时间从新到旧排序
  - 当前共 `61` 篇
  - 这是后续“从头到尾依次粗读”的正式顺序来源

- `docs/paper_quality_shortlist.md`
  - 内部精选高质量 Top 30 优先级表
  - 主要用于决定优先精读、优先复现、优先借鉴的方法
  - 现在不再是唯一粗读入口，但仍是高优先级参考

- `docs/paper_list_feishu.md`
  - broad 全景池，100+ 条
  - 用于保留赛道全貌、上游链路和边界扩展
  - 不再作为主粗读执行序列

- `docs/paper_inventory.md`
  - 内部研究地图
  - 维护方法演进链、分组、direct-hit / 强相关脉络

### 3.3 论文粗读模板与粗读产物

- `docs/paper_roughread_template.md`
  - 当前正式统一粗读模板
  - 已从“自由长文粗读”升级为“叙述 + 结构化字段”的双层格式
  - 新增关键字段：
    - 任务身份
    - 证据来源
    - benchmark 可比性检查
    - 复现生态
    - 是否值得继续投入
    - 核心问题映射

- `docs/paper_roughread_top25_batch1.md`
  - 已完成第一批 Top 25 粗读卡片
  - 当前包含 5 篇：
    - `ETPNav`
    - `1st Place Solutions for RxR-Habitat Vision-and-Language Navigation Competition (CVPR 2022)`
    - `Constraint-Aware Zero-Shot Vision-Language Navigation in Continuous Environments`
    - `DAgger Diffusion Navigation`
    - `StreamVLN`

- `docs/paper_roughread_full_list_batch1.md`
  - 已开始尝试按“完整列表顺序”推进粗读
  - 当前只落地了第 1 篇：
    - `P$^{3}$Nav: End-to-End Perception, Prediction and Planning for Vision-and-Language Navigation`
  - 这份文档说明了一个事实：
    - 粗读执行入口已经从“只看 shortlist”转向“完整列表顺序推进”

### 3.4 粗读自动化脚本

- `scripts/prepare_roughread_queue.py`
  - 用于从 `docs/paper_list_feishu_strict.md` 自动抽取顺序粗读队列
  - 支持：
    - `--index`
    - `--batch-size`
    - `--format json/jsonl/md`
  - 当前用途：
    - 统一“下一篇该读谁”的队列来源
    - 生成单篇 scaffold，便于后续半自动批量粗读

- 其他已有脚本：
  - `scripts/proxy_exec.sh`
  - `scripts/collect_arxiv_dates.py`
  - `scripts/fetch_arxiv_abs_dates.py`

---

## 4. 当前最重要的调研结论

### 4.1 列表与边界

1. broad 全景池和主执行列表已经分离。
2. 当前主执行列表应以 `docs/paper_list_feishu_strict.md` 为准。
3. 这份列表虽然文件名仍叫 `strict`，但其内容已经扩展为用户认可的“continuous VLN / VLN-CE 相关完整版”。
4. 当前后续粗读应从这份列表从头到尾顺序推进，而不是只做高质量 shortlist。

### 4.2 方法与 baseline 认知

当前已形成的第一轮工程判断：

- `ETPNav`
  - 仍是最稳的 continuous VLN baseline / codebase 入口
  - 原因：
    - `R2R-CE` 与 `RxR-CE` 都有显式训练/评测入口
    - pretraining / finetuning / checkpoint 都公开
  - 但缺点是：
    - 环境依赖老
    - 依赖 waypoint predictor
    - 依赖额外预训练数据

- `RxR-Habitat 2022` 冠军方案
  - 更适合看作 `ETPNav` 的前身工程 recipe
  - 不适合作为长期主代码底座

- `CA-Nav`
  - 更适合作为 progress / constraint / sub-instruction bridge 结构参考
  - 不适合作为轻量 baseline

- `DifNav`
  - 是 diffusion 进入 continuous VLN 的关键 direct-hit 论文
  - 但当前公开训练闭环仍不完整

- `StreamVLN`
  - 是 history / streaming / deployment 路线的重要高价值新主线
  - 但 benchmark 可比性必须单独标注，因为它使用了额外导航数据、DAgger 数据和通用多模态数据

### 4.3 当前高价值方法线已经分成三类

1. 稳定 baseline / 工程底座
   - `ETPNav`

2. 高层结构接口参考
   - `CA-Nav`
   - `Ground Slow, Move Fast`
   - `NavForesee`
   - `P3Nav`

3. 历史压缩 / 在线推理 / 长程闭环
   - `StreamVLN`

---

## 5. 当前真实进度

如果要用一句话概括当前阶段：

**基础设施和研究地图已经打好，主论文列表已经稳定，粗读模板已经统一，但“完整列表逐篇粗读”还只刚刚起步，baseline / codebase reconnaissance 还没有独立抽成正式文档。**

### 5.1 已完成的阶段

- 工作区、Git、代理、conda、HPC 规则已经全部打通
- 论文列表已经从零散检索推进到：
  - broad 全景池
  - 主执行完整列表
  - 高质量 shortlist
- `arXiv v1` 日期核查和倒序排序已经完成
- 粗读模板已经统一
- 第一批 Top 25 卡片已经完成 5 篇
- 完整列表顺序粗读已经启动，并完成第 1 篇

### 5.2 尚未完成的关键阶段

- 完整列表 61 篇还没有真正逐篇按统一模板铺开
- 现有旧批次卡片还没有全部回填到新模板字段
- 很多 2025–2026 论文只完成了 paper 级事实核实，项目页 / 代码页 / 录用信息尚不完整
- baseline / codebase reconnaissance 还没有形成独立的正式文档

---

## 6. 当前阻塞与风险点

1. 文件名与内容语义已有轻微漂移：
   - `paper_list_feishu_strict.md` 文件名仍叫 strict
   - 但实际内容是扩展后的完整版时间线
   - 新代理不要再按“最窄 strict”理解它

2. 粗读形态仍不完全统一：
   - `paper_roughread_top25_batch1.md` 是旧批次粗读
   - `paper_roughread_full_list_batch1.md` 是新方向尝试
   - 两者尚未完全统一到“单论文单文件”的最终规范

3. 用户最新偏好发生了新增：
   - 用户明确希望后续粗读结果放入**单独一个文件夹**
   - 每篇论文一个 `.md` 文件
   - 文件名就是论文标题
   - 内容必须严格遵循统一模板
   - 篇幅和粒度要接近用户给出的 `Ground Slow, Move Fast` 示例
   - 不希望看到太简略的卡片式结果

4. 由于上一轮对话被中断，这个“单论文单文件”的规范**还没有真正落地完成**。
   - 也就是说：**这是当前最直接的未完成工作之一。**

---

## 7. 用户当前最新明确要求

新的代理必须特别注意下面这些最新要求：

1. 后续粗读不是只做高质量 shortlist，而是：
   - **从完整列表 `docs/paper_list_feishu_strict.md` 从头到尾依次推进**

2. 粗读结果的落盘形态要改成：
   - 单独一个目录
   - 每篇论文一个 `.md` 文件
   - 文件名是论文标题
   - 文件内只放该论文的粗读正文

3. 粗读内容要求：
   - 必须严格依照既定模板
   - 不要加多余说明性文字
   - 必须能直接复制到飞书
   - 篇幅和粒度要接近用户之前提供的详细样例
   - 不接受“过于简单”的版本

4. 调研方式要求：
   - 要尽量自动化
   - 支持后续多篇同时出结果
   - 不能每篇完全手工从零重来

---

## 8. 当前推荐的下一步执行顺序

新代理接手后，建议严格按下面顺序继续：

### Step 1：统一粗读产物的目录规范

先新建一个正式目录，例如：

- `docs/paper_roughreads_full/`

后续所有“完整列表顺序粗读”都放这里。

每篇论文一个文件，例如：

- `docs/paper_roughreads_full/P3Nav: End-to-End Perception, Prediction and Planning for Vision-and-Language Navigation.md`

### Step 2：先重写第 1 篇 `P3Nav`

不要继续沿用当前 `docs/paper_roughread_full_list_batch1.md` 的 batch 形态。  
先把 `P3Nav` 重写成：

- 单论文单文件
- 严格模板
- 接近用户样例的篇幅和细度

这是当前最直接的验收点。

### Step 3：让自动化脚本衔接“完整列表 -> 单论文 scaffold”

在 `scripts/prepare_roughread_queue.py` 基础上，继续补：

- 从 `paper_list_feishu_strict.md` 抽取第 N 篇
- 生成目标文件路径
- 自动生成单篇 markdown scaffold

这样后续每篇不会手动新建文件。

### Step 4：在用户确认 `P3Nav` 粗读口径后，继续第 2 篇

下一篇应当是：

- `EmergeNav: Structured Embodied Inference for Zero-Shot Vision-and-Language Navigation in Continuous Environments`

然后再依序推进：

- `HiMemVLN`
- `Let's Reward Step-by-Step`
- `Enhancing Vision-Language Navigation with Multimodal Event Knowledge from Real-World Indoor Tour Videos`
- `One Agent to Guide Them All`
- ...

### Step 5：粗读推进到一定规模后，再抽 reconnaissance 文档

当完整列表顺序粗读推进到一个合理批次后，再单独整理：

- `baseline / codebase reconnaissance`

重点聚焦：

- 仓库是否可跑
- 依赖栈是否过旧
- 数据 / 权重是否可得
- 最小可验证起点选谁

---

## 9. 当前目录中最关键的文件

如果新代理只读最必要文件，建议优先顺序如下：

1. `docs/project_handoff.md`
2. `work.md`
3. `findings.md`
4. `docs/paper_list_feishu_strict.md`
5. `docs/paper_roughread_template.md`
6. `docs/paper_quality_shortlist.md`
7. `docs/paper_roughread_top25_batch1.md`
8. `docs/paper_roughread_full_list_batch1.md`
9. `scripts/prepare_roughread_queue.py`

---

## 10. 当前仓库状态建议

当前仓库应该保持：

- 重要文档改动及时提交并 push
- 大日志、数据、模型、缓存不上传远程
- 不主动删除仍可能有价值的文件

当前低价值但未必必须立即删除的对象，仍包括：

- `project.md`（内容边界与时效性待后续判断）

---

## 11. 建议给新代理的最小继承说明

如果开启新对话，只想给最小必要上下文，可以直接让新代理先读：

- `docs/project_handoff.md`

然后补一句：

> 继续从 `docs/paper_list_feishu_strict.md` 的第 1 篇开始，按 `docs/paper_roughread_template.md` 的模板，把粗读结果改成“单独目录、单论文单文件”的规范化格式。先重写 `P3Nav`，达到接近 `Ground Slow, Move Fast` 示例的细度后，再继续下一篇。

---

## 12. 一句话状态结论

**这个项目当前已经完成研究地图、列表整理、粗读模板和第一批卡片化，但真正符合用户最新要求的“完整列表顺序粗读 + 单论文单文件 + 高细度模板化输出”还没有完全落地，这就是新代理接手后的第一优先任务。**
