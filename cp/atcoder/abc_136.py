import math
import os
import random
import re
import sys

def sum_numbers(n):
    res = math.ceil(math.log(n, 10))
    s = 1 if math.log(n, 10) % 2 == 0 else 0

    for i in range(0, res, 2):
        k = 10**(i + 1) - 1
        if n > k:
            s = s + 9 * (10 ** i)
        else:
            s = s + n - 10**i + 1

    return s

def check_non_decreasing_squares(n: int, a: list):
    p = a[0]
    for i in range(1, n):
        if a[i] > p:
            p = a[i]
        if p - a[i] == 1 or p - a[i] == 0:
            continue
        print("No")
        exit(0)
    print("Yes")

def cal_distance_numbers():
    k, x = list(map(int, input().rstrip().split()))

    for i in range(x - k + 1, x + k):
        print(i, end = " ")

def count_anagram_strings():
    n = int(input())
    count = 0
    d = dict()
    for i in range(n):
        key = "".join(sorted(list(input())))
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1

    # N numbers have N * (N - 1) / 2 pairs
    for v in d.values():
        count += v * (v - 1) / 2
    
    print(int(count))

if __name__ == '__main__':
    n, m = list(map(int, input().rstrip().split()))
    a, b = [0]*n, [0 for i in range(n)]

    for i in range(n):
        a[i], b[i] = list(map(int, input().rstrip().split()))

    # max days M so max of completed jobs is M
    # completed days should be less than M

    h, max_jobs, tmp, p, k = 0, 0, 0, 0, 0

    while (p < n):
        while (k < n and m > 0):
            if a[k] <= m:
                tmp += b[k]
                m -= 1
            k += 1
        max_jobs = tmp if tmp > max_jobs else max_jobs
        tmp -= b[p]
        p += 1
        m += 1