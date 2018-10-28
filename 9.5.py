class Distribution:
    def getWays(self, n, m):
        if m > n:
            return 0
        elif m == n:
            return 1
        fz, fm = 1, 1
        # n-1 中选 m-1
        for i in range(m - 1):
            fz *= n - 1 - i
        for i in range(1, m):
            fm *= i
        return fz / fm
