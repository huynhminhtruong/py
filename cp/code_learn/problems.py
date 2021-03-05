import math
from operator import itemgetter

def is_prime(n: int)->bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if not (n % i):
            return False
    return True

def col_array_input():
    n = int(input())
    a = list()
    for i in range(n):
        t = int(input())
        if is_prime(t):
            a.append(t)
    print(*a)

def col_array_count():
    n = int(input())
    d = dict()
    for i in range(n):
        t = int(input())
        d[t] = d.get(t, 0) + 1
    d = sorted(d.items(), key=itemgetter(0))
    print("".join("{0} - {1};".format(x[0], x[1]) for x in d))

if __name__ == "__main__":
    pass