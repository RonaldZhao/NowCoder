class StandInLine:
    def getWays(self, n, a, b):
        if n <= 1:
            return [0, 0]
        a1, a2 = 1, 1
        if n > 2:
            for i in range(1, n + 1):
                a1 *= i
            a1 /= 2
            a2 = a1 * 2 / n
        return [a1, a2]
