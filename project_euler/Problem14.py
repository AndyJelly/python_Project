# -*- coding:utf-8 -*-
from timeprinter import timeprinter


def getCollatzsequence(begin, chain_dict):
    chain_list = []
    chain_list.append(begin)
    bExit = False
    while True:
        if begin in chain_dict:
            break
        if begin == 1:
            bExit = True
            break
        if begin % 2 == 0:
            begin = int(begin / 2)
        else:
            begin = 3 * begin + 1
        chain_list.append(begin)

    if bExit:
        for i in range(len(chain_list)):
            chain_dict[chain_list[i]] = len(chain_list) - i
    else:
        for i in range(len(chain_list) - 1):
            chain_dict[chain_list[i]] = chain_dict[chain_list[-1]] + len(chain_list) - i
    # print(chain_list)
    # print(chain_dict)


def getCollatzsequenceslow(begin):
    chain_list = []
    while True:
        if begin == 1:
            break
        if begin % 2 == 0:
            begin = int(begin / 2)
        else:
            begin = 3 * begin + 1
        chain_list.append(begin)
    return len(chain_list)


if __name__ == '__main__':
    tp = timeprinter()
    #ret_list_slow = list()
    ret_dict_slow = dict()
    for i in range(1000000, 2, -1):
        temp = getCollatzsequenceslow(i)
        #ret_list_slow.append(temp)
        ret_dict_slow[i] = temp
    print(sorted(ret_dict_slow, key=lambda x: ret_dict_slow[x])[-1])
    tp.printexectime()

    ret_dict = {}
    # print(getCollatzsequence(13, ret_dict))
    # print(getCollatzsequence(14, ret_dict))
    for i in range(1000000, 2, -1):
    # for i in range(2, 1000000):
        getCollatzsequence(i, ret_dict)
    tp.printexectime()
    print(len(ret_dict))
    #sorted返回一个新的list，key作为进行比较的元素
    #去除dict中value最大的key
    print(sorted(ret_dict, key = lambda x : ret_dict[x])[-1])
