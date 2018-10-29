class Ants:
    def collision(self, n):
        def gcd(a, b):
            return gcd(b, a % b) if a % b else b
        x = gcd(2 ** n - 2, 2 ** n)
        return [(2 ** n - 2) / x, 2 ** n / x]