# 资料索引与来源记录

这个目录不再保存论文PDF全文。正文中已经核验过的论文、技术报告和官方页面继续通过DOI、官方链接和元数据保留，便于后续回查来源；需要阅读全文时再从正式来源获取。

## 目录

```text
08_library/
├─ reports/     少量官方网页快照
├─ metadata/    历史下载记录与当前文件清单
└─ README.md    资料索引与阅读线索
```

`papers/`不再承担本地PDF归档功能。

## 论文与报告索引

| 来源 | 主题 | 对应问题 |
|---|---|---|
| Swart et al. (2019), CanESM5 | CanESM5模型说明 | 理解CanESM5定位、分辨率和CMIP6背景 |
| O'Neill et al. (2016), ScenarioMIP | SSP情景与CMIP6实验设计 | 理解未来情景与气候投影 |
| Pronk et al. (2022) | ERA5与WRF风资源比较 | 区分再分析与中尺度模型的角色 |
| Lee & Fields (2021) | 发电量偏差、损失与不确定性 | 理解AEP、损失项和不确定性 |
| Haupt et al. (2023) | 中尺度—微尺度耦合 | WRF/LES/CFD耦合接口 |
| Kosović et al. (2026) | ABL湍流、功率与载荷 | 湍流与风机运行环境 |
| Agarwal & Lundquist (2026) | 复杂地形稳定度 | 稳定度指标、测量高度与空间代表性 |
| Barber et al. (2022) | 复杂地形WRA误差 | 风速误差如何继续传到AEP |
| Porté-Agel et al. (2020) | 风机与风场流动 | ABL、尾流、RANS/LES |
| Zhou & Esau (2026) | 风速样本长度 | 长期代表性与统计收敛 |
| Hammond & Simley (2026) | 建设前AEP偏差、P50/P90 | 工程能量评估与风险 |
| Drobinski (2026) | 网格化气象数据到能源产量 | 贯通资源、AEP、P50/P90和气候风险 |
| Borowski et al. (2026) | 气候模式进入WRA | 跟踪未来风资源评估的新方法，当前为预印本 |
| Blaabjerg et al. (2024) | 风电电力电子与并网控制 | Type-3/Type-4、变流器、grid code与系统支撑 |
| Pandit et al. (2023) | SCADA状态与性能监测 | SCADA、故障检测、性能监测与O&M |
| Skamarock et al. (2019) | WRF ARW技术说明 | WRF方程、数值方法、嵌套与物理方案 |

完整DOI、官方链接及各来源用于核验的具体事实见根目录[SOURCES.md](../SOURCES.md)和[07_resources](../07_resources/README.md)。

## 保留的网页资料

`reports/`当前只保留少量网页快照，用于记录公开方法或官方版本信息：

- `Global_Wind_Atlas_Method.html`
- `NCAR_WRF_Technical_Description.html`
- `IEC_61400_15_1_2025_official_page.html`

IEC标准正文仍受版权和购买许可约束，本仓库只保留官方入口和必要的范围说明。

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

## 元数据

`metadata/download_log.json`保留前期资料核验阶段的历史下载记录，包括URL、文件大小和SHA-256。对应PDF已经删除，该文件只作为来源追溯记录。

`metadata/inventory.json`记录当前仍实际存在于`08_library`中的文件，不再包含已删除PDF。
