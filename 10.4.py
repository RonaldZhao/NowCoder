# -*- coding:utf-8 -*-
import random


class Random5:
    @staticmethod
    def randomNumber():
        return random.randint(0, 1000000) % 5 + 1


class Random7:
    # 随机产生[1,5]
    def rand5(self):
        return Random5.randomNumber()

    # 请通过self.rand5()随机产生[1,7]
    def randomNumber(self):
        ret = 21
        while ret > 20:
            ret = (self.rand5() - 1) * 5 + self.rand5() - 1
        return ret % 7 + 1
