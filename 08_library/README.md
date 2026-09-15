# 本地资料库

这个目录保存当前阶段已经核验来源、并实际下载到本地的公开论文和技术资料，用于正文核验、后续阅读和方法回溯。

## 目录

```text
08_library/
├─ papers/      同行评议论文与明确标记的预印本
├─ reports/     官方技术说明、标准页面存档等
└─ metadata/    下载记录与校验信息
```

## 已下载论文

| 文件 | 主题 | 状态/许可 | 对应问题 |
|---|---|---|---|
| `2019_Swart_CanESM5_GMD.pdf` | CanESM5模型说明 | GMD，CC BY 4.0 | 理解CanESM5定位、分辨率和CMIP6背景 |
| `2016_ONeill_ScenarioMIP_CMIP6_GMD.pdf` | ScenarioMIP与SSP情景 | GMD，CC BY 3.0 | 理解未来情景与气候投影 |
| `2022_Pronk_ERA5_vs_WRF_WindResource_WES.pdf` | ERA5与WRF风资源表现比较 | WES，CC BY 4.0 | 理解再分析与中尺度模型的分工 |
| `2021_Lee_Fields_WindEnergyPredictionBias_Uncertainty_WES.pdf` | 发电量偏差、损失与不确定性综述 | WES，CC BY 4.0 | 理解AEP、损失项和不确定性 |
| `2023_Haupt_Mesoscale_Microscale_Coupling_WES.pdf` | 中尺度—微尺度耦合 | WES，CC BY 4.0 | WRF/LES/CFD耦合接口 |
| `2026_Kosovic_Atmospheric_Turbulence_Wind_Turbines_WES.pdf` | 大气边界层湍流、功率与载荷 | WES，CC BY 4.0 | ABL、湍流、风机运行环境 |
| `2026_Agarwal_Lundquist_Atmospheric_Stability_Complex_Terrain_WES.pdf` | 复杂地形中的大气稳定度 | WES，CC BY 4.0 | 稳定度指标、测量高度与空间代表性 |
| `2022_Barber_Complex_Terrain_WRA_Accuracy_WES.pdf` | 复杂地形WRA误差与AEP | WES，CC BY 4.0 | 风速误差如何传到AEP |
| `2020_PorteAgel_Wind_Turbine_Farm_Flows_Review_BLM.pdf` | 风机与风场流动综述 | Boundary-Layer Meteorology，CC BY 4.0 | ABL、尾流、RANS/LES与风场流动 |
| `2026_Zhou_Esau_WindSpeedSeriesLength_WES.pdf` | 风速样本长度与资源评估 | WES，CC BY 4.0 | 长期代表性和样本长度 |
| `2020_WRF_CFD_Coupling_Uncertainty_WES.pdf` | WRF–CFD耦合不确定性 | WES，CC BY 4.0 | 理解中微尺度接口和传递位置 |
| `2026_Hammond_Simley_Preconstruction_AEP_Bias_WES.pdf` | 建设前AEP偏差、P50/P90 | WES，CC BY 4.0 | 理解工程能量评估与风险 |
| `2026_Drobinski_GriddedClimateDatasets_RenewableYield_npj.pdf` | 网格化气象/气候数据到可再生能源产量 | npj Climate Action综述，CC BY 4.0 | 贯通资源、AEP、P50/P90和气候风险 |
| `2026_Borowski_ClimateModel_Integration_WRA_PREPRINT.pdf` | 气候模式融入长期风资源评估 | **预印本，同行评议中**，CC BY 4.0 | 跟踪气候模式与WRA结合的新方法 |
| `2024_Blaabjerg_Power_Electronics_Wind_Generation_DRAFT.pdf` | 风电电力电子与并网控制综述 | Nature Reviews Electrical Engineering作者稿，CC BY-NC 4.0 | Type-3/Type-4、变流器、grid code与系统支撑 |
| `2023_Pandit_SCADA_Condition_Performance_Monitoring_Review.pdf` | SCADA状态与性能监测综述 | Wind Engineering，CC BY 4.0 | SCADA、故障检测、性能监测与O&M |

## 已下载官方资料

| 文件 | 来源 | 用途 |
|---|---|---|
| `2019_Skamarock_WRF_ARW_v4_TechnicalNote.pdf` | NCAR | WRF方程、数值方法、边界条件、嵌套和物理方案 |
| `Global_Wind_Atlas_Method.html` | Global Wind Atlas | ERA5→WRF→微尺度的公开方法说明 |
| `NCAR_WRF_Technical_Description.html` | NCAR | WRF技术说明入口 |
| `IEC_61400_15_1_2025_official_page.html` | IEC | 记录IEC 61400-15-1:2025官方范围与版本信息 |

## 没有直接下载的关键来源

以下资料仍然保留在在线索引中，但本地不保存全文：

1. **IEC 61400系列正式标准全文**  
   标准正文受IEC版权和购买许可约束。当前只存官方产品页面，不复制受限全文。

2. **Pryor et al. (2020), Climate change impacts on wind power generation, Nature Reviews Earth & Environment**  
   该综述补充气候变化与风电的整体背景。当前正式页面为订阅内容，本地只保留正式链接。

3. **Jung & Schindler (2022), A review of recent studies on wind resource projections under climate change**  
   作为未来气候风资源综述保留在在线参考表中，是否归档PDF取决于最终许可核验。

## 阅读线索

资料可按下面的关系串联：

1. `2026_Drobinski...`：先看网格化气象数据如何贯通资源、能量和风险；
2. `2026_Kosovic...`：建立ABL、风切变、稳定度、湍流与风机运行之间的联系；
3. `2022_Pronk...`：理解ERA5和WRF在风资源中的角色；
4. `2023_Haupt...`：进入中尺度—微尺度耦合；
5. `2026_Agarwal_Lundquist...`与`2022_Barber...`：继续看复杂地形中的稳定度和WRA误差传播；
6. `2020_PorteAgel...`：系统梳理风机尾流、风场流动和ABL耦合；
7. `2021_Lee_Fields...`与`2026_Hammond...`：进入损失、不确定性、P50/P90和后验偏差；
8. `2024_Blaabjerg...`：从机组控制继续进入发电机、变流器和并网支撑；
9. `2023_Pandit...`：看机组投运后的SCADA、性能监测和故障诊断；
10. `2019_Swart...`与`2016_ONeill...`：理解案例中的CanESM5和SSP585；
11. `2026_Borowski...`：跟踪气候模式进入长期WRA的最新研究，保留其预印本状态标记。

## 发布到GitHub前

本地下载与公开再分发是两件事。Copernicus论文、Drobinski综述、Porté-Agel综述和Pandit综述已有明确Creative Commons许可。Blaabjerg作者稿页面标注CC BY-NC 4.0，同时文件首页保留作者门户的使用限制说明，因此当前只作为本地研究副本，不计划随Git仓库分发。其他资料在公开发布前仍逐项核验许可。

PDF会明显增大Git仓库体积。第一次commit前需要再决定：

- 将允许再分发的PDF直接纳入仓库；
- 或仅发布本README、DOI和官方链接，把PDF保留为本地资料库。

`metadata/download_log.json`保留首轮下载URL、文件大小、SHA-256和失败记录；`metadata/inventory.json`记录当前本地资料库的文件清单、大小、MIME类型和SHA-256。
