# NavTrust: Benchmarking Trustworthiness for Embodied Navigation 粗读

## 这篇论文为什么重要

这篇论文的价值和方法论文不一样。它最重要的地方不在于提出了一个新的导航器，而在于把 embodied navigation 里一个长期被默认忽略的问题单独做成了 benchmark：现有导航模型在真实部署里到底有多不可信，以及这种不可信具体来自哪些输入模态。

过去很多 VLN 和 OGN 论文默认沿着一条很熟悉的路径写：在 clean simulator setting 下比较 `SR / SPL / nDTW`，然后把更强的结果直接解释为更好的导航能力。但真实机器人遇到的问题往往不是 clean RGB、完美 depth 和规范 instruction，而是：
- 镜头脏污、低照度、黑屏、模糊；
- depth 缺失、量化误差、多径反射；
- instruction 写得不标准、被压缩、省略、改写，甚至被 prompt 注入污染。

NavTrust 的切入点正是这里。作者不是再做一个 robustness supplement，而是提出一个统一 benchmark，把 `VLN` 和 `OGN` 一起放到 RGB、depth、instruction 三类 corruption 下，并进一步比较不同 mitigation strategy 到底有没有用。这件事对当前项目很有价值，因为它会直接影响后续：
- baseline 应不应该只看 clean 主榜；
- codebase reconnaissance 时哪些方法值得继续投入；
- 新方法设计时哪些 robustness failure 是必须正面处理的。

如果说很多导航论文回答的是 “clean benchmark 下谁更强”，那 NavTrust 回答的是另一个更现实的问题：`这些方法一旦离开理想输入，还剩下多少可用性。`

## 基本信息与当前公开情况

- 标题：NavTrust: Benchmarking Trustworthiness for Embodied Navigation
- arXiv：`2603.19229`
- arXiv v1：`2026-03-19`
- 作者：Huaide Jiang, Yash Chaudhary, Yuping Wang, Zehao Wang, Raghav Sharma, Manan Mehta, Yang Zhou, Lichao Sun, Zhiwen Fan, Zhengzhong Tu, Jiachen Li
- 机构：`UC Riverside / University of Michigan / Workday / USC / Lehigh / Texas A&M`

截至 `2026-04-12`，我核到的公开情况是：
- arXiv abstract / HTML 可访问
- 官方项目页已公开：`https://navtrust.github.io/`
- 项目页明确写着：`Code (Coming Soon)`
- 当前未检到正式公开的官方仓库入口

所以这篇论文现在的状态比较明确：
- benchmark 定义、项目页和可视化结果已经公开；
- 但代码尚未发布，短期内更适合拿来做 benchmark understanding，而不是直接复现。

## 这篇论文真正补了什么缺口

NavTrust 补的不是某个模型性能缺口，而是 benchmark 口径缺口。

作者认为现有 embodied navigation 评测存在三个长期问题：
- 多数工作只看 clean input，对真实世界常见 corruption 几乎不测。
- VLN 和 OGN 的 robustness 往往各测各的，缺乏统一 protocol。
- 即便有人测鲁棒性，也经常只测 RGB，而很少系统测 depth；更少有人把 mitigation strategy 放进同一个框架里 head-to-head 比较。

因此 NavTrust 的核心贡献其实是三件事：
- 把 `RGB / depth / language` 三类 corruption 放进统一 benchmark。
- 把 `VLN` 和 `OGN` 都纳入同一个 trustworthiness evaluation frame。
- 不只是做 failure diagnosis，还系统比较 `data augmentation / teacher-student distillation / adapters / safeguard LLM` 这四类 mitigation 策略。

这也是为什么我会把它看成一篇很值得保留的 benchmark 论文，而不是“又一篇 robustness 附录”。

## Benchmark 设计里最值得记的几部分

### 它不是只测 VLN，而是把 VLN 和 OGN 放到了同一张 robustness 地图里

论文的数据基础是：
- `VLN`: `R2R` 和 `RxR`
- `OGN`: `Habitat-Matterport3D` 的 unseen split

作者专门强调，他们对齐了 VLN 和 OGN 的 start / goal locations，使得两类 agent 能在相同空间条件下比较。这一点很关键，因为它让 benchmark 不只是两个任务拼盘，而是一个真正统一的 trustworthiness surface。

从当前课题角度看，这个设计很有价值。因为后面如果要比较 “语言条件导航” 和 “目标条件导航” 的鲁棒性差异，这篇论文已经提供了一个统一入口。

