# -*- coding: utf-8 -*-
# python 36

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)     # 横轴，（自变量） 256个点，-pi到pi之间
    c,s = np.cos(x),np.sin(x)           # 纵轴（应变量）

    # plt.figure(1)       # 创建一张图
    # plt.plot(x,c)
    # plt.title("cos")
    # plt.figure(2)
    # plt.plot(x,s)
    # plt.title("sin")
    # plt.show()

    # plt.figure(1)       # 创建一张图,没有这一句也可以出来一张图，通过这句可以创建多张图
    plt.plot(x,c,color="blue", linewidth=1.0, linestyle="-",label="COS(x)",alpha=0.5)
    plt.plot(x,s,"r*",label="SIN(x)")
    plt.title("cos&sin")

    ax = plt.gca()
    # 获取当前坐标轴，通过上面的语句，已经生成了一个坐标中，这里获取它，并做一些修改
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data",0))
    ax.spines["bottom"].set_position(("data",0))

    ax.xaxis.set_ticks_position("bottom")
    ax.yaxis.set_ticks_position("left")
    # 控制x轴的显示范围
    # plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
    #            [r'$-\pi$', r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
    plt.yticks(np.linspace(-1,1,5,endpoint=True))   #设置y轴的显示范围

    for label in ax.get_xticklabels()+ax.get_yticklabels():
        label.set_fontsize(12)
        label.set_bbox(dict(facecolor="white",edgecolor="None",alpha=0.2))

    plt.legend(loc="upper left")    # label显示位置，图片中生成一个铭文
    plt.grid()          # 显示网格

    # plt.axis([-1,1,-0.5,1])     #控制显示范围

    # 填充
    plt.fill_between(x, np.abs(x) < 0.5,    #The curves are defined by the points (*x*, *y1*) and (*x*, *y2*)
                     c, c>0.5,
                     color="green",
                     alpha=0.5)

    # plt.fill_between(x, np.abs(x) < 0.5,
    #                  s, s>0.5,
    #                  color="blue",
    #                  alpha=0.5)

    # 添加注释
    t = 1
    plt.plot([t,t],[0,np.cos(t)],"y",linewidth=3, linestyle="--")

    #
    plt.annotate("cos(1)",xy=(1,np.cos(1)), xycoords="data",xytext=(+10,+30),
                 textcoords="offset points", arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
    plt.show()




if __name__ == '__main__':
    main()


