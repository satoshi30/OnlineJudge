def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        ans += L[i*2]
    print(ans)

if __name__ == '__main__':
    main()