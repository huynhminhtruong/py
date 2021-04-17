if __name__ == "__main__":
    n = 2 * int(input())
    a = [(input().split()) for _ in range(n)]
    a = sorted(a, key=lambda x: (x[0], x[1]))
    print(a)