import functools as ft


def d(n):
    a = [int(i) for i in str(n)]
    b = list(map(lambda i: i + 1, a))
    print(a, b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    res = a
    while a // b:
        res += a // b
        a = a // b + a % b
    print(res + a // b)
