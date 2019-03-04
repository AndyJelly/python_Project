# -*- coding: utf-8 -*-
# python 36

import pandas as pd
import numpy as np


list_title = ["begin_time",
              "end_time",
              "file_size",
              "print_speed",
              "file_name"]

def main():
    s = pd.Series([i*2 for i in range(1, 11)])
    print(s)
    datas = pd.date_range("20190304", periods=8, freq='D')
    print(datas)
    df = pd.DataFrame(np.random.randn(8, 5), index=datas, columns=list_title)
    print(df)

    df = pd.DataFrame({'A': 1,
                       'B': pd.Timestamp('20190304'),
                       'c': pd.Series(1, index=list(range(4)), dtype='float32'),
                       'D': np.array([3]*4, dtype='float32'),
                       'E': pd.Categorical(['police', 'student', 'teacher', 'doctor'])})
    print(df)
    print(np.array([3]*4))

    print(df.head(2))
    print(df.tail(2))
    print(df.index)
    print(df.values)
    print(df.T)
    # print(df.sort(columns='C'))
    print(df.describe())


if __name__=='__main__':
    main()