### RGB corruption 设计得很像真正机器人会遇到的问题

NavTrust 的 `RGB corruption` 一共八类：
- `Motion Blur`
- `Low-Lighting w/o Noise`
- `Low-Lighting w/ Noise`
- `Spatter`
- `Flare`
- `Defocus`
- `Foreign Object`
- `Black-Out`

这套设计有一个我比较认可的判断：作者没有把 motion noise、wheel slip、pose drift 直接建模成控制层扰动，而是优先把很多真实机器人最终“看起来像什么”的视觉后果建模出来。比如高速抖动最终在画面上往往表现为 blur，这样做的好处是 benchmark 更 simulator-agnostic、更可复现。

这说明他们的 benchmark 思路是面向 perception-policy pipeline 的，而不是面向底层动力学仿真。

### Depth corruption 是这篇论文最应该记住的新增点

很多 embodied benchmark 对 depth 的态度其实非常理想化：默认只要有 depth，depth 就是更可靠的几何 backbone。NavTrust 恰恰挑战了这个默认前提。

它加入了四类 depth corruption：
- `Gaussian Noise`
- `Missing Data`
- `Multipath`
- `Quantization`

这四类都不是随便拍脑袋加的：
- `Missing Data` 对应透明/反光表面导致的无效深度；
- `Multipath` 对应 ToF 传感器角落或高反射表面的深度回波；
- `Quantization` 对应低比特深度压缩；
- `Gaussian Noise` 对应低成本深度相机和复杂照明下的深度抖动。

这部分是整篇论文我最想保留的 benchmark 资产之一。因为它直接提醒我们：`depth` 不是天然的鲁棒性加成，它本身也会成为主要 failure source。

### Instruction corruption 设计得比“改几个词”更系统

论文把 instruction corruption 做成了五个维度：
- `Diversity of Instructions`：用 LLaMA-3.1 为每条 instruction 生成 `friendly / novice / professional / formal` 四类风格改写
- `Capitalizing`：把名词、动词、方位词等关键 token 全部大写
- `Masking`：把 stopwords 或低空间相关词替换成 `[MASK]`
- `Black-Box Malicious Prompts`
- `White-Box Malicious Prompts`

这套设计不是为了做 NLP 花活，而是很直接地测三件事：
- 模型对表面形式变化到底有多敏感
- 模型的 tokenizer / vocabulary 设计会不会把真实口语或风格改写直接变成脆弱点
- prompt-based navigator 会不会被系统提示层级的恶意注入干扰

这一点对 current project 尤其重要，因为如果后面继续往 VLM / LLM navigator 方向走，instruction robustness 不可能再只靠 clean benchmark 来判断。

### 它还把 mitigation strategy 一并标准化了

这篇论文真正“做得完整”的地方，是它没有停在发现问题，而是继续比较四类 mitigation：
- `Corruption-aware Data Augmentation`
- `Teacher-Student Distillation`
- `Adapters`
- `Safeguard LLM`

这里的设计是很务实的。作者不是为了提出新方法，而是想回答：对于 embodied navigation，这几种常见鲁棒化路线到底谁更适合哪种 corruption。

## 实验里最有价值的发现

### 第一层结论：很多主流方法在 corruption 下掉得比想象中更厉害

作者一共评了七个 agent：
- `VLN`: `NaVid / Uni-NaVid / ETPNav`
- `OGN`: `L3MVN / WMNav / VLFM / PSL`

结论非常直白：clean condition 下看起来不错的 agent，在 corruption 下会出现非常明显的 success collapse。

RGB corruption 下，作者给了几个很能说明问题的例子：
- `Black-out` 和 `Foreign-object` 对 RGB-only agent 特别致命；
- 在 `RxR` 上，`NaVid / Uni-NaVid / PSL` 在黑屏或遮挡下普遍掉得比 depth-involved 方法更狠；
- `VLFM` 的 overall PRS 最强，`PRS-SR / PRS-SPL` 都能达到 `0.94`，说明 foundation-model prior + frontier ranking 这条路线在感知退化下确实更稳。

这部分说明的不是哪个单一模型最强，而是：`是否使用 depth`、`depth 如何接入`、`visual backbone 的预训练方式`，都会显著改变 corruption profile。

### 第二层结论：depth 不是银弹，depth corruption 自己也会把系统打崩

论文对 depth corruption 的分析很值得仔细记。

