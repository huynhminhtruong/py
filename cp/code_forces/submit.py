from collections import Counter
from itertools import combinations

if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    s = sum(a)
    t = s
    s /= 2

    while n > 0 and t > s:
        t -= a[n - 1]
        n -= 1
    print(n + 1 if t < s else n)