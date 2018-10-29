class Championship:
    def calc(self, k):
        def C(m, n):
            f = lambda x, y: x * y
            return reduce(f, range(m, m - n, -1)) / reduce(f, range(1, n + 1))

        a = 1
        for i in range(k * 2 - 1, 0, -2):
            a *= i
        b = C(k + 1, k - 1) * reduce(lambda x, y: x * y, range(1, k))

        def gcd(a, b):
            return gcd(b, a % b) if a % b else b

        x = gcd(a - b, a)
        return [(a - b) / x, a / x]
