from typing import Generator

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