# 资料索引与来源记录

这个目录同时保存已经核验过的公开论文/技术报告PDF，以及DOI、官方链接和来源元数据，便于在阅读正文时直接回查原始资料。

## 目录

```text
08_library/
├─ papers/       论文与综述PDF
├─ reports/      技术报告PDF与少量官方网页快照
├─ metadata/     下载记录与当前文件清单
└─ README.md     资料索引与阅读线索
```

## 已收录PDF

| 文件 | 主题 |
|---|---|
| `2016_ONeill_ScenarioMIP_CMIP6_GMD.pdf` | ScenarioMIP与SSP情景 |
| `2019_Swart_CanESM5_GMD.pdf` | CanESM5模型说明 |
| `2020_PorteAgel_Wind_Turbine_Farm_Flows_Review_BLM.pdf` | 风机与风场流动综述 |
| `2020_WRF_CFD_Coupling_Uncertainty_WES.pdf` | WRF–CFD耦合不确定性 |
| `2021_Lee_Fields_WindEnergyPredictionBias_Uncertainty_WES.pdf` | 发电量偏差、损失与不确定性 |
| `2022_Barber_Complex_Terrain_WRA_Accuracy_WES.pdf` | 复杂地形WRA误差 |
| `2022_Pronk_ERA5_vs_WRF_WindResource_WES.pdf` | ERA5与WRF风资源比较 |
| `2023_Haupt_Mesoscale_Microscale_Coupling_WES.pdf` | 中尺度—微尺度耦合 |
| `2023_Pandit_SCADA_Condition_Performance_Monitoring_Review.pdf` | SCADA状态与性能监测 |
| `2024_Blaabjerg_Power_Electronics_Wind_Generation_DRAFT.pdf` | 风电电力电子与并网控制 |
| `2026_Agarwal_Lundquist_Atmospheric_Stability_Complex_Terrain_WES.pdf` | 复杂地形稳定度 |
| `2026_Borowski_ClimateModel_Integration_WRA_PREPRINT.pdf` | 气候模式进入WRA，当前为预印本 |
| `2026_Drobinski_GriddedClimateDatasets_RenewableYield_npj.pdf` | 网格化气象数据到能源产量 |
| `2026_Hammond_Simley_Preconstruction_AEP_Bias_WES.pdf` | 建设前AEP偏差与P50/P90 |
| `2026_Kosovic_Atmospheric_Turbulence_Wind_Turbines_WES.pdf` | ABL湍流、功率与载荷 |
| `2026_Zhou_Esau_WindSpeedSeriesLength_WES.pdf` | 风速样本长度与长期代表性 |
| `reports/2019_Skamarock_WRF_ARW_v4_TechnicalNote.pdf` | WRF ARW技术说明 |

完整DOI、官方链接及各来源用于核验的具体事实见根目录[SOURCES.md](../SOURCES.md)和[07_resources](../07_resources/README.md)。

## 网页资料

`reports/`还保留少量网页快照，用于记录公开方法或官方版本信息：

- `Global_Wind_Atlas_Method.html`
- `NCAR_WRF_Technical_Description.html`
- `IEC_61400_15_1_2025_official_page.html`

IEC标准正文仍受版权和购买许可约束，本仓库只保留官方入口和必要的范围说明，不保存标准全文。

## 阅读线索

资料可按下面的关系串联：

1. Drobinski：先看网格化气象数据如何贯通资源、能量和风险；
2. Kosović：建立ABL、风切变、稳定度、湍流与风机运行之间的联系；
3. Pronk：理解ERA5和WRF在风资源中的角色；
4. Haupt：进入中尺度—微尺度耦合；
5. Agarwal、Barber：继续看复杂地形中的稳定度和WRA误差传播；
6. Porté-Agel：系统梳理风机尾流、风场流动和ABL耦合；
7. Lee、Hammond：进入损失、不确定性与P50/P90；
8. Blaabjerg：从机组控制继续进入发电机、变流器和并网支撑；
9. Pandit：看机组投运后的SCADA、性能监测和故障诊断；
10. Swart、O'Neill：理解案例中的CanESM5和SSP585；
11. Borowski：跟踪气候模式进入长期WRA的最新研究，并保留其预印本状态。

## 来源与再使用

这些PDF来自开放获取论文、作者公开稿或公开技术报告。每份文件的版权与再使用条件以原文件和出版方页面为准；本目录保留原始文件名、来源链接和校验信息，便于追溯。

`metadata/download_log.json`保留下载URL、文件大小和SHA-256等历史记录；`metadata/inventory.json`记录当前实际存在于`08_library`中的文件。