几个典型现象是：
- `Gaussian noise` 和 `Missing data` 对依赖 depth 的方法破坏很大；
- `L3MVN` 在一些 depth corruption 下甚至能从 `SR 50%` 直接掉到 `2%`；
- `VLFM` 也会从 `50%` 直接掉到 `0%`；
- `ETPNav` 和 `WMNav` 相对更稳，但也远谈不上免疫。

作者进一步给出一个很重要的判断：`Simply adding a depth sensor does not ensure robustness; the fusion strategy is critical.` 这句话我觉得可以直接记住。

也就是说，真正决定鲁棒性的不是 “有没有 depth”，而是：
- depth 是原始输入直接 early fusion 进去；
- 还是经过更稳健的中间处理再融合；
- 系统是否过度依赖某个几何通道。

### 第三层结论：instruction corruption 暴露了 tokenizer 和 vocabulary 层面的脆弱性

这一段是对当前项目最直接有启发的部分。

论文给了几个很具体的数字：
- 在 `RxR` 上，`50% masking` 会让 `NaVid` 掉 `12% SR`，`ETPNav` 掉 `28% SR`，`Uni-NaVid` 掉 `21% SR`
- `professional / formal` 这类高词汇密度风格改写，会让 `NaVid` 掉大约 `22-26% SR`，`ETPNav` 掉 `37-40% SR`，`Uni-NaVid` 掉 `31-36% SR`

这组结果非常说明问题。它说明 VLN 里的 instruction robustness 不只是“语义理解能力强不强”，还跟：
- tokenizer 对非常规词形的适配
- vocabulary 覆盖
- instruction canonicalization 能力
- system prompt 是否容易被恶意短语带偏
直接相关。

作者还总结了 `RxR` 上 instruction corruption 的 retention：
- `NaVid` 约 `PRS-SR / PRS-SPL = 0.64 / 0.64`
- `Uni-NaVid` 约 `0.58 / 0.58`
- `ETPNav` 约 `0.48 / 0.46`

这里最值得记的是：`ETPNav` 虽然是强 baseline，但它的 instruction robustness 反而明显落后，作者把这一点归因于 tokenizer 紧耦合和词汇覆盖较窄。这种 failure mode 是后面做 open-source embodied LLM 时必须正面面对的。

## Mitigation 结果最值得记的东西

### 对 RGB / depth corruption，最有效的不是单帧随机增强，而是保持 episode 一致性的 augmentation

在 `ETPNav` 上，作者把 data augmentation 分成：
- `Per-frame DA`
- `Per-episode DA`
- `Distributed per-episode DA`
- 更高强度的 `Per-episode DA`

结果很有意思：
- `Per-frame DA` 的 `PRS-SR` 是 `RGB 0.89 / Depth 0.67`
- `Per-episode DA` 提升到 `RGB 0.92 / Depth 0.72`
- `Distributed per-episode DA` 是 `RGB 0.93 / Depth 0.73`
- 更高强度版本达到 `RGB 0.94 / Depth 0.75`

作者给出的解释也很合理：像 `ETPNav` 这种在线拓扑建图系统，本身就依赖时间一致性。如果 corruption 每帧都乱跳，反而会破坏 graph update 的稳定性。把 corruption 保持为整段 episode 内一致，反而更贴近真实 sensor degradation。

这个观察很实用，不只是 benchmark 结论，而是后续做鲁棒化训练时可以直接迁移的方法学判断。

### Teacher-Student Distillation 对 depth corruption 特别有效

`Teacher-Student distillation` 的结果是：
- `PRS-SR(RGB) = 0.93`
- `PRS-SR(Depth) = 0.85`

相比 augmentation，它对 depth corruption 的收益尤其明显。作者认为原因是：teacher 提供了更稳定的结构化决策和中间特征，可以把 noisy geometry 对 planner 的破坏部分抵消掉。

这说明如果系统是类似 `planner + geometry` 的 modular pipeline，distillation 可能比单纯 exposure 更能保住 long-horizon intent。

### Adapter 的效果有明显不对称：depth 侧有效，RGB 侧不太行

这篇论文没有把 adapter 写得过于乐观，反而这一点让我更相信结果。

作者直接说：
- depth / RGB 双通道 residual adapters 整体上能提高 depth robustness
- 但 RGB adapter 在他们的设置里表现不好，主要因为 `TorchVision ResNet-50` 与 `VlnResnetDepthEncoder` 的表示特性不同，难以共享同样的修正策略

从 Table II 也能看出来：
- `Adapter` 在 `Depth PRS-SR` 上能到 `0.89`
- 但 `RGB PRS-SR` 只有 `0.33`

