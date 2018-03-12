# -*- coding:utf-8 -*-
from datetime import datetime


class timeprinter(object):
    def __init__(self):
        print('execute begin')
        self.begin_time = datetime.now()

    def __del__(self):
        self.__executetime()
        print('execute done, spend %rs' % self.delta_time)

    def printexectime(self):
        self.__executetime()
        print('alread execute %rs' % self.delta_time)

    def __executetime(self):
        self.end_time = datetime.now()
        self.delta_time = (self.end_time - self.begin_time).total_seconds()
