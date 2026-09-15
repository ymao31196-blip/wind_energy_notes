# 复杂地形与风机尾流

复杂地形和风机尾流都属于微尺度风场问题，但二者来源不同。地形通过几何、粗糙度和热力差异改变来流，风机则通过动量提取和湍流生成改变下游流场。真实风电场中，两类效应会叠加。

## 1. 地形如何改变风场

山脊、坡面和谷地会改变局地压力分布和流动路径。常见现象包括：

- 山脊和收缩区域的流动加速；
- 背风坡分离和回流；
- 谷地通道效应；
- 不同风向下完全不同的流场结构；
- 粗糙度突变和森林对近地层风的修改；
- 稳定度与地形共同作用形成的局地环流。

局地加速可以用相对参考点的speed-up ratio表示：

```math
S
=
\frac{U_{site}-U_{ref}}{U_{ref}}.
```

这个量依赖参考位置、风向、高度和气象状态，本身不提供场址长期AEP。

## 2. 复杂地形评估是一条工作流

Barber等（2022）比较了五个复杂地形场址上的七种风资源评估工作流。研究从风速误差继续追踪到AEP，结果显示风速预测精度与AEP精度之间没有简单线性关系。

从风场模拟到AEP还要经过：

```math
\text{风向分扇区}
\rightarrow
\text{风速频率分布}
\rightarrow
\text{垂直外推}
\rightarrow
\text{长期外推}
\rightarrow
\text{功率曲线}
\rightarrow
\text{AEP}.
```

如果进入实际风电场，还要继续加入尾流和其他损失项。

这意味着复杂地形模型的评价对象不能只停留在某个方向、某个时刻的风速误差。模型在局地风速上更接近观测，并不自动保证最终AEP误差更小。

## 3. 风机尾流

风机从来流中提取动量后，下游形成低速、高湍流区域。可以用归一化速度亏损描述：

```math
\frac{\Delta U}{U_\infty}
=
\frac{U_\infty-U_{wake}}{U_\infty},
```

其中$`U_\infty`$表示未受尾流影响的来流，$`U_{wake}`$表示尾流区域风速。

尾流具有两个工程后果：

- 下游风机可利用风速降低，形成发电损失；
- 湍流增强，使下游风机承受更复杂的疲劳载荷。

Porté-Agel等（2020）的综述指出，尾流演化受到大气边界层湍流、稳定度、地表异质性和风机运行状态共同影响。

## 4. 尾流模型的层级

不同任务对应不同模型复杂度。

**工程尾流模型**计算速度亏损和尾流扩张，计算代价低，适用于风场布局优化、快速AEP计算和大量工况扫描。

**RANS**通过平均流方程和湍流闭合描述尾流，能够处理更复杂的地形和边界条件，计算成本高于工程模型。

**LES**显式解析主要大尺度湍流结构，可研究尾流摆动、尾流相互作用和ABL耦合，计算成本进一步上升。

模型复杂度增加会带来更多可解析物理过程，也增加入口条件、网格、湍流参数化和计算资源要求。

## 5. 稳定度、湍流与尾流恢复

环境湍流控制尾流和周围高速流体的混合速率。一般情况下：

- 较强湍流促进动量交换，尾流恢复更快；
- 稳定分层抑制垂直混合，尾流影响距离可能增加；
- 不稳定边界层中的热力湍流会增强混合；
- 风切变和风向切变会改变尾流形态和偏移。

复杂地形进一步改变这些关系。山脊加速、流动分离和地形产生的湍流会与风机尾流同时存在。

## 6. WRF—CFD—尾流链条

对于大区域复杂场址，可将模型链写成

```math
\text{ERA5或预报场}
\rightarrow
\text{WRF}
\rightarrow
\text{复杂地形CFD/LES}
\rightarrow
\text{风机尾流}
\rightarrow
\text{AEP与载荷}.
```

接口处至少要核对：

- 风向和风速廓线；
- 大气稳定度；
- 湍流强度或湍流动能；
- 地表粗糙度与地形；
- 模型分辨率和尺度重叠；
- 风机参数化方式。

WRF输出的高分辨率背景场不能直接等同于风机入口条件。进入微尺度和尾流阶段后，仍要处理地形解析、湍流生成和风机动量提取。

## 7. 验证对象

复杂地形和尾流研究常用多层验证：

- 测风塔或Lidar的风速、风向和风廓线；
- 湍流强度或湍流统计量；
- 不同风向扇区下的速度加速/亏损；
- 风机SCADA功率；
- 风场总功率和尾流损失；
- 长期AEP。

Barber等（2022）的结果尤其说明，局地风速验证和项目AEP验证属于不同层级，需要分别保留。

## 参考资料

1. Barber, S. et al. (2022), *The wide range of factors contributing to wind resource assessment accuracy in complex terrain*.  
   https://doi.org/10.5194/wes-7-1503-2022
2. Porté-Agel, F., Bastankhah, M., and Shamsoddin, S. (2020), *Wind-Turbine and Wind-Farm Flows: A Review*.  
   https://doi.org/10.1007/s10546-019-00473-0
3. Haupt, S. E. et al. (2023), *Lessons learned in coupling atmospheric models across scales for onshore and offshore wind energy*.  
   https://doi.org/10.5194/wes-8-1251-2023
4. Agarwal, N. J. and Lundquist, J. K. (2026), *Characterizing atmospheric stability in complex terrain*.  
   https://doi.org/10.5194/wes-11-883-2026
