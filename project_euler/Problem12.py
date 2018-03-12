# -*- coding:utf-8 -*-
from datetime import datetime


def getdivisors(input_int):
    ret = 0
    for i in range(1, int(input_int**.5) + 1):
        if input_int % i == 0:
            if i == input_int**.5:
                ret += 1
            else:
                ret += 2
    #         output_list.append(i)
    # return len(output_list)
    return ret


def generatetriangularnumbers():
    i = 1
    while True:
        yield int(0.5 * i * (i + 1))
        i += 1


if __name__ == '__main__':
    begin = datetime.now()
    a = 1
    sum = 1
    while getdivisors(sum) <= 500:
        a += 1
        sum += a
    print(sum, a, getdivisors(sum))
    end = datetime.now()
    deltatime = (end - begin).total_seconds()
    print('execute success,spend %f.' % deltatime)

    begin2 = datetime.now()
    g = generatetriangularnumbers()
    while True:
        num = next(g)
        if getdivisors(num) > 500:
            print(num,getdivisors(num))
            break
    end2 = datetime.now()
    deltatime2 = (end2 - begin2).total_seconds()
    print('execute success,spend %f.' % deltatime2)



