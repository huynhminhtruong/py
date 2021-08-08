import math
import os
import random
import re
import sys
import functools as ft
from operator import itemgetter, attrgetter
from collections import Counter
from itertools import combinations


def candles(a: int, b: int):
    res = a
    while a // b:
        res += a // b
        a = a // b + a % b
    print(res + a // b)


def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [
        v if v != elemToReplace else substitutionElem for i, v in enumerate(inputArray)
    ]


def isSmooth(a):
    idx = len(a) % 2
    if not idx:
        idx = len(a) // 2
        return a[0] == a[-1] == a[idx] + a[idx - 1]
    return a[0] == a[-1] == a[len(a) // 2]


def replaceMiddle(a):
    idx = len(a) % 2
    if not idx:
        idx = len(a) // 2
        a[idx - 1] = a[idx] + a[idx - 1]
        a.pop(idx)
    return a


def makeArrayConsecutive2(a):
    a.sort()
    b = range(a[0], a[-1])
    return len(set(b) - set(a))


def isPower(n):
    i, d = 2, False

    while i < n:
        if not n % i:
            n //= i
            if not d:
                d = not d
        else:
            if d:
                return False
            i += 1
    return True


def isSumOfConsecutive2(n):
    cnt = 0
    for i in range(1, n):
        j = i + 1
        res = i
        while res < n:
            res += j
            j += 1
            cnt += res == n
    return cnt


def squareDigitsSequence(n):
    cnt, a = 1, list()
    a.append(n)
    while True:
        a.append(sum([int(i) ** 2 for i in str(a[-1])]))
        cnt += 1
        if a.count(a[-1]) > 1:
            break
    return cnt


def pagesNumberingWithInk(current, numberOfDigits):
    while len(str(current)) <= numberOfDigits:
        numberOfDigits -= len(str(current))
        current += 1
    return current - 1


def comfortableNumbers(l, r):
    cnt, a = 0, range(l, r + 1)
    b = [sum([int(j) for j in str(i)]) for i in a]
    for i, v in enumerate(a):
        j = i + 1
        while j < r - l + 1:
            cnt += a[i] + b[i] >= a[j] and a[j] - b[j] <= a[i]
            j += 1
    return cnt


if __name__ == "__main__":
    # n = int(input())
    l, r = map(int, input().split())
    print(comfortableNumbers(l, r))
