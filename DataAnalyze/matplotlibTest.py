# -*- coding: utf-8 -*-
# python 36

import matplotlib.pyplot as plt
import numpy as np


def sin_cos():
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)     # 横轴，（自变量） 256个点，-pi到pi之间
    c, s = np.cos(x), np.sin(x)           # 纵轴（应变量）

    # plt.figure(1)       # 创建一张图
    # plt.plot(x,c)
    # plt.title("cos")
    # plt.figure(2)
    # plt.plot(x,s)
    # plt.title("sin")
    # plt.show()

    # plt.figure(1)       # 创建一张图,没有这一句也可以出来一张图，通过这句可以创建多张图
    plt.plot(x, c, color="blue", linewidth=1.0, linestyle="-", label="COS(x)", alpha=0.5)
    plt.plot(x, s, "r*", label="SIN(x)")
    plt.title("cos&sin")

    ax = plt.gca()
    # 获取当前坐标轴，通过上面的语句，已经生成了一个坐标中，这里获取它，并做一些修改
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))

    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    # 控制x轴的显示范围
    # plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
    #            [r'$-\pi$', r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
    plt.yticks(np.linspace(-1, 1, 5, endpoint=True))   #设置y轴的显示范围

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        # ax.get_xticklabels() 返回的是一个列表
        label.set_fontsize(12)
        label.set_bbox(dict(facecolor="white", edgecolor="None", alpha=0.2))

    plt.legend(loc="upper left")    # label显示位置，图片中生成一个铭文
    plt.grid()          # 显示网格

    # plt.axis([-1,1,-0.5,1])     #控制显示范围

    # 填充
    plt.fill_between(x, np.abs(x) < 0.5,    #The curves are defined by the points (*x*, *y1*) and (*x*, *y2*)
                     c, c > 0.5,
                     color="green",
                     alpha=0.5)

    # plt.fill_between(x, np.abs(x) < 0.5,
    #                  s, s>0.5,
    #                  color="blue",
    #                  alpha=0.5)

    # 添加注释
    t = 1
    plt.plot([t, t], [0, np.cos(t)], "y", linewidth=3, linestyle="--")

    #
    plt.annotate("cos(1)", xy=(1, np.cos(1)), xycoords="data", xytext=(+10, +30),
                 textcoords="offset points", arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
    plt.show()


def demo_1():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8])      # 生成一个一维数组,作为横轴
    y = np.array([3, 5, 7, 6, 2, 6, 10, 15])    # 生成一个一维数组,作为纵轴

    plt.figure(1)
    plt.plot(x, y, 'r')     # 简单折线图

    plt.figure(2)
    plt.plot(x, y, 'y', lw=2)
    plt.show()


def demo_bar():
    # men_means = (20, 35, 30, 35, 27)
    # women_means = (25, 32, 34, 20, 25)
    #
    # ind = np.arange(len(men_means))     # 通过arange，创建数组，返回 numpy的ndarray 对象， 作为横轴
    # width = 0.35
    # fig, ax = plt.subplots()        # fig 图片对象， ax 坐标轴对象
    #
    # rect_men = ax.bar(ind - width / 2, men_means, width, color="SkyBlue", label='Men')
    # rect_men = ax.bar(ind + width / 2, women_means, width, color="IndianRed", label='Women')
    #
    # ax.set_ylabel('Scores')
    # ax.set_title('Scores by group and gender')
    # plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
    # ax.legend()
    #
    # plt.show()

    # x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    # y = np.array([13, 25, 17, 36, 21, 16, 10, 15])
    # plt.bar(x, y, 0.2, alpha=1, color='SkyBlue')  # 生成条形图（柱状图）
    # plt.plot(x, y)
    # plt.show()

    n = 10
    x = np.arange(n)        # [0 1 2 3 4 5 6 7 8 9]

    y1 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)        # uniform distribution 均匀分布
    y2 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)

    # 画出两个柱状图
    plt.bar(x, y1, color="SkyBlue", label='y1')
    plt.bar(x, -y2, color="IndianRed", label='y2')

    # 在柱状图上显示具体数值, ha水平对齐, va垂直对齐
    print(x)
    temp = zip(x, y2)
    print(temp)
    for x, y in zip(x, y1):
        plt.text(x, y + 0.1, '%.2f' % y, ha='center', va='bottom')
    print(x)

    for x, y in temp:
        plt.text(x, -y - 0.1, '%.2f' % y, ha='center', va='bottom')

    # 设置坐标轴范围
    plt.xlim(-1, n)
    plt.ylim(-1.5, 1.5)

    # 去除坐标轴
    plt.xticks(())
    plt.yticks(())

    plt.legend()

    plt.show()


