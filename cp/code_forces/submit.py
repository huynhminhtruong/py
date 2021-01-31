if __name__ == '__main__':
    n, m, a, b = map(int, input().split())
    d = (n // m) * b
    print([min(n * a, d + (n % m) * a, d + b), min(n * a, b)][not d])