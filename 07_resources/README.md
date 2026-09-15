# 工具、项目与进一步阅读

这一页汇总当前使用频率较高的官方资料、论文和开源项目，并按它们在研究链中的作用分类。

## 1. 官方与基础资料

### U.S. Department of Energy：Wind Energy Basics

内容覆盖风机能量转换、主要部件和基础功率概念。

https://www.energy.gov/cmei/systems/wind-energy-basics

### Global Wind Atlas

提供风资源空间分布浏览，并公开“再分析→中尺度→微尺度”的多尺度建模方法。

主页：  
https://globalwindatlas.info/

方法：  
https://globalwindatlas.info/about/method

### ECMWF ERA5

提供ERA5再分析资料说明、10 m风分量定义和历史气象数据入口。

https://www.ecmwf.int/en/forecasts/datasets/complete-era5-global-atmospheric-reanalysis

### NCAR WRF

WRF官方用户网站和用户指南。

https://www2.mmm.ucar.edu/wrf/users/

https://www2.mmm.ucar.edu/wrf/users/wrf_users_guide/build/html/index.html

## 2. GitHub项目

### Predicting the Wind

https://github.com/flrs/predicting_the_wind

以虚拟风场开发场景串联测风、长期风估计、风机功率和电网背景，结构接近完整的问题链。

### Pywind

https://github.com/VortexFDC/pywind

Vortex团队维护的风数据分析项目。当前内容包括NetCDF读取、数据合并、基础统计图、MCP、大气稳定度、风切变和时空变率。

仓库中的Notebook组织和风数据处理可以参考这一项目的任务式结构。

### Python4WindEnergy

https://github.com/DTUWindEnergy/Python4WindEnergy

DTU Wind Energy整理的Python教学材料。项目年代较早，但“课程资料+Notebook”的组织形式仍然值得参考。

### OpenOA

https://github.com/NREL/OpenOA

NREL主导的风电场运行评估框架，覆盖：

- SCADA与风场运行数据；
- 数据质量控制；
- 功率曲线；
- AEP；
- 尾流损失；
- 不确定性分析。

它主要面向真实风电场运行评估，与本仓库中的气候模式精细化案例形成互补。

### IEA Task 43 awesome-wind

https://github.com/IEA-Task-43/awesome-wind

风电开源工具索引。当前按资源评估、尾流与仿真等方向整理了OpenOA、brightwind、FLORIS、PyWake等项目。

## 3. 气候与案例相关论文

### ERA5

Hersbach, H. et al. (2020). *The ERA5 global reanalysis*. Quarterly Journal of the Royal Meteorological Society.

https://doi.org/10.1002/qj.3803

### CanESM5

Swart, N. C. et al. (2019). *The Canadian Earth System Model version 5 (CanESM5.0.3)*. Geoscientific Model Development.

https://doi.org/10.5194/gmd-12-4823-2019

### ScenarioMIP

O'Neill, B. C. et al. (2016). *The Scenario Model Intercomparison Project (ScenarioMIP) for CMIP6*. Geoscientific Model Development.

https://doi.org/10.5194/gmd-9-3461-2016

## 4. 风资源与工程评估关键论文

### ERA5与WRF风资源比较

Pronk, V. et al. (2022). *Can reanalysis products outperform mesoscale numerical weather prediction models in modeling the wind resource in simple terrain?* Wind Energy Science.

https://doi.org/10.5194/wes-7-487-2022

文中直接比较ERA5与WRF在简单地形和海上场景中的风资源表现，可用于区分平均偏差、中心化RMSE和相关性等不同评价维度。

### 发电量偏差、损失与不确定性

Lee, J. C. Y. and Fields, M. J. (2021). *An overview of wind-energy-production prediction bias, losses, and uncertainties*. Wind Energy Science.

https://doi.org/10.5194/wes-6-311-2021

综述系统整理Gross/Net AEP、尾流损失、可利用率、电气损失、限电和不确定性在真实风电项目评估中的位置。

### 中尺度—微尺度耦合

Haupt, S. E. et al. (2023). *Lessons learned in coupling atmospheric models across scales for onshore and offshore wind energy*. Wind Energy Science.

https://doi.org/10.5194/wes-8-1251-2023

这篇来自DOE Atmosphere to Electrons中微尺度耦合工作，覆盖尺度灰区、边界强迫、湍流初始化、内外部耦合和验证问题。

### 大气边界层湍流与风机载荷

Kosović, B. et al. (2026). *Impact of atmospheric turbulence on performance and loads of wind turbines: knowledge gaps and research challenges*. Wind Energy Science.

https://doi.org/10.5194/wes-11-509-2026

综述从大气边界层出发讨论风切变、稳定度、湍流尺度、功率波动和风机载荷，连接风资源气象与风机运行环境。

### 复杂地形中的大气稳定度

Agarwal, N. J. and Lundquist, J. K. (2026). *Characterizing atmospheric stability in complex terrain*. Wind Energy Science.

https://doi.org/10.5194/wes-11-883-2026