def demo_2():
    # 传入参数是numpy数组时,绘出来的多点（x1,y1）(x2,y2)...，多个点连成一条线
    for i in range(0, 15):
        x = np.zeros([2])
        x[0] = i
        x[1] = i+1

        y = np.zeros([2])
        if i % 2 == 0:
            y[0] = 10
            y[1] = 20
        else:
            y[0] = 30
            y[1] = 20
        plt.plot(x, y, 'g', lw=1)
    plt.show()

    # for i in range(0,15):
    #     x = np.zeros([3])
    #     x[0] = i
    #     x[1] = i+2
    #     x[2] = i+4
    #
    #     y = np.zeros([3])
    #     if i % 2 == 0:
    #         y[0] = 10
    #         y[1] = 20
    #         y[2] = 30
    #     else:
    #         y[0] = 30
    #         y[1] = 20
    #         y[2] = 10
    #     plt.plot(x, y, 'g', lw=1)
    # plt.show()


def demo_3():
    # 在一张图中，画出多条曲线
    x = np.linspace(-4, 4, 256)
    # print(x)
    y1 = 2 * x + 1
    y2 = x ** 2

    plt.figure(num=1, figsize=(10, 4))      # num 只是指定图片的编号，并不是个数
    plt.plot(x, y1, linestyle='--', label='y = 2 * x + 1')
    plt.plot(x, y2, color='red', linewidth=1.0, linestyle=':', label='y = x ** 2')

    # 设置图片的标题
    plt.title('fun(x)', loc='left')


    # # 设置坐标轴的取值范围
    # plt.xlim((-1, 1))
    # plt.ylim((0, 3))

    # 控制显示范围
    plt.axis([-1, 1, 0, 3])
    # 设置x轴的刻度
    plt.xticks(np.linspace(-1, 1, 9))
    plt.yticks(np.linspace(0, 3, 9))

    # 设置x、y轴的label
    plt.xlabel('this x axis', fontproperties='SimHei', fontsize=14)
    plt.ylabel('this y axis', fontproperties='SimHei', fontsize=14)


    # 设置坐标轴

    ax = plt.gca()         # 获取当前的坐标轴, gca = get current axis
    # 设置右边框和上边框的颜色为none，即不显示
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    # 设置x坐标轴为下边框
    ax.xaxis.set_ticks_position('bottom')
    # 设置y坐标轴为左边框
    ax.yaxis.set_ticks_position('left')

    # 设置x轴, y轴 在(0, 0)的位置
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))

    # ax.spines['bottom'].set_color('none')
    # ax.spines['left'].set_color('none')
    # ax.xaxis.set_ticks_position('top')
    # ax.yaxis.set_ticks_position('right')
    #
    # ax.spines['top'].set_position(('data', 0))
    # ax.spines['right'].set_position(('data', 0))

    # 设置坐标轴label的大小，背景色等信息
    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(8)
        label.set_bbox(dict(facecolor='yellow', edgecolor='none', alpha=0.5))

    plt.legend(loc='best')
    plt.grid()

    # Plot lines and/or markers to the class:`~matplotlib.axes.Axes`
    plt.plot([0.5, 0.5], [0, 2], 'k--', lw=2.5)
    plt.annotate(r'$2 * x + 1 = %s$' % 2, xy=(0.5, 2), xycoords='data', xytext=(+30, -30),
                 textcoords='offset points', fontsize=16,
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad = .2'))
    plt.show()


def demo_scatter():
    n = 1024
    x = np.random.normal(0, 1, n)
    print(x)
    y = np.random.normal(0, 1, n)
    print(y)
    color = np.arctan2(y, x)

    # Make a scatter plot（散点图） of `x` vs `y`.
    plt.scatter(x, y, s=75, c=color, alpha=0.5)

    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)

    plt.xticks()
    plt.yticks()
    plt.show()


def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(- x ** 2 - y ** 2)


def demo_contourf():
    # 数据数目
    n = 256
    # 定义x, y
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)

    # 生成网格数据    生成一个256*256的二维数组
    X, Y = np.meshgrid(x, y)
    # print(X)
    # print(X.ndim)
    # print(X.shape)
    #
    # print(Y.ndim)
    # print(Y.shape)
    # 填充等高线的颜色, 8是等高线分为几部分
    plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)
    # 绘制等高线
    C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidths=0.5)
    # 绘制等高线数据
    plt.clabel(C, inline=True, fontsize=10)

    # plt.xticks()
    # plt.yticks()
    plt.show()


def demo_3D():
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = Axes3D(fig)    # 将figure变为3d

    # 数据数目
    n = 256
    # 定义x, y
    x = np.arange(-4, 4, 0.25)
    y = np.arange(-4, 4, 0.25)

    # 生成网格数据
    X, Y = np.meshgrid(x, y)

    # 计算Z轴的高度
    Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
    # 绘制3D曲面
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
    # 绘制从3D曲面到底部的投影
    ax.contour(X, Y, Z, zdim='z', offset=-2, cmap='rainbow')

    # 设置z轴的维度
    ax.set_zlim(-2, 2)
    # 保存图片
    plt.savefig('./data/fig3D.png')
    plt.show()


if __name__ == '__main__':
    # sin_cos()
    # demo_1()
    # demo_bar()
    # demo_3()
    # demo_scatter()
    # demo_contourf()
    demo_3D()


