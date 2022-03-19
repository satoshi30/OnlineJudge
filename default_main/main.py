def main():
    V, A, B, C = map(int, input().split())
    V = V % (A + B + C)
    a = V - A
    b = a - B
    c = b - C

    if a < 0:
        print("F")
    elif b < 0:
        print("M")
    else:
        print("T")

if __name__ == '__main__':
    main()