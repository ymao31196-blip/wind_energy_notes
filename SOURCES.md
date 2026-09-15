# Source Notes｜资料来源与核验记录

本文件记录初版资料的主要事实来源。原则是：基础定义优先引用官方机构和同行评议论文；GitHub社区项目用于学习工作流、代码组织和实践方法，不作为气象或工程基本定律的唯一依据。

核验日期：2026-09-15。

## A. 风机与风功率

### U.S. Department of Energy

- Wind Energy Basics  
  https://www.energy.gov/cmei/systems/wind-energy-basics
- How Do Wind Turbines Work?  
  https://www.energy.gov/cmei/systems/how-do-wind-turbines-work
- Enabling Wind Power Nationwide / Understanding Wind Energy  
  https://www.energy.gov/sites/prod/files/2015/05/f22/Enabling%20Wind%20Power%20Nationwide_18MAY2015_FINAL.pdf

用于核验：

- 风机通过叶片气动力驱动转子和发电机；
- 风中功率与$\rho A V^3/2$关系；
- 切入、额定与切出风速的基本概念；
- Betz上限的基本表述。

注意：具体切入/额定/切出风速依赖机型，仓库中只将DOE给出的典型范围作为示意，不作为统一参数。

## B. 容量因子与风资源

### NREL Annual Technology Baseline

https://atb.nrel.gov/electricity/2024b/land-based_wind

用于核验：

- CF不仅受资源水平影响，也受机组设计、轮毂高度、停机和损失影响。

### NREL Wind Resource Assessment

https://www.nrel.gov/docs/fy14osti/60429.pdf

用于核验：

- 风速分布常以Weibull参数描述；
- 平均风速不足以描述完整风资源。

## C. ERA5

### ECMWF ERA5 dataset description

https://www.ecmwf.int/en/forecasts/datasets/complete-era5-global-atmospheric-reanalysis

用于核验：

- ERA5为ECMWF第五代再分析；
- 当前覆盖1940年至今；
- 大气网格约31 km；
- 提供大量逐小时变量。

### ECMWF u/v wind calculation

https://confluence.ecmwf.int/spaces/CKB/pages/133262398/

用于核验：

$$
|\mathbf V|=\sqrt{u^2+v^2}
$$

以及气象风向定义与普通数学极坐标约定的差异。

### Hersbach et al. (2020)

https://doi.org/10.1002/qj.3803

用于理解再分析的科学定义：再分析通过数值模式与数据同化整合历史观测，形成时空连续的大气状态估计。

## D. WRF与多尺度风资源

### NCAR WRF Model Users Site

https://www2.mmm.ucar.edu/wrf/users/

### WRF Users Guide

https://www2.mmm.ucar.edu/wrf/users/wrf_users_guide/build/html/index.html

用于核验：

- WRF是面向研究和数值天气预报的大气模拟系统；
- WRF包含WPS、初始化、ARW求解器、WRFDA等组件；
- WPS处理模拟区域、地形/土地利用和外部气象资料。

### Global Wind Atlas Method

https://globalwindatlas.info/about/method

用于核验：

- GWA采用大尺度→中尺度→微尺度路线；
- 当前公开方法以ERA5驱动WRF，再进入微尺度风图谱计算；
- 中尺度与微尺度耦合前需要generalization避免尺度效应重复计入。

## E. CanESM5与未来情景

### Swart et al. (2019)

https://doi.org/10.5194/gmd-12-4823-2019

用于核验CanESM5的模型定位及其对CMIP6的贡献。

### O'Neill et al. (2016)

https://doi.org/10.5194/gmd-9-3461-2016

用于核验ScenarioMIP的情景设计思想。未来情景模拟用于研究不同社会经济/排放路径下的气候投影，不提供未来天气的逐时逐月确定性预报。

## F. 社区项目

### Predicting the Wind

https://github.com/flrs/predicting_the_wind

README核验：项目以虚拟风场开发为场景，串联测量、气候/地面参考、长期风估计、风机功率和电网背景。

### VortexFDC/Pywind

https://github.com/VortexFDC/pywind

README核验：当前项目内容包含NetCDF读取、数据合并、MCP、大气稳定度、风切变和时空变率等。

### DTU Python4WindEnergy

