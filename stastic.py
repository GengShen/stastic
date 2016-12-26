# coding=utf-8
import pandas as pd
from normal_distribute import normal_distribute


class stastic:
    '''统计工具类'''

    def __init__(self):
        pass

    def read_csv(self, file_name):
        '''读取名为file_name的csv文件'''
        with open(file_name) as f:
            t = pd.read_csv(f)
        return t

    def read_csv_column(self, file_name, n):
        '''读取csv文件file_name的第n列,n >= 0, 以列表返回'''
        t = self.read_csv(file_name)
        l = [float(i) for i in t[t.columns[n]]]
        return l

    def aver(self, l):
        '''求l列表的平均值'''
        sum = 0
        for i in l:
            sum += i
        return sum / len(l)

    def sd(self, l):
        '''求l列表的标准差'''
        a = self.aver(l)
        sum = 0
        for i in l:
            sum += (i - a)**2
        return (sum / len(l))**0.5

    def normal_standard(self, x):
        '''求标准正态分布下x值对应的概率'''
        n = normal_distribute()
        return n.st_norm(x)