研究基于Perdigão试验47座气象塔比较稳定度表征方法，并检查低高度、少测点和时间平均窗口对轮毂高度稳定度判断的影响。

### 复杂地形风资源评估误差

Barber, S. et al. (2022). *The wide range of factors contributing to wind resource assessment accuracy in complex terrain*. Wind Energy Science.

https://doi.org/10.5194/wes-7-1503-2022

研究比较五个复杂地形场址上的七套WRA工作流，从局地风速误差继续追踪到AEP，说明风速预测精度与最终AEP精度之间不存在简单线性映射。

### 风机与风场流动综述

Porté-Agel, F., Bastankhah, M., and Shamsoddin, S. (2020). *Wind-Turbine and Wind-Farm Flows: A Review*. Boundary-Layer Meteorology.

https://doi.org/10.1007/s10546-019-00473-0

综述系统连接大气边界层、风机尾流、风场流动、工程尾流模型、RANS和LES，是理解尾流与ABL耦合的主要入口之一。

### 风速样本长度与长期代表性

Zhou, L. and Esau, I. (2026). *Determining the ideal length of wind speed series for wind speed distribution and resource assessment*. Wind Energy Science.

https://doi.org/10.5194/wes-11-217-2026

用于理解短期测量、年际变化和统计量收敛之间的关系。

### P50/P90与建设前AEP偏差

Hammond, R. and Simley, E. (2026). *Biases in preconstruction estimates of wind plant annual energy production*. Wind Energy Science.

https://doi.org/10.5194/wes-11-1251-2026

研究将建设前AEP估计与实际运行结果对照，重点涉及P50/P90和预测不确定性。

### 网格化气象数据到能源产量

Drobinski, P. (2026). *Assessing renewable wind and solar energy yield with gridded climate datasets*. npj Climate Action.

https://doi.org/10.1038/s44168-025-00332-4

这篇开放获取综述把再分析、气候模拟、垂直外推、能量产出、P50/P90和气候风险放在同一条方法链中，在当前资料库中承担总览作用。

### 气候模式进入未来风资源评估

Borowski, J., Avila, K., and Dörenkämper, M. (2026). *Assessing Future Wind Speed Variations: Methodology for Climate Model Integration in Wind Resource Assessment*. Wind Energy Science Discussions.

https://doi.org/10.5194/wes-2026-129

当前仍处于同行评议阶段。它与CanESM5—ERA5案例方向接近，用于跟踪气候模式进入长期风资源评估的最新方法，不作为已经定型的方法标准。

## 5. 控制、电气与运行监测

### 风电系统中的电力电子

Blaabjerg, F., Chen, M., and Huang, L. (2024). *Power electronics in wind generation systems*. Nature Reviews Electrical Engineering.

https://doi.org/10.1038/s44287-024-00032-x

这篇综述从风轮、发电机和并网变流器继续延伸到Type-3/Type-4机组、机侧/网侧控制、故障穿越、无功支撑、频率响应以及grid-following/grid-forming等电气问题。

### SCADA运行与状态监测

Pandit, R. et al. (2023). *SCADA data for wind turbine data-driven condition/performance monitoring: A review on state-of-art, challenges and future trends*. Wind Engineering.

https://doi.org/10.1177/0309524X221124031

综述覆盖SCADA数据、功率性能监测、故障检测、正常行为模型、数据驱动诊断和维护决策，并讨论10 min聚合数据与高频数据之间的信息差异。

### NREL 5 MW基准风机

Jonkman, J. et al. (2009). *Definition of a 5-MW Reference Wind Turbine for Offshore System Development*. NREL/TP-500-38060.

https://www.nrel.gov/docs/fy09osti/38060.pdf

该技术报告给出经典的变速—变桨控制结构，常被用于OpenFAST和风机控制研究。

## 6. IEC标准入口

### IEC 61400-15-1:2025

风电场场址适宜性输入条件，包含长期气象和风流特征的定义、测量、预测与报告框架。

https://webstore.iec.ch/en/publication/29169

### IEC 61400-12-1:2022

单机功率性能测量方法，同时要求对不确定性来源及其综合影响进行评估。

https://webstore.iec.ch/en/publication/68499

IEC标准正文受版权和购买许可约束，本仓库只保留官方入口和必要的范围说明。

## 7. 资料索引

已经核验过的论文、官方技术资料和来源追溯记录见：

[08_library](../08_library/README.md)

已核验且纳入资料库的论文PDF和公开技术报告随仓库一并归档；DOI与官方页面仍作为来源追溯和版本核验入口。

## 8. 待扩展方向

现有主链已经覆盖长期风资源、ABL、复杂地形、尾流、AEP和不确定性。下一阶段可继续补充：

- 现场测量质量控制与IEC测量流程；
- 极端风况、设计条件与结构载荷；
- 海上边界层和海上风资源；
- 风场控制与尾流控制；
- WRF真实案例与参数化敏感性；
- 多源观测同化和数据融合；
- 风电功率预测；
- 风电场控制、虚拟电厂和电力系统应用。

新资源进入索引前，需要能对应到明确的数据、模型、评价或应用问题。
