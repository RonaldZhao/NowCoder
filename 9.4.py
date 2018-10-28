class LonelyA:
    def getWays(self, n, A, b, c):
        if n == 3:
            return 0
        a = 1
        for i in range(1, n + 1):
            a *= i
        ab = a / n * 2
        ac = ab
        bac = a / n / (n - 1) * 2
        return a - ab - ac + bac
