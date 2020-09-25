---
title: "Electrodynamics"
categories: "physics"
tags: 
date: 2020-09-25
---

# 磁化

磁荷未被观测到，物质内的原子中的电子在绕核旋转时形成电流，圈电流形成**磁矩**:
$$
\vec{m} = I\vec{S}
$$ 	
在无外场作用下，磁矩随机分布，宏观磁化强度为0，定义宏观中的磁化强度为：
$$
\vec{M} = \frac{\sum \vec{m}_i}{V}
$$ 
在外场作用下，磁矩会倾向转到与外场相同的方向，这时$\vec{M}$不为0，但是注意两点：

* 磁矩方向与外场不完全相同
* 磁化过程需要时间

# 磁场

* 磁场强度：$\vec{H}$ 
* 磁感应强度：$\vec{B}$ 
* 磁化强度：$\vec{M}$ 

满足关系$\vec{B}=\mu_0(\vec{H}+\vec{M})$  


当施加外场$\vec{H}_e$时，物质会磁化出$\vec{M}$，注意$\vec{M}$ 也会在产生磁场$\vec{H}_i$，平衡之后物质内的磁场应该是二者的叠加$\vec{H}=\vec{H}_e+\vec{H}_i$。平衡之后，$\vec{M}$与$\vec{H}$满足关系$\vec{M}=f(\vec{H})$，有如下几种模型：

* $\vec{M}=\chi \vec{H}$, 最简单的线性磁化
* 考虑物质的微观模型，当外部磁场过大时，物质内的磁矩全部沿外磁场方向达到最大
* 考虑剩磁，磁滞回线

# 麦克斯韦方程组

在静磁场中满足：
$$
\begin{aligned}
				\nabla \cdot \vec{B} &= 0\\
				\nabla \times \vec{H} &= 0
\end{aligned}
$$ 
代入$\vec{B}=\mu_0(\vec{H}+\vec{M})$和$\vec{M}=f(\vec{H})$，将$\vec{H}$写成标量场梯度，就可以解出$\vec{H}$。

## 电磁力

在物质当中的应力张量的形式存在分歧，主要原因在于机械能和电磁场能的划分。

# 模拟

## 最简单

将所有$\vec{M}$存在网格上，计算网络之间的力和力矩，问题：

* 不考虑二次磁化产生的$\vec{H}_i$
* 只考虑线性磁化

## 考虑微观磁化过程

考虑朗道方程：
$$
\frac{d\vec{M}}{dt} = -\gamma (\vec{M}\times \vec{H}_{eff} - \eta \vec{M}\times \frac{d\vec{M}}{dt})
$$ 
即考虑微观的磁化过程，注意微观$\vec{M}$的大小并不会发生改变，只会改变方向。

每个cell中sample两个点，组合之后得到cell的磁化强度：
$$
\vec{M} = \frac{1}{2}(\vec{m}_1+\vec{m}_2)M_s
$$ 