https://github.com/DTUWindEnergy/Python4WindEnergy

README核验：DTU Wind Energy的Python教学资料仓库。

### NREL OpenOA

https://github.com/NREL/OpenOA

README核验：面向风电场运行评估，包含时序数据结构、AEP、尾流损失、功率曲线和气象数据处理等。

### IEA Task 43 awesome-wind

https://github.com/IEA-Task-43/awesome-wind

README核验：社区维护的风电开源软件资源列表，包括资源评估、尾流和仿真类工具。

## G. 个人案例事实源

案例材料严格来自本地重跑工程中冻结的最终事实源与最终小论文草稿：

- `08_reports/exp_018_final_small_paper/FINAL_FACT_SOURCE.md`
- `08_reports/exp_018_final_small_paper/small_paper_final_draft.md`

当前案例采用的关键冻结事实包括：

- B：未校正CanESM5主体基线；
- M1：偏ERA5历史参考恢复的直接映射；
- M2：`M2_no_temporal_controlled`；
- M2重构：$Y=B+0.30\Delta$；
- 最终M2不使用MOMENT；
- M1历史参考恢复最好；
- M2在指定$A\ge0.15$、$R_{min}\ge0.80$政策情景下为唯一可行候选；
- 三方法均为Pareto非支配点，不能宣称M2整体最优；
- SSP585只做结构迁移描述，不做未来准确度验证；
- CF只作为简化代理，不等同于真实风电场容量因子。

## H. 初版核验中主动避免的错误

1. 没有把ERA5写成“观测真值”；
2. 没有把SSP585写成未来逐月天气预测；
3. 没有把WRF和CFD写成彼此替代关系；
4. 没有把$P\propto V^3$直接当成真实风机全风速区功率曲线；
5. 没有把Betz极限写成整机效率；
6. 没有把月平均$u,v$合成的风速代理当成真实月平均标量风速；
7. 没有把案例中的CF代理写成实际风电场CF；
8. 没有把M2写成历史精度最优或未来更准确；
9. 没有把MOMENT消融结果推广为“时序信息无效”。

## I. 本轮补充的权威来源

### IEC 61400-15-1:2025

https://webstore.iec.ch/en/publication/29169

用于核验：

- 长期气象与风流特征属于场址适宜性评价的重要输入；
- 标准强调测量、预测、环境极值、设备与场址条件整合，以及过程可追溯性；
- 标准正文受版权保护，本仓库只保存官方产品页面，不保存受限全文。

### IEC 61400-12-1:2022

https://webstore.iec.ch/en/publication/68499

用于核验：

- 单机功率性能测量需要配套不确定性评估；
- 功率曲线和能量产出估计不能脱离测量与不确定性条件。

### Pronk et al. (2022)

https://doi.org/10.5194/wes-7-487-2022

用于核验：

- ERA5和WRF在风资源评估中的优势维度可能不同；
- 该研究的简单地形与海上案例中，WRF平均偏差较小，ERA5在中心化RMSE和相关系数上更好；
- 这个结果不推广为所有场址的一般排序。

### Lee and Fields (2021)

https://doi.org/10.5194/wes-6-311-2021

用于核验：

- 风电能量评估包含可利用率、尾流、电气、限电等多类损失；
- 风速测量、垂直外推、空气密度和模型误差会进入AEP不确定性；
- 工程能量评估需要同时记录损失和不确定性。

### Haupt et al. (2023)

https://doi.org/10.5194/wes-8-1251-2023

用于核验：

- 中尺度—微尺度耦合存在尺度灰区、边界强迫、湍流初始化和地表处理等问题；
- 最优中尺度配置未必对应最优微尺度结果；
- 多尺度耦合需要逐层验证。

### Zhou and Esau (2026)

https://doi.org/10.5194/wes-11-217-2026

用于核验：

- 样本长度对不同风速统计量的收敛影响不同；
- 一年观测可能仍不足以充分覆盖年际变化；
- 随机跨年采样与连续现场观测不能直接等价。

### Hammond and Simley (2026)

https://doi.org/10.5194/wes-11-1251-2026

用于核验：

- P50和P90用于建设前AEP风险表达；
- 实际运行数据可用于检验建设前AEP偏差和不确定性覆盖；
- P90的可靠性依赖损失与不确定性建模。

