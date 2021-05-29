import math
import os
import random
import re
import sys
import functools as ft
from operator import itemgetter, attrgetter
from collections import Counter
from itertools import combinations

def pascal(n: int):
    a = [[1]]
    for _ in range(n - 1):
        tmp = zip([0] + a[-1], a[-1] + [0])
        a.append([sum(i) for i in tmp])
    return a

def digital_root(n):
    while int(n) // 10 > 0:
        n = sum(list(map(int, str(n))))
    return n

def circularly_sorted(a: list) -> bool:
    i = 1
    while i < len(a) and a[i] >= a[i - 1]:
        i += 1
    b = zip(a[i:] + a[:i], sorted(a))
    return len([i for i in b if i[0] == i[1]]) == len(a)

def find_odd_times(a: list) -> int:
    # use list.count(number) instead
    cnt = 1
    a.sort()

    for i in range(1, len(a)):
        if a[i] != a[i - 1]:
            if cnt % 2: return a[i - 1]
            cnt = 1
        else:
            cnt += 1
    return a[-1]

def array_diff(a: list, b: list) -> list:
    c = set(a) & set(b)
    return [i for i in a if not (i in c)]

def valid_parentheses(s: str) -> bool:
    a = list()
    for i in s:
        if i == '(':
            a.append(i)
        elif i == ')':
            if not len(a):
                return False
            a.pop()
    return not len(a)

def duplicate_encode(s: str) -> str:
    res = list()
    s = s.lower()
    for i in s:
        res.append(')' if s.count(i) > 1 else '(')
    return "".join(res)

def iq_test(a) -> int:
    a = [int(i) % 2 for i in a.split()]
    return a.index(1) + 1 if a.count(0) > 1 else a.index(0) + 1

def generate_hashtag(s: str):
    a = "".join(['#'] + [i[0].upper() + i[1:] for i in s.split()])
    return False if not (len(a) - 1) or len(a) > 140 else a

def move_zeros(a: list):
    cnt = a.count(0)
    a = list(filter(lambda i: i != 0, a))
    a.extend([0] * cnt)
    return a

def sort_list(a: list):
    # sort even after odd numbers
    return sorted(a, key=lambda i: (not (i % 2)))

if __name__ == '__main__':
    n = int(input())
    a = list()
    print(pascal(n))