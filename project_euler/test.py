# -*- coding:utf-8 -*-


def enumint(set_int, input_array):
    for i in range(0, len(input_array)):
        input_temp = [temp for temp in input_array]
        input_temp.remove(input_array[i])
        set_int.add(input_array[i] * 0 + input_temp[0])
        set_int.add(input_array[i] * 0 + input_temp[1])
        set_int.add(input_array[i] * 10 + input_temp[0])
        set_int.add(input_array[i] * 10 + input_temp[1])
        set_int.add(input_array[i] * 100 + input_temp[0] * 10 + input_temp[1])
        set_int.add(input_array[i] * 100 + input_temp[1] * 10 + input_temp[0])


def isinvaildinput(input_int_array):
    if max(input_int_array) >= 10:
        return -1

    # 2/5、6/9不能同时出现
    if 2 in input_int_array and 5 in input_int_array:
        return -1

    if 6 in input_int_array and 9 in input_int_array:
        return -1

    #不能有重复的数字
    temp_set = set()
    for i in input_int_array:
        temp_set.add(i)
    if len(temp_set) != 3:
        return -1


def func():
    input_str = input()
    temp_str = input_str.split(',')
    input_int_array = [int(i) for i in temp_str]
    temp = True
    while temp:
        temp = False
        if isinvaildinput(input_int_array) == -1:
            return -1
        else:
            #将所有的组合放到一个列表中
            input_int_arrays = []
            input_int_temp = [i for i in input_int_array]

            twoorfive = []
            sixornine = []
            if 2 in input_int_temp:
                twoorfive.append(2)
                twoorfive.append(5)
                input_int_temp.remove(2)
            elif 5 in input_int_temp:
                twoorfive.append(2)
                twoorfive.append(5)
                input_int_temp.remove(5)
            if 6 in input_int_temp:
                sixornine.append(6)
                sixornine.append(9)
                input_int_temp.remove(6)
            elif 9 in input_int_temp:
                sixornine.append(6)
                sixornine.append(9)
                input_int_temp.remove(9)

            if not input_int_temp:
                return -1
            if twoorfive:
                for j in twoorfive:
                    if sixornine:
                        for k in sixornine:
                            temp = [i for i in input_int_temp]
                            temp.append(k)
                            temp.append(j)
                            input_int_arrays.append(temp)
                            continue
                    else:
                        temp = [i for i in input_int_temp]
                        temp.append(j)
                        input_int_arrays.append(temp)
                        continue
            else:
                if sixornine:
                    for k in sixornine:
                        temp = [i for i in input_int_temp]
                        temp.append(k)
                        input_int_arrays.append(temp)
                else:
                    temp = [i for i in input_int_temp]
                    input_int_arrays.append(temp)

            #将每个数组转成所有可能的数字组合
            set_int = set()

            for array_int in input_int_arrays:
                enumint(set_int, array_int)
            list_int = list(set_int)
            list_int.sort()
            print(list_int)

            #返回值
            max_int = max(input_int_array)
            if max_int >= len(list_int):
                return list_int[-1]
            else:
                return list_int[max_int-1]


if __name__ == '__main__':
    print(func())






