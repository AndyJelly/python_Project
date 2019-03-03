# -*- coding: utf-8 -*-
# python 36

import numpy as np


def np_ndarray():
    # print(np.eye(2))

    list = [[1,3,5],[2,4,6]]
    print(type(list))
    np_list = np.array(list, dtype=np.int64)
    print(type(np_list))
    print(np_list.shape)        # 几行几列
    print(np_list.ndim)         # 几维
    print(np_list.dtype)        # 构造时，传入的dtype,数据类型
    print(np_list.itemsize)     # 每个元素的大小 int64对应占的字节
    print(np_list.size)         # 元素的个数


def np_random():
    # 常用数组/分布
    # np.random
    print(np.zeros([2, 3]))  # 2行3列，值为0的矩阵
    print(np.ones([2, 3]))  # 2行3列，值为1的矩阵
    print(np.random.rand(2, 1))  # 创建指定形状(示例为10行10列)的数组(范围在0至1之间)
    print(np.random.uniform(0, 100, 3))  # 范围内，随机取一个数
    print(np.random.randint(0, 9, 3))  # 随机取范围内的整数
    print(np.random.choice([10, 20, 30, 40, 50], 2))  # 提供数字范围内，选出2个
    print(np.random.beta(1, 10, 2))


if __name__ == '__main__':
    np_ndarray()
    np_random()
