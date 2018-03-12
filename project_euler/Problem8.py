# -*- coding:utf-8 -*-
#from string import whitespace
from operator import mul
from functools import reduce


def func():
    # input_str = ''
    with open('Problem8.txt', 'r') as f:
        whitespace = ' \t\n\r\v\f'
        input_arrays = [int(c) for line in f.readlines() for c in line if c not in whitespace]
        print(len(input_arrays))

        print(max([reduce(mul, input_arrays[i: i + 13]) for i in range(len(input_arrays) - 12)]))

    # ugly code
        # lines = f.readlines()

    # for line in lines:
    #     input_str += line.strip()

    # input_arrays = []
    # for i in range(0, len(input_str) - 12):
    #     input_arrays.append(input_str[i: i+13])
    #
    # list_ret = []
    # for input_array in input_arrays:
    #     ret = 1
    #     for i in input_array:
    #         ret *= int(i)
    #         list_ret.append(ret)
    # print(len(list_ret))
    # print(max(list_ret))


if __name__ == '__main__':
    func()
