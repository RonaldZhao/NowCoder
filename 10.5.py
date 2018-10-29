import random

p = random.random()


class RandomP:
    @staticmethod
    def f():
        return 0 if random.random() < p else 1


class Random01:
    def random01(self):
        t = "00"
        while t in ["00", "11"]:
            t = str(RandomP.f()) + str(RandomP.f())
        return 0 if t == "01" else 1


r = Random01()
print(r.random01())
