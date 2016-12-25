
class normal_distribute(object):

    def __init__(self, aver=0.0, div=1.0):
        '''初始化,aver为正态分布均值,div为正态分布标准差,默认为标准正态分布'''
        self.aver = aver
        self.div = div

    def st_norm(self, u):
        '''标准正态分布'''
        import math
        x = abs(u) / math.sqrt(2)
        T = (0.0705230784, 0.0422820123, 0.0092705272,
             0.0001520143, 0.0002765672, 0.0000430638)
        E = 1 - pow((1 + sum([a * pow(x, (i + 1))
                              for i, a in enumerate(T)])), -16)
        p = 0.5 - 0.5 * E if u < 0 else 0.5 + 0.5 * E
        return(p)

    def norm(self, x):
        '''将正态分布归一化为标准正态分布,x为x轴值,并输出x对应的正态分布概率'''
        d = (x - self.aver) / self.div
        return self.st_norm(d)
