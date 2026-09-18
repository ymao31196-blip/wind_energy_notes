# 不确定性如何传到AEP

风资源评估中的不确定性来自多个环节。最终年发电量（Annual Energy Production, AEP）分布取决于这些误差如何沿“测量—长期订正—空间外推—功率转换—损失模型”逐级传递。

## 1. 不确定性来源

常见来源可以按链路位置分组：

| 环节 | 典型不确定性 |
|---|---|
| 测量 | 仪器误差、缺测、安装与代表性 |
| 长期订正 | MCP关系、参考资料偏差、年际变化 |
| 垂直外推 | 风切变、稳定度、轮毂高度差异 |
| 空间外推 | 地形、粗糙度、流场模型 |
| 风机与风场 | 功率曲线、尾流、可利用率 |
| 系统与运行 | 电气损失、限电、环境停机 |

不同来源之间可能存在相关性。例如稳定度会同时影响风切变、湍流和尾流恢复，不能总把这些误差当成相互独立。

## 2. 线性误差传播

对于一个由多个变量决定的量

```math
Y=f(x_1,x_2,\ldots,x_n),
```

在小扰动、近线性且误差独立的条件下，可以用一阶近似：

```math
\sigma_Y^2
\approx
\sum_i
\left(
\frac{\partial f}{\partial x_i}
\right)^2
\sigma_{x_i}^2.
```

如果变量之间存在协方差，还需要加入交叉项：

```math
\sigma_Y^2
\approx
\mathbf J
\mathbf\Sigma
\mathbf J^\mathsf T,
```

其中$`\mathbf J`$是由各输入偏导数组成的局部敏感度，$`\mathbf\Sigma`$是输入协方差矩阵。对角线元素对应各输入的方差，非对角线元素描述两个不确定输入是否会一起偏大或一起偏小；这些相关性会改变最终不确定度。

风电链路包含非线性功率曲线、阈值和损失模型，一阶近似只能在局部条件下使用。

## 3. Monte Carlo传播

更通用的做法是为不确定输入指定分布，反复抽样并重新计算完整链路。若输入之间已知存在相关性，抽样时也要保留这种相关结构，不能把所有变量都独立随机化：

```math
\mathbf x^{(k)}
\sim
p(\mathbf x),
```

```math
AEP^{(k)}
=
F(\mathbf x^{(k)}).
```

经过大量样本后，可以直接得到AEP经验分布。P50和P90等量来自这个分布，而非单独添加在最终AEP上的固定百分比。

如果P90定义为“有90%概率被超过的发电量”，它对应AEP分布的较低分位位置。

## 4. 自然变率与知识不确定性

长期AEP变化中至少要区分两类来源：

**自然变率**来自真实气候和天气过程，例如年际风况变化。

**知识不确定性**来自测量有限、模型近似、外推方法和参数估计。

这两类变化都会让年度发电量形成分布，但含义不同。自然变率无法通过换一个模型消除；知识不确定性可以通过更长测量、更好的模型和验证逐步降低。

## 5. 复杂地形中的传播

Barber等（2022）在五个复杂地形场址比较多个风资源评估（Wind Resource Assessment, WRA）工作流时发现，局地风速预测误差不会直接、线性地转换为AEP误差。风向频率、垂直外推、长期外推和功率计算方式都会改变最终结果。

因此，只比较风速RMSE无法完整描述项目风险。评价还要看误差进入功率曲线和长期频率分布后的结果。

## 6. P50/P90的校验

Hammond和Simley（2026）使用实际风场运行结果检查建设前AEP预测，发现样本中的P50仍存在系统偏差，P90和不确定性估计也有改进空间。

这类研究说明，给出P50/P90并不等于不确定性已经处理充分。预测分布本身还需要用后验运行数据检验。

## 7. 与计算示例的关系

[Monte Carlo不确定性传播Notebook](../09_notebooks/04_uncertainty_propagation.ipynb)使用合成输入，把风速尺度、尾流损失、可利用率和电气损失作为随机变量，生成一个Net AEP代理分布。

示例只用于展示传播机制。输入分布是人为设定的，不代表任何具体项目的行业标准不确定度。

## 参考资料

1. Lee, J. C. Y. and Fields, M. J. (2021), *An overview of wind-energy-production prediction bias, losses, and uncertainties*.  
   https://doi.org/10.5194/wes-6-311-2021
2. Barber, S. et al. (2022), *The wide range of factors contributing to wind resource assessment accuracy in complex terrain*.  
   https://doi.org/10.5194/wes-7-1503-2022
3. Hammond, R. and Simley, E. (2026), *Biases in preconstruction estimates of wind plant annual energy production*.  
   https://doi.org/10.5194/wes-11-1251-2026
4. Drobinski, P. (2026), *Assessing renewable wind and solar energy yield with gridded climate datasets*.  
   https://doi.org/10.1038/s44168-025-00332-4
