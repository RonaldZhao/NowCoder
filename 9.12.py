class CombineByMistake:
    def countWays(self, n):
        if n == 1:
            return 0
        elif n == 2:
            return 1
        pre, ret = 0, 1
        for i in range(3, n + 1):
            t = (i - 1) * (pre + ret) % 1000000007
            pre, ret = ret, t
        return ret
