from typing import Generator\


# FenwickTree, BinaryIndexedTree
# https://qiita.com/R_olldIce/items/f2f7930e7f67963f0493
# https://atcoder.jp/contests/practice2/tasks/practice2_b
class FenwickTree(object):
    def __init__(self, size):
        self.size = size
        self.data = [0] * (size+1)

    def add(self, idx, num):https://atcoder.jp/contests/abc180/tasks/abc180_d
        i = 0
        while idx <= self.size:
            self.data[idx] += num
            while True:
                if (idx >> i) & 1:
                    idx += 1 << i
                    break
                i += 1

    def sum(self, l, r):
        def _sum(idx):
            sum = self.data[idx]
            i = 0
            while idx > 0:
                while True:
                    if idx & (1 << i):
                        idx -= (1 << i)
                        sum += self.data[idx]
                        break
                    i += 1
            return sum
        return _sum(r) - _sum(l-1)

# UnionFind　同じ連結成分にあるノード数を負の数でとる
# https://atcoder.jp/contests/practice2/tasks/practice2_a
# https://atcoder.jp/contests/abc181/tasks/abc181_f
class UnionFind:
    def __init__(self, size):
        self.data = [-1] * size
    def root(self, x):
        if self.data[x] < 0:
            return x
        ans = self.root(self.data[x])
        self.data[x] = ans
        return ans
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.data[x] > self.data[y]:
            x, y = y, x
        self.data[x] += self.data[y]
        self.data[y] = x
        return True
    def same(self, x, y):
        return self.root(x) == self.root(y)

# 素数の列挙、エラトステネスの篩
def sieve_of_eratosthenes(limit: int) -> list:
    """
    :param limit: upper limit
    :return: primes: List of prime numbers
    """
    primes = []
    numbers = [i for i in range(2, limit + 1)]
    p = numbers[0]
    while p ** 2 <= limit:
        primes.append(p)
        numbers = [i for i in numbers if i % p != 0]
        p = numbers[0]
    primes += numbers
    return primes

# 素因数分解、素因数のリストを返す
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

# 半全部列挙
# https://atcoder.jp/contests/abc184/tasks/abc184_f
# 1. 半分のグループBを全列挙
# 2. 残り半分のグループCを全列挙
# 3. 二分探索を用いて最適な組み合わせを探す
# Aの中からlimit以内となる最大値を求める
def half_full_search(A: list, limit: int) -> int:
    len_n = len(A)

    def _bit_search(digit: int):
        for i in range(2 ** digit):
            yield [(i >> j) & 1 for j in range(digit)]

    L = A[:len_n//2]
    left = []
    for i in range(2 ** (len_n//2)):
        tmp = 0
        for j in range(len_n//2):
            b = (i >> j) & 1
            tmp += b * L[j]
        left.append(tmp)
    R = A[len_n//2:]
    right = []
    for i in range(2 ** (len_n - len_n // 2)):
        tmp = 0
        for j in range((len_n - len_n // 2)):
            b = (i >> j) & 1
            tmp += b * R[j]
        right.append(tmp)
    left = sorted(left)

    import bisect
    max_value = 0
    for r in right:
        tmp = limit - r
        if tmp >= 0:
            idx = bisect.bisect_right(left, tmp)
            l = left[idx-1]
            max_value = max(max_value, r+l)
    return max_value


# 組み合わせの公式を計算
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


# アフィン変換の累積和、累積和のリストを返す
# https://atcoder.jp/contests/abc189/tasks/abc189_e
def affine_transform_cumsum(iter: int) -> list:
    initial_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    cumsum_matrix = [initial_matrix]

    # オプションに応じてアフィン変換の行列を返す
    def _get_option():
        op = input().split()
        # 原点を中心に時計回りに90度回転
        if op[0] == '1':
            return [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]
        # 原点を中心に反時計回りに90度回転
        elif op[0] == '2':
            return [[0, -1, 0], [1, 0, 0], [0, 0, 1]]
        # 直線 x=p について対称な位置に移動
        elif op[0] == '3':
            p = int(op[1])
            return [[-1, 0, 2*p], [0, 1, 0], [0, 0, 1]]
        # 直線 y=p について対称な位置に移動
        elif op[0] == '4':
            p = int(op[1])
            return [[1, 0, 0], [0, -1, 2*p], [0, 0, 1]]

    for _ in range(iter):
        prev_matrix = cumsum_matrix[-1]
        get_matrix = _get_option()
        add_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    add_matrix[i][j] += get_matrix[i][k] * prev_matrix[k][j]
        cumsum_matrix.append(add_matrix)

    return cumsum_matrix

# ナップザック問題をrecursive
# O(2**N)のため、10**8-9あたりまで
import sys
sys.setrecursionlimit(10 ** 9)
def _knapsack(weight: list, limit: int) -> int:
    if not weight:
        return limit
    w = weight[-1]
    val = _knapsack(weight[:-1], limit)
    if limit >= w:
        val_2 = _knapsack(weight[:-1], limit - w)
        val = min(val, val_2)
    return val