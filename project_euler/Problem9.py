# -*- coding:utf-8 -*-
from functools import reduce
from operator import mul


def func():
    for a in range(1, 250):
        for b in range(a+1, 450):
            if a*a + b*b == (1000 - a - b)**2:
                return a*b*(1000 - a - b)


def func2():
    list_ret = [(a, b, (1000-a-b)) for a in range(1, 333) for b in range(a+1, 500) if a**2 + b**2 == (1000-a-b)**2]
    return [reduce(mul, ret[0:]) for ret in list_ret][0]


if __name__ == '__main__':
    print(func2())
