# Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation 粗读

## 基本信息

### 论文标题
Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation

### 中文标题
Ground Slow, Move Fast：面向通用视觉语言导航的双系统基础模型

### 任务身份
这篇论文是 strict direct-hit 的 continuous VLN / VLN-CE 主线论文，而且是这一批里最值得重视的系统级工作之一。它不只是提出了一个更强的导航器，而是把 continuous VLN 明确拆成：
- 高层语义推理与中程目标落点
- 低层连续轨迹生成与动态避障

这正面回应了当前主线里最关键的接口问题：`semantic reasoning` 和 `real-time continuous control` 如何解耦又如何协同。

### arXiv 首次提交日期
2025-12-09

### 录用情况
当前可较高可信度记为：
- `ICLR 2026`
- `arXiv v1 已公开`

核实依据不是 arXiv comment，而是：
- 官方 `InternNav` README 已将该文作为 `ICLR 2026` 论文引用
- 可检索到对应 `OpenReview` 条目

### 作者
Meng Wei、Chenyang Wan、Jiaqi Peng、Xiqian Yu、Yuqiang Yang、Delin Feng、Wenzhe Cai、Chenming Zhu、Tai Wang、Jiangmiao Pang、Xihui Liu

### 所属机构
论文首页列出的核心机构包括：
- Shanghai AI Laboratory
- The University of Hong Kong
- Zhejiang University
- Tsinghua University

### 资源入口
- arXiv：https://arxiv.org/abs/2512.08186
- PDF：https://arxiv.org/pdf/2512.08186
- HTML：https://arxiv.org/html/2512.08186v1
- 项目页：https://internrobotics.github.io/internvla-n1-dualvln.github.io
- 代码：https://github.com/InternRobotics/InternNav
- 模型：https://huggingface.co/InternRobotics/InternVLA-N1-DualVLN
- 数据：https://huggingface.co/datasets/InternRobotics/InternData-N1
- 代码仓说明文档：https://internrobotics.github.io/user_guide/internnav/index.html

需要特别注意：
- 这篇论文的代码不是单独“小仓库”，而是并入 `InternNav` 统一导航工具箱
- 对复现者来说，这意味着生态完整，但也意味着工程面更重

### 数据与基准
论文覆盖的主评测面非常广：
- `R2R-CE`
- `RxR-CE`
- `VLN-PE`
- `Social-VLN`
- 多平台真实机器人实验

训练数据方面，官方主页和代码仓说明显示其背后依托：
- `R2R`
- `R2R-EnvDrop`
- `RxR`
- `ScaleVLN` 子集
- `DAgger` 增广数据
- 更大规模的 `InternData-N1`

因此这篇论文虽然主榜结果很强，但默认不是“最朴素数据设定”下的公平 baseline。

### 证据来源
- arXiv 摘要页
- arXiv HTML 主文
- 官方项目页
- 官方代码仓 `InternNav` README
- Hugging Face 模型页 / 数据页

### 当前未核实项
- 单独 checkpoint 与各子模块权重的精细对应关系
- `InternData-N1` 各子来源对主表结果的精确贡献比例

## 这篇论文要解决什么问题

### 问题定义
作者认为，近一批大模型 VLN 方法虽然泛化变强，但大多仍然采用一种单链路范式：
- 把视觉观测和语言指令直接映射成短视野离散动作

这种设计在 continuous VLN 里会同时暴露三个问题：
- 动作序列碎片化，不够平滑
- 推理频率低，响应迟缓
- 面对动态障碍、楼梯、拥挤场景时稳定性不足

### 作者对 prior work 的核心判断
作者不是简单批评 prior work “不够强”，而是认为问题出在接口层：
- 大 VLM 擅长语义理解和目标落点推理
- 但不适合高频、低时延、连续控制
- 端到端硬连会同时损害高层泛化和低层实时性

换句话说，现有 VLN agent 把“慢推理”和“快控制”混成了一套网络，导致两边都做不好。

### 这篇论文试图补的关键缺口
它要补的是一个非常明确的系统缺口：
- 高层语义目标到底应该输出什么，才能有效驱动低层控制器
- 低层控制器又如何在不破坏高层泛化的前提下，实现高频轨迹执行、动态避障和误差吸收

### 为什么这个问题对当前课题很重要
这篇论文和你当前课题的耦合度极高，因为它直接对应：
- `hierarchical planning-control`
- `subgoal / latent bridge`
- `obstacle avoidance`
- `closed-loop stability`
- `real-world deployment`

如果后续你要设计“高层 video/VLM backbone + 低层 continuous action expert”的路线，这篇基本就是必须重点回看的系统参照物。

## 一句话概括方法

DualVLN 的核心做法是：用一个低频运行的大型 VLM 负责从第一视角图像与语言中预测中程 `pixel goal + latent goal`，再用一个高频运行的轻量 diffusion policy 把显式像素目标和隐式潜变量共同转成连续、平滑、可避障的局部轨迹，从而把高层语义推理和低层实时控制解耦成一个真正可部署的双系统导航模型。

## 核心方法

### Figure 1：整篇论文的中心思想就是“慢思考 + 快执行”
Figure 1 非常关键，它不是普通 pipeline 示意图，而是直接给出了 DualVLN 的时间尺度分工：
- `System 2`：慢速，约 `2 Hz`
- `System 1`：快速，约 `30 Hz`

这张图把作者的核心判断说得很清楚：
- 高层 VLM 不应该承担高频控制责任
- 低层控制器也不应该重新做一遍指令理解

### 整体框架
DualVLN 由两个系统组成。

#### System 2：VLM-based Global Planner
输入：
- 历史第一视角图像
- 当前图像
- 语言指令

输出：
- 显式 `pixel goal`
- 隐式 `latent goal`

它负责中程目标推理，也就是“下一个应该往图像中的哪里走”。

#### System 1：Diffusion-based Local Policy
输入：
- 高频 RGB 输入
- 来自 System 2 的 `pixel goal`
- 来自 System 2 的 `latent goal`

输出：
- 连续局部轨迹

它负责高频、平滑、可执行的连续运动生成，并处理动态障碍与局部扰动。

### Figure 2：真正重要的是两个系统之间的桥
Figure 2 显示 DualVLN 不是简单串联，而是通过两种目标桥接：
- `explicit pixel goal`
- `implicit latent goal`

`pixel goal` 的价值在于：
- 可解释
- 容易验证
- 能让低层明确知道高层要去哪里

`latent goal` 的价值在于：
- 传递纯像素坐标之外的语义与上下文压缩信息
- 提供比单一点位更丰富的条件

这其实就是一个非常典型、也非常值得借鉴的 `subgoal / latent bridge` 设计。

### 为什么像素目标很关键
作者专门强调高层输出 `pixel goal`，而不是直接输出连续轨迹或离散动作。
这件事很重要，因为：
- 连续轨迹太低层，会让高层背负不必要的控制负担
- 离散动作太短视，不足以稳定指导连续局部运动
- 像素目标恰好是“语义 grounding”与“控制条件”之间的中层接口

从方法论上说，这篇论文证明了：
- 高层 VLM 输出中程、可解释、图像内锚点，是非常合理的

### 训练方式：先解耦，再对接
论文明确采用分阶段训练思想：
- 先把 System 2 训练成稳定的 pixel-goal grounding 模型
- 再冻结 System 2
- 对 latent query 做 prompt-tuning
- 最后让 System 1 学习在显式与隐式双目标条件下输出轨迹

作者认为这样做的好处是：
- 保住高层 VLM 的泛化能力
- 避免低层轨迹学习反向污染高层语义推理

这和很多 end-to-end policy 的思路完全不同，更偏向“接口清晰的系统协同”。

### 与 prior work 的本质区别
它与之前代表性方法的根本差别不在“用了 diffusion”这么简单，而在于：
- 不再让一个单体模型同时做全局 reasoning 和局部高频控制
- 不再把 low-level policy 视作高层 VLM 的附属头
- 明确把连续导航问题拆成语义 grounded mid-term target 与 continuous local trajectory 两个层面

这使它比传统 waypoint predictor + planner 更 end-to-end，
又比单体大模型直接出动作更可控。

## 实验做了什么，结果如何

### benchmark 与设置
主实验覆盖：
- `R2R-CE Val-Unseen`
- `RxR-CE Val-Unseen`
- `VLN-PE`
- `Social-VLN`
- 多平台真实机器人

其中主榜 `R2R-CE / RxR-CE` 是最重要的可比面。

### 主结果：R2R-CE 与 RxR-CE 都很强
在 `R2R-CE Val-Unseen` 上，DualVLN 达到：
- `NE 4.05`
- `OSR 70.7`
- `SR 64.3`
- `SPL 58.5`

在 `RxR-CE Val-Unseen` 上，DualVLN 达到：
- `NE 4.58`
- `SR 61.4`
- `SPL 51.8`
- `nDTW 70.0`

这组结果说明它不是只在一个 benchmark 上奏效，而是在两条主线 benchmark 上都非常有竞争力。

### VLN-PE：双系统接口在物理控制平台上更有意义
在 `VLN-PE` 上，作者分别报告了 flash controller 与 physical locomotion controller。

其中 `flash controller` 结果为：
- `NE 3.90`
- `OSR 69.93`
- `SR 63.62`
- `SPL 56.49`

`physical controller` 结果为：
- `NE 4.66`
- `OSR 55.9`
- `SR 51.60`
- `SPL 42.49`

论文特别强调：
- 即使不在 VLN-PE 轨迹上单独微调，DualVLN 依然超过所有基线

这很能说明双系统接口对“更真实的物理控制噪声”是有帮助的。

### Social-VLN：动态障碍下仍有明显优势
作者还引入了 `Social-VLN`，这是一个建立在 `R2R-CE` 上、显式引入动态 humanoid 干扰的 benchmark。

在 `Social-VLN` 上，DualVLN 行显示：
- `NE 5.97`
- `OSR 41.0`
- `SR 37.2`
- `SPL 35.8`
- `HCR 35.4`

论文正文指出：
- DualVLN 相比标准 VLN 结果大约掉了 `27%` 的成功率
- StreamVLN 也掉了大约 `26%`

这说明动态社会场景对当前 VLN 仍然很难，但 DualVLN 至少把问题正面拉出来测了，而且比对手更稳。

### 真实机器人：不仅是“能跑”，而是跨 embodiment 能跑
真实机器人实验用了三类平台：
- `Turtlebot4` 轮式机器人
- `Unitree Go2` 四足机器人
- `Unitree G1` 人形机器人

系统运行方式是：
- 机器人采集同步图像
- 远端 `RTX 4090` 服务器异步推理
- 整体占用约 `20GB` 显存

论文描述的真实场景包括：
- office
- canteen
- street
- convenience store

作者给出的结论是：
- 模型在不同机体高度、震动和 tracking 条件下都能保持较强鲁棒性

这对“能否跨 robot morphology 泛化”是非常有价值的证据。

## 图表与案例分析

### Figure 1：系统级贡献一图说清
Figure 1 的价值不是好看，而是把这篇论文和所有“单网络导航器”彻底区分开：
- 高层慢速 VLM
- 低层高速 diffusion policy

这张图其实就是整篇论文最重要的研究判断。

### Figure 7：显式像素目标与隐式潜变量缺一不可
作者在消融里比较了：
- 没有先训练 System 2
- 没有 pixel goal
- 只有单一种类条件

核心结论是：
- 如果没有显式 pixel goal，System 1 很难学出稳定轨迹
- 如果没有 latent goal，局部策略又会损失一部分语义与上下文指导

也就是说，这篇论文不是“pixel goal alone”路线，而是显式与隐式双桥接路线。

## 消融与方法学判断

### 先训练高层再冻结，是必要条件
作者明确观察到，如果不采用 decoupled training：
- diffusion policy 收敛会慢很多
- 高层 VLM 的泛化还会被拖坏

这说明这篇论文最重要的方法学判断之一是：
- 对这种“高层 foundation model + 低层 control policy”系统，硬端到端联训并不一定更优

### 显式 pixel goal 对轨迹一致性非常关键
作者还做了轨迹投影分析，把预测轨迹重新投回图像平面，衡量轨迹与像素目标之间的一致性。
结论是：
- 成功率越高的 DualVLN 版本，其轨迹点与像素目标距离越近、角度偏差越小

这说明 `pixel goal` 不是仅用于解释的可视化辅助，而是真正驱动局部策略学习的核心条件。

