class HighAndShort:
    def countWays(self, n):
        def C(m, n):
            # 求C(m, n)
            f = lambda x, y: x * y
            return reduce(f, range(m, m - n, -1)) / reduce(f, range(1, n + 1))

        return C(n, n / 2) / (n / 2 + 1)
