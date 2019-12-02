# -*- coding: utf-8 -*-
"""
Professor Chambouliard hast just discovered a new type of magnet material. He put particles of this material in a box made of small boxes arranged in K rows and N columns as a kind of 2D matrix K x N where K and N are postive integers. He thinks that his calculations show that the force exerted by the particle in the small box (k, n) is:

v(k, n) = \frac{1}{k(n+1)^{2k}}

The total force exerted by the first row with k = 1 is:

u(1, N) = \sum_{n=1}^{n=N}v(1, n) = \frac{1}{1.2^2} + \frac{1}{1.3^2}+...+\frac{1}{1.(N+1)^2}

We can go on with k = 2 and then k = 3 etc ... and consider:

S(K, N) = \sum_{k=1}^{k=K}u(k, N) = \sum_{k=1}^{k=K}(\sum_{n=1}^{n=N}v(k, n)) \rightarrow (doubles(maxk, maxn))

Task:
To help Professor Chambouliard can we calculate the function doubles that will take as parameter maxk and maxn such that doubles(maxk, maxn) = S(maxk, maxn)? Experiences seems to show that this could be something around 0.7 when maxk and maxn are big enough.

Examples:
doubles(1, 3)  => 0.4236111111111111
doubles(1, 10) => 0.5580321939764581
doubles(10, 100) => 0.6832948559787737
Notes:
In u(1, N) the dot is the multiplication operator.
Don't truncate or round: Have a look in "RUN EXAMPLES" at "assertFuzzyEquals".
"""


def v(k, n):
    """
    for k > 9 observated that partial force is 0.
    Sum map of maps partial force function aplied to each row
    """
    return 1 / (k * ((n + 1) ** (2 * k))) if k < 10 else 0


def naive_doubles(maxk, maxn):
    my_sum = 0
    for k in range(1, maxk + 1):
        for n in range(1, maxn + 1):
            my_sum += v(k, n)
            # print(v(k, n))
    return my_sum


def naive_map_doubles(maxk, maxn):
    """
    Sum map of maps partial force function aplied to each row
    """
    # return sum(map(lambda n: sum(map(lambda k: 1 / (k * ((n + 1) ** (2 * k))) if k <10 else 0, range(1, maxk + 1))), range(1, maxn + 1)))
    return sum(map(lambda k: sum(map(lambda n: (n + 1) ** (-2 * k), range(1, maxn + 1)))/k if k < 10 else 0, range(1, maxk + 1)))


if __name__ == '__main__':
    print(naive_doubles(1, 10))
    print(naive_map_doubles(1, 10))
    assert "%.6f" % naive_map_doubles(1, 1) == "%.6f" % naive_doubles(1, 1)
    assert "%.6f" % naive_map_doubles(100, 1000) == "%.6f" % naive_doubles(100, 1000)

    import timeit

    naive_time = timeit.timeit('naive_doubles(100, 1000)', number=10, globals=globals())
    print('naive time: %s' % naive_time)

    naive_mapped_time = timeit.timeit('naive_map_doubles(100, 1000)', number=10, globals=globals())
    print('naive with map time: %s' % naive_mapped_time)

    print('method with map is faster %.2f times' % (naive_time/naive_mapped_time))
