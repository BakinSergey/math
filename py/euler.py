# построение графика функции эйлера F(X) = N,
# где N - число делителей числа X(числа Эйлера)

from collections import Counter
from functools import reduce
from operator import mul
from pprint import pprint


def prim_facs(n):
    """разложение на простые множители"""
    i = 2
    primfac = []
    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(int(n))
    return primfac


def euler(n: int) -> int:
    """вернет число простых делителей, меньших чем n"""

    return reduce(mul, [k ** (v - 1) * (k - 1) for (k, v) in
                        Counter(prim_facs(n)).items()], 1)


def euler_plot(n):
    from matplotlib import pyplot as plt
    li = [(x, euler(x)) for x in range(n)]
    pprint(li)
    plt.plot(*zip(*li))
    plt.show()


if __name__ == '__main__':
    pass
    # assert(euler(11) == 10)

    euler_plot(300)


# если p-простое и a не делится на p то a^(p-1) - 1 делится на p
# 2 ** 12 - 1 = 4095
# 4095 / 13 = 315
