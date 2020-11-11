import math
import os
import random
import re
import sys
import functools
from operator import itemgetter, attrgetter
from collections import Counter

def _STOCK_EXCHANGE_LOSSES():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    n, a = N(), Y()
    l, v, r = 0, a[0], 1
    MIN = 2 ** 31 + 1

    for i in range(1, n):
        if a[i] < a[l]:
            if v > a[i]:
                v = a[i]
            if MIN > v - a[l]:
                MIN = v - a[l]
        else:
            r += 1
            l = i
            v = a[i]
    print(MIN if r < n else 0)

def _Power_Of_Thor_Episode_1():
    P = lambda: map(int, input().split())
    x, y, a, b = P()
    # game loop
    while True:
        remaining_turns = int(input())
        print("Debug messages...{0} {1} {2}".format(a, b, remaining_turns), file=sys.stderr, flush=True)
        if x == a:
            print("N" if y < b else "S")
            b += -1 if y < b else 1
        elif y == b:
            print("W" if x < a else "E")
            a += -1 if x < a else 1
        else:
            if x < a:
                print("NW" if y < b else "SW")
            else:
                print("NE" if y < b else "SE")
            b += -1 if y < b else 1
            a += -1 if x < a else 1

def _ASCII_Art():
    N = lambda: int(input())

    l = N()
    h = N()
    s = [ord(x.upper()) for x in input()]
    t, res = list(), list()

    for i in range(h):
        t.append(input())
    for row in t:
        r = ""
        for i in range(len(s)):
            if s[i] >= ord('A') and s[i] <= ord('Z'):
                p = (s[i] % ord('A')) * l
                r += row[p:p + l]
            else:
                r += row[l * 26:l * 27]
        res.append(r)
    for row in res:
        print(row)

if __name__ == '__main__':
    n = list(map(int, input().strip().split()))
    c = 0
    for i in n, n[::-1]:
        c += 1
        print(i)
    print(c)
    
# 1 2 3 4 5 6

# Get input from file
# file_input = open('input.in', 'r')
# Get input from terminal
# n = int(input())
# a, b, c = list(map(int, input().rstrip().split()))