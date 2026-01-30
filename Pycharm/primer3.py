import sys

if __name__ == '__main__':
    A = tuple(map(float, input().split()))

    if len(A) != 10:
        print("Неверный размер кортежа", file=sys.stderr)
        exit(1)

    s = 0
    for item in A:
        if abs(item) < 5:
            s += item

    print(s)