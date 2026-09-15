# 发电量评估与不确定性

风资源进入项目评估后，需要从风速分布进一步计算长期发电量，并把尾流、可利用率、电气损失、限电和环境因素等纳入统一口径。最终输出通常不只有一个AEP数字，还需要给出相应的不确定性和超越概率。

## 1. Gross AEP与Net AEP

风机功率曲线与风况结合后，可以得到理想条件下的发电量估计。工程上通常进一步区分：

- **Gross AEP**：未扣除主要项目损失前的发电量；
- **Net AEP**：扣除预期损失后的发电量。

Lee和Fields在2021年的综述中整理了风电行业常见损失项，包括可利用率损失、尾流损失、电气损失、限电以及环境和性能相关损失。不同项目的损失构成会有明显差异。

可用一个简化关系表示：

```math
AEP_{net}
=
AEP_{gross}
\left(1-L_{wake}\right)
\left(1-L_{availability}\right)
\left(1-L_{electrical}\right)
\cdots
```

实际工程中损失项之间未必完全独立，上式主要用于理解损失如何进入能量链条。

## 2. 不确定性来源

一个项目的AEP估计会同时受到多类误差影响，例如：

- 风速测量误差；
- 测量时段的长期代表性；
- MCP或长期订正模型；
- 轮毂高度外推；
- 空间流场模型；
- 功率曲线；
- 尾流模型；
- 可利用率和限电假设；
- 年际气候变率。

这些不确定性最终会传播到能量估计。Lee和Fields的综述指出，风速本身是能量评估的关键输入，风速不确定性会显著影响AEP不确定性。传播方法和Monte Carlo示例见[不确定性如何传到AEP](03_uncertainty_propagation.md)。

## 3. P50与P90

风电项目常用P50和P90描述发电量分布。

- **P50**：有50%概率被超过的发电量；
- **P90**：有90%概率被超过的发电量，对应更保守的发电量水平。

在建设前能量评估中，P50和P90通常由预测分布及其不确定性得到。P90常用于表达较高置信水平下的项目发电能力，因此对融资和风险评估具有直接意义。

Hammond和Simley在2026年的Wind Energy Science研究中比较了建设前能量评估与实际运行数据。他们发现，样本中的P50预测仍存在系统偏差，同时长期不确定性和P90对实际预测误差的覆盖仍有改进空间。这说明P90的可靠性取决于前面的损失和不确定性建模。

## 4. 年际变率与模型不确定性

长期发电量波动至少包含两个来源：

```math
\text{AEP variability}
=
\text{climate variability}
+
\text{model / measurement uncertainty}.
```

这只是概念分解，两部分在实际分析中并不一定严格可加。

年际气候变率描述真实风况随年份变化；模型不确定性则来自测量、外推和数值模型。两者如果混在一起，容易把“某一年风偏小”解释成模型误差，或者把模型偏差误认为自然波动。

## 5. 月平均资料的额外限制

如果上游只有月平均$`u,v`$，先计算月尺度风速代理，再通过简化功率曲线得到的结果更常用于相对比较。

这种链路缺少：

- 小时级风速分布；
- 轮毂高度修正；
- 湍流与稳定度；
- 实际机组控制；
- 尾流；
- 可利用率与限电；
- 工程损失项。

因此，这类结果不能直接进入真实项目P50/P90或银行融资意义上的AEP评估。

## 6. 与本仓库案例的关系

CanESM5—ERA5案例使用CF代理检查上游风场处理差异能否传导到下游指标。它的位置大致是：

```math
\text{气候模式风场}
\rightarrow
\text{精细化}
\rightarrow
\text{风速代理}
\rightarrow
\text{CF代理}.
```

真实风电项目还需要继续经过：

```math
\text{轮毂高度风况}
\rightarrow
\text{风机与风场模型}
\rightarrow
\text{Gross AEP}
\rightarrow
\text{损失模型}
\rightarrow
\text{Net AEP}
\rightarrow
\text{P50/P90}.
```

把两条链分开，可以避免把气候研究中的代理量解释成工程项目的真实发电收益。

## 参考资料

1. Lee, J. C. Y. and Fields, M. J. (2021), *An overview of wind-energy-production prediction bias, losses, and uncertainties*.  
   https://doi.org/10.5194/wes-6-311-2021
2. Hammond, R. and Simley, E. (2026), *Biases in preconstruction estimates of wind plant annual energy production*.  
   https://doi.org/10.5194/wes-11-1251-2026
3. IEC 61400-12-1:2022, *Power performance measurements of electricity producing wind turbines*.  
   https://webstore.iec.ch/en/publication/68499
4. IEC 61400-15-1:2025, *Site suitability input conditions for wind power plants*.  
   https://webstore.iec.ch/en/publication/29169
5. Drobinski, P. (2026), *Assessing renewable wind and solar energy yield with gridded climate datasets*.  
   https://doi.org/10.1038/s44168-025-00332-4
