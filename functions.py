from typing import Generator

# 素因数分解
# https://atcoder.jp/contests/abc169/tasks/abc169_d
def prime_factorize(num: int) -> list:
    prime_factors = []
    while num % 2 == 0:
        num //= 2
        prime_factors.append(2)
    factor = 3
    while factor ** 2 <= num:
        if num % factor == 0:
            num //= factor
            prime_factors.append(factor)
        else:
            factor += 2
    if num != 1:
        prime_factors.append(num)
    return prime_factors

# bit全探索
# https://atcoder.jp/contests/abc167/tasks/abc167_c
def bit_search(digit: int) -> Generator:
    for i in range(2**digit):
        # print(bin(i))
        # for j in range(M):
        #     # print((i >> j) & 1)
        #     bit = (i >> j) & 1)
        yield [(i >> j) & 1 for j in range(digit)]


# 組み合わせ
# https://atcoder.jp/contests/abc167/tasks/abc167_e
from operator import mul
from functools import reduce
def combination(n, r):
    if r == 0:
        return 1
    r = min(r, n-r)
    numerator = reduce(mul, range(n-r+1, n+1))
    denominator = reduce(mul, range(1, r+1))
    return numerator // denominator