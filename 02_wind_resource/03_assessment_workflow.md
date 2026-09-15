# 风资源评估的完整链条

风资源评估的最终目标是把有限的现场信息转化为具有长期代表性的风况描述，并进一步支撑机组选型、发电量估计和项目风险判断。工程实践通常会把测量、长期订正、垂直外推、空间流场建模和不确定性分析串成一条连续链路。

## 1. 从现场测量开始

现场数据通常来自测风塔、激光雷达或其他遥感设备。进入后续分析前，需要确认测量高度、采样频率、缺测率、仪器变化、周围障碍物和数据质量控制规则。

测量数据的价值在于直接对应具体场址，但测量周期往往短于项目需要的长期气候尺度。IEC 61400-15-1:2025把长期气象和风流特征的定义、测量与预测纳入风电场场址适宜性评价框架，说明长期代表性本身就是正式工程评价的一部分。

## 2. 长期参考与MCP

短期现场观测通常需要和长期参考序列结合。参考资料可以来自长期气象站、ERA5等再分析资料，或经过验证的中尺度模拟产品。

Measure-Correlate-Predict（MCP）的基本结构是：

$$
V_{site}=F(V_{ref},\mathbf z)+\varepsilon,
$$

其中$V_{site}$表示现场风况，$V_{ref}$表示长期参考序列，$\mathbf z$可以包含风向、季节或其他辅助变量。

MCP的关键在于重叠时段建立的关系能否在更长时间尺度上保持稳定。短期样本、异常年份和参考资料偏差都会影响长期订正结果。

Zhou和Esau在2026年的Wind Energy Science研究进一步说明，风速均值、标准差和Weibull参数对样本量的要求不同，连续观测时段是否覆盖年际、季节和日变化也会影响结论。因此，“有一年数据”和“已经充分描述长期风资源”需要分开判断。

## 3. 高度转换与轮毂高度风况

测量高度往往低于风机轮毂高度，需要进行垂直外推。幂律和对数律都可以作为近似表达，但实际垂直风廓线受到粗糙度、大气稳定度、地形和天气过程影响。

在复杂场址中，垂直外推的不确定性会直接进入后续发电量估计。Lee和Fields对风能产量预测不确定性的综述中，将风速测量、垂直外推、空气密度、流场模型等都列为能量评估中的不确定性来源。ABL状态、稳定度和湍流的进一步说明见[大气边界层、稳定度与湍流](04_boundary_layer_stability_turbulence.md)。

## 4. 从点到场

单个测量点不足以直接描述整个风电场。空间外推需要处理：

- 地形高程；
- 地表粗糙度；
- 障碍物；
- 大气稳定度；
- 风向变化；
- 海陆边界或复杂地形效应。

平坦或简单地形中，再分析资料和中尺度模型都可能提供有用信息。Pronk等在2022年的研究中比较了ERA5和WRF：在所研究的简单地形与海上场景中，WRF的平均偏差较小，而ERA5在中心化RMSE和相关系数上表现更好。这个结果说明模型选择应围绕具体评价指标和场址条件展开。

复杂地形下通常还需要更高分辨率的流场模型，例如WAsP或CFD。

## 5. 中尺度到微尺度

当WRF等中尺度模型继续向CFD或LES传递信息时，问题会从“提高分辨率”转向“如何传递尺度信息”。

Haupt等对DOE Atmosphere to Electrons中微尺度耦合工作的总结指出，耦合中需要处理：

- 中尺度与微尺度方程和物理假设不同；
- 约100 m到边界层深度之间存在尺度灰区；
- 微尺度湍流需要合理初始化；
- 地表条件在不同尺度上的表达方式不同；
- 外部耦合需要确定边界与强迫信息的传递方式。

该研究还发现，表现最好的中尺度配置并不一定产生表现最好的微尺度结果。因此，每个尺度都需要单独验证。

## 6. 从风况到工程输出

一条典型链路可以概括为：

$$
\text{现场测量}
\rightarrow
\text{长期订正}
\rightarrow
\text{轮毂高度风况}
\rightarrow
\text{空间流场}
\rightarrow
\text{风机功率}
\rightarrow
\text{AEP与不确定性}.
$$

每一步都会引入新的假设和误差来源。工程上的可追溯性要求记录数据来源、参数、损失项和不确定性传播方式。

## 参考资料

1. IEC 61400-15-1:2025, *Site suitability input conditions for wind power plants*.  
   https://webstore.iec.ch/en/publication/29169
2. Zhou, L. and Esau, I. (2026), *Determining the ideal length of wind speed series for wind speed distribution and resource assessment*.  
   https://doi.org/10.5194/wes-11-217-2026
3. Pronk, V. et al. (2022), *Can reanalysis products outperform mesoscale numerical weather prediction models in modeling the wind resource in simple terrain?*  
   https://doi.org/10.5194/wes-7-487-2022
4. Lee, J. C. Y. and Fields, M. J. (2021), *An overview of wind-energy-production prediction bias, losses, and uncertainties*.  
   https://doi.org/10.5194/wes-6-311-2021
5. Haupt, S. E. et al. (2023), *Lessons learned in coupling atmospheric models across scales for onshore and offshore wind energy*.  
   https://doi.org/10.5194/wes-8-1251-2023
6. Drobinski, P. (2026), *Assessing renewable wind and solar energy yield with gridded climate datasets*.  
   https://doi.org/10.1038/s44168-025-00332-4
