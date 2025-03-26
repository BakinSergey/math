# построение графика функции чисел Каталана С(n) = 2n! / n!(n+1)!
import math
from pprint import pprint
from typing import List


def catalan(n: int) -> List[int]:
    """вернет n чисел Каталана"""
    res = [1]
    while len(res) < n:
        res.append(sum(i[0] * i[1] for i in zip(res, res[::-1])))

    return res


def catalan_expo_plot(n):
    from matplotlib import pyplot as plt
    cat = [(x, catalan(x)[-1]) for x in range(n)]
    expo = [(x, math.e ** x) for x in range(n)]

    plt.plot(*zip(*cat))
    plt.plot(*zip(*expo))
    plt.show()


if __name__ == '__main__':
    pass
    # assert(euler(11) == 10)

    catalan_expo_plot(20)

# числа каталана - 1,1,2,5,14