### Social-VLN 证明低层控制的价值不只是“平滑”
如果只看标准 `R2R-CE / RxR-CE`，你可能会觉得 System 1 只是让轨迹更顺。
但 Social-VLN 和真实机器人实验说明：
- 它更重要的价值是为动态障碍、临时偏差、控制噪声提供吸收层

这使得 DualVLN 更像一种 `closed-loop controller architecture`，而不是单纯的 VLN model。

## Benchmark 可比性与复现生态

### 可比性检查
- 是否直接可比 `R2R-CE`：`是`
- 是否直接可比 `RxR-CE`：`是`
- 是否使用额外预训练数据：`是`
- 是否使用额外导航数据：`是`
- 是否使用额外标注 / teacher / DAgger 数据：`是`
- 是否依赖额外传感器做主榜结果：`主榜 DualVLN 行是 RGB；真实部署含 RGB-D / odometry`
- 是否含扩展 benchmark：`是，VLN-PE 与 Social-VLN`

这里必须强调：
- 这篇论文的主榜结果虽然直接可比，但其训练数据生态显著强于传统“只用 benchmark train split”的工作

### 复现生态
- 代码是否公开：`是，公开在 InternNav`
- 模型是否公开：`是`
- 数据是否公开：`是`
- 文档是否完整：`较完整`
- 复现门槛：`中高`

复现门槛高的原因主要是：
- 工具箱较大
- 涉及多 benchmark / 多平台
- 真实部署链路较重

但和“只有论文没代码”的方法相比，它已经属于生态非常完整的一类。

### 当前判断
这篇论文同时适合作为：
- 高层架构参考
- 低层接口设计参考
- 真实部署参考
- 代码侦察候选

但它不适合作为“最朴素公平 baseline”的原因也很明确：
- 训练数据和系统资源都偏强

## 亮点

### 亮点 1
它把 continuous VLN 中最难讲清楚的接口问题讲清楚了：高层输出 `pixel goal + latent goal`，低层输出连续轨迹。

### 亮点 2
它不是停留在模拟器主榜，而是把 `VLN-PE`、`Social-VLN` 和真实机器人全部接起来，形成完整系统闭环。

### 亮点 3
代码、模型、数据、文档都已公开，具备很高的后续侦察价值。

## 局限与风险

### 局限 1
主榜结果依赖很强的数据生态，不能把它误当成“只靠模型结构创新就达到的纯净增益”。

### 局限 2
工程系统较重，复现和二次改造成本高于普通单仓库方法。

### 局限 3
虽然双系统清楚，但真正端侧部署时仍然需要远端算力配合，说明实时全本地化还不是它当前的重点。

## 对当前课题的启发

### 最值得借鉴的部分
最值得借鉴的是它把高层目标显式化成 `pixel goal`，同时再加一个 `latent goal` 作为隐式桥。这比单纯输出 waypoint 或动作都更适合作为 VLM 到 control expert 的接口。

### 不该直接照搬的部分
不建议直接照搬它的大而全训练生态。对当前课题来说，更应学习的是：
- 双系统分工
- 中层目标接口
- 低层 diffusion 执行器的职责边界

而不是原样复刻 `InternData-N1 + 全套工具箱`。

### 对应核心问题映射
- `history / memory`：中
- `progress`：中
- `hierarchical planning-control`：高
- `subgoal / latent bridge`：高
- `obstacle avoidance`：高
- `deadlock recovery`：中高
- `closed-loop stability`：高

## 是否值得继续投入

### 是否值得精读
高

### 是否值得优先复现 / 代码侦察
高

### 建议后续动作
- 优先侦察 `InternNav` 中 `DualVLN` 对应模块
- 单独梳理 `System 2 -> pixel goal / latent goal -> System 1` 的接口张量与训练顺序
- 与 `JanusVLN`、`NavForesee`、`DifNav` 做“高层-低层接口”视角的并排比较

## 一句话结论

Ground Slow, Move Fast 最重要的价值，不只是把 diffusion 用进 VLN，而是首次把 continuous VLN 系统性拆成“慢速语义 grounded planner + 快速连续轨迹 policy”的双系统基础模型；它既是当前主线里极强的结构参考，也是非常值得优先侦察代码的一篇高质量论文。
