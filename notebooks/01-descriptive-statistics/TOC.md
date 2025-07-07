
# Descriptive Statistics | 描述性统计

---

## TOC | 目录

- [Descriptive Statistics | 描述性统计](#descriptive-statistics--描述性统计)
  - [TOC | 目录](#toc--目录)
  - [What is 'Descriptive'? | 何为描述性](#what-is-descriptive--何为描述性)
  - [Typical descriptive method | 典型描述性方法](#typical-descriptive-method--典型描述性方法)
    - [Numerical Methods | 数值方法](#numerical-methods--数值方法)
    - [Graphical Methods | 图形方法](#graphical-methods--图形方法)
      - [Univariate Visualization | 单变量可视化​](#univariate-visualization--单变量可视化)
      - [Multivariate Visualization | 多变量可视化​](#multivariate-visualization--多变量可视化)
  - [Terminologies | 术语解释](#terminologies--术语解释)
  - [References | 参考文献](#references--参考文献)

---

## What is 'Descriptive'? | 何为描述性

描述性统计 中的 '描述性', 指的是该统计方法对数据集进行**概括性描述**的特点, 核心是通过简化的方式, 呈现数据的**基本特征**, 而不涉及对**总体参数推断**或者**概率判断**.

“描述性”的核心含义, 总结如下:

1. 用**数据特征**[^何为特征]对数据集整体进行总结概括
2. 呈现**现状**而非**推断**
3. 无**概率性陈述**

[^何为特征]: 什么是特征?
<!-- TODO:后续对名词进行详细解释 -->

'数据特征来概括' 指的是 用 少量关键指标, '代替' 原始数据.

'现状呈现而非推断' 指的是, 仅对当前的数据进行描述, 而不去预测未来或者推断总体

'无概率性陈述' 指的是, 不涉及 置信区间, 假设检验 等 概率计算.

> [!IMPORTANT]
> 可视化也属于描述统计.\
> 直方图, 散点图等 都是利用图形的方式 去 '描述' 数据特征.\
> 时间序列描述 同样属于描述性方法.

---

## Typical descriptive method | 典型描述性方法

提供以下几种描述的角度作为参考.

### Numerical Methods | 数值方法

1 **集中趋势 | Central Tendency**\
描述数据的 **集中趋势**. 反映数据的中心.\
常用指标: 均值, 中位数, 众数 等. Mean, Median, Mode, etc.

2 **离散程度 | Dispersion**\
描述数据的 **离散程度**. 体现数据的'波动大小'.\
常用指标: 方差, 标准差, 极差, 四分位距 等. Variance, Standard Deviation, Range, Interquartile Range (IQR), etc.

3 **分布形式 ​| ​Distribution Shape​**\
描述数据的 **分布形式**. 描述数据分布的对称性 和 尖锐程度.\
常用指标: 偏度, 峰度. Skewness, Kurtosis.

4 **关联性 | Association​**\
描述数据与数据之间的 **关联性**. 显示变量之间的线性关系强度.\
关键指标: 协方差, 相关系数. Covariance, Correlation Coefficient.

### Graphical Methods | 图形方法

通过数形补充数值无法直观呈现的信息. 可视化方法与数值方法并列, 能够对数值方法作进一步的补充, 同时描述数值方法.

提供一些常见的可视化方法:

<!-- TODO: 后续补充图表 -->

#### Univariate Visualization | 单变量可视化​

**单变量可视化 -> 描述 单变量的特征**

1 **直方图 | Histogram**\
展示数据分布形状与中心位置\
对应数值维度: 分布形态, 集中趋势.

2 **箱线图 | Box Plot​**\
五数概括: 最小值, Q1, 中位数, Q3, 最大值.\
对应数值维度: 离散程度, 异常值.

3 **密度曲线图 | Density Curve​**\
叠加在直方图上显示平滑分布.\
对应数值维度: 分布形态.

4 **饼图/条形图 | Pie Chart/Bar Chart​**\
展示分类数据的频率分布.\
对应数值维度: 集中趋势.

#### Multivariate Visualization | 多变量可视化​

**多变量可视化 -> 描述 多变量之间的关系**

1 **散点图 | Scatter Plot​**\
显示两连续变量的相关性与模式.\
对应数值维度: 关联性

2 **热力图 | Heatmap**\
用颜色矩阵展示相关系数强度.\
对应数值维度: 关联性

3 **分组箱线图 | Grouped Box Plot​**\
比较不同类别的数据分布差异.\
对应数值维度: 离散程度, 关联性

4 **气泡图 ​​| Bubble Chart​**\
用点大小表示第三个变量的值.\
对应数值维度: 关联性, 分布形态

[直方图](./histogram.ipynb)

---

## Terminologies | 术语解释

---

## References | 参考文献
[1]()
<!-- EOF -->