### Drobinski (2026)

https://doi.org/10.1038/s44168-025-00332-4

用于核验：

- 网格化再分析与气候模拟已经广泛用于可再生能源资源与产量评估；
- 从气象资源到能源产量还需经过垂直外推、空气密度、功率转换和不确定性处理；
- P50/P90和气候风险属于完整能量评估链中的下游量。

### Borowski et al. (2026)

https://doi.org/10.5194/wes-2026-129

状态：Wind Energy Science Discussions预印本，当前仍在同行评议。

用于跟踪气候模式集成到长期风资源评估中的最新方法思路，不作为已经定型的标准或共识。

## J. ABL、复杂地形与尾流补充来源

### Kosović et al. (2026)

https://doi.org/10.5194/wes-11-509-2026

用于核验：

- 风能利用发生在大气边界层内；
- 风资源常用轮毂高度风速、风向、风切变、湍流强度及其变化描述；
- 湍流会影响功率波动、气动载荷和疲劳寿命；
- 稳定度通过浮力与机械剪切改变边界层湍流结构。

### Agarwal and Lundquist (2026)

https://doi.org/10.5194/wes-11-883-2026

用于核验：

- 复杂地形中的稳定度具有明显空间差异；
- Perdigão数据表明，10 min Reynolds分解窗口会低估部分湍流结构；
- 10 m高度稳定度测量不能可靠代表100 m轮毂高度状态；
- 稳定度可通过Obukhov长度、湍流动能等不同量表征。

### Barber et al. (2022)

https://doi.org/10.5194/wes-7-1503-2022

用于核验：

- 研究比较五个复杂地形场址上的七种WRA工作流；
- 局地风速预测误差与AEP误差之间不存在简单线性映射；
- 风向频率、垂直外推、长期外推、功率曲线和损失模型共同影响最终AEP；
- 复杂地形模型评价需要从风速验证继续追踪到能量产出层。

### Porté-Agel et al. (2020)

https://doi.org/10.1007/s10546-019-00473-0

用于核验：

- 风机和风场流动与湍流大气边界层存在多尺度双向耦合；
- 尾流中的速度亏损会造成发电损失，增强湍流会增加疲劳载荷；
- 工程尾流模型、RANS和LES覆盖不同的精度—计算成本区间；
- ABL湍流、稳定度和地表异质性会改变尾流演化。

## K. 风机控制、电力电子与SCADA补充来源

### Blaabjerg et al. (2024)

https://doi.org/10.1038/s44287-024-00032-x

用于核验：

- 现代风电机组由风轮、发电机和并网变流器共同完成风能到电能的转换；
- Type-3 DFIG通过部分功率变流器连接转子，Type-4机组采用全功率变流器；
- 机侧控制与转速、转矩和最大功率追踪相关，网侧控制负责直流母线、电流、无功功率和并网点电压；
- 典型grid code涉及有功/频率响应、电压与无功支撑、故障穿越、电能质量、保护和通信；
- 高比例电力电子电源条件下，grid-forming和频率支撑成为风电并网的重要研究方向。

前期核验使用了Aalborg University门户公开的submitted manuscript。门户页面标注CC BY-NC 4.0，作者稿首页同时保留门户使用限制说明；仓库保留该作者稿用于来源追溯，其版权与再使用条件仍以原文件和出版方页面为准。

### Pandit et al. (2023)

https://doi.org/10.1177/0309524X221124031

用于核验：

- SCADA数据广泛用于风机状态监测、性能监测和O&M决策；
- 研究中常见10 min聚合SCADA，高频数据保留更多动态信息但增加存储和计算负担；
- SCADA状态监测常见任务包括异常检测、功率曲线监测、故障分类和正常行为建模；
- 数据驱动监测流程包括数据收集、特征构造、模型选择、验证和决策；
- SCADA与振动、应变、电流等更高频状态监测数据具有不同信息尺度。

### Jonkman et al. (2009)

https://www.nrel.gov/docs/fy09osti/38060.pdf

用于核验：

- NREL 5 MW基准机组采用变速、变桨到顺桨的典型控制结构；
- 额定以下主要使用发电机转矩控制，目标是高效捕获风能；
- 额定以上主要使用集体变桨调节发电机转速和功率。