这说明 parameter-efficient robustness tuning 不是随便往 encoder 上塞一个 adapter 就能统一解决问题，sensor branch 的表征结构本身决定了 adapter 能不能奏效。

### Safeguard LLM 是 instruction robustness 里很值得记的一招

在 instruction corruption 上，作者用两种 safeguard：
- fine-tuned `LLaMA 3.2`
- prompt-engineered `OpenAI o3`

结果都有效，但作用方式不同：
- fine-tuned LLaMA 3.2 对 strip 掉 adversarial content、把输入规范化成 canonical form 更强
- `o3` 更擅长处理风格改写、词汇替换和语气变化

论文报告的 `PRS-SR` 提升是：
- fine-tuned LLaMA 3.2：对 `NaVid / Uni-NaVid / ETPNav` 分别提升 `0.14 / 0.20 / 0.32`
- prompt-engineered `o3`：分别提升 `0.03 / 0.08 / 0.20`

这组结果很有启发性，因为它说明 instruction robustness 不一定非要重训 navigator。有时候在输入侧加一个 canonicalization / safeguard layer，就已经能大幅改善脆弱性。

## 真实机器人部署部分为什么值得看

这篇论文的 real-world 部分不是很大，但很有价值，因为它不是纯 showcase，而是明确在验证 “simulation 里看到的 corruption trend 是否能转移到真实机器人”。

作者把 `Uni-NaVid` 和 `ETPNav` 部署到了 `RealMan` 机器人平台，在 lab 环境下测导航步数。

几个结果很值得记：
- clean condition 下，两者都在 `25 steps` 完成
- `Low-Lighting w/ Noise` 和 `Black-out` 下，`Uni-NaVid` 直接 fail，而 `ETPNav` 虽然变慢，但还能完成，分别要 `50` 和 `52` 步
- 对 `ETPNav` 使用 corruption-aware data augmentation 后，这两个场景下降到 `42` 和 `46` 步
- 在 `Professional` instruction 改写下，`Uni-NaVid` 需要 `55` 步，`ETPNav` 直接 fail
- 引入 safeguard LLM 后，`Uni-NaVid` 从 `55 -> 33` 步，`ETPNav` 从 fail 恢复为 `49` 步完成

这些结果说明 NavTrust 的价值不只是给出一套 synthetic benchmark，而是 benchmark 上看到的 failure and mitigation trend 至少在一定程度上能迁移到真实机器人。

## 我对这篇论文的总体判断

我认为 NavTrust 非常值得进入当前高质量论文列表，但理由和方法论文不一样。

它的核心价值在于：
- benchmark 口径非常对当前项目；
- corruption taxonomy 做得系统，而且 depth 这块补得很关键；
- mitigation evaluation 不是附带小实验，而是真的能指导后续方法选型；
- real-world deployment 给了 benchmark validity 的外部证据。

当然，它也有边界：
- 本质上它是 benchmark / evaluation paper，不提供新的导航主干。
- mitigation 实验主要做在 `R2R subset` 和少数模型上，不是所有方法都全面覆盖。
- 很多 corruption 仍然是 simulator-based synthetic corruption，而不是真实传感器日志回放。
- 代码还没公开，短期内更适合做研究判断，不适合直接复现 benchmark pipeline。

但这些边界不影响它的重要性。因为对当前课题来说，trustworthiness benchmark 本来就应该作为横向比较和方法设计的底层约束，而不是等模型做完再顺便补。

## 对当前课题最有启发的地方

### 1. 以后不能只看 clean benchmark

这篇论文最直接的提醒就是：如果后续还只看 `SR / SPL` clean 主表，很可能会高估很多方法的真实可用性。

### 2. depth 相关方法必须单独审视 corruption profile

很多方法一旦引入 depth、map 或几何先验，就会默认自己“更稳”。NavTrust 说明真实情况复杂得多：depth branch 本身也可能是最脆弱的那部分。

### 3. instruction robustness 很可能要单独建输入防线

如果后续继续沿 VLM / LLM 导航方向推进，instruction canonicalization、prompt sanitization、style normalization 这些工作很可能不是可选项，而是必须有的系统层。

### 4. 它应该进入当前内部高质量列表

我的判断是：
- 值得精读：高
- 值得作为 benchmark / protocol 参考：高
- 值得优先复现：中
- 值得优先做 code reconnaissance：中偏低，主要因为代码尚未公开

它更像一篇后续所有 baseline 比较都应该反复回看的 benchmark paper。
