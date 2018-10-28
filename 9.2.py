class Robot:
    def countWays(self, x, y):
        s = x + y - 2
        fz = 1
        for i in range(s, s - x + 1, -1):
            fz *= i
        fm = 1
        for i in range(1, x):
            fm *= i
        return fz / fm
