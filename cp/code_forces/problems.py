import math
import os
import random
import re
import sys
import functools
from operator import itemgetter, attrgetter
from collections import Counter

def _convert_status(status: str):
    status.lower()
    if status == "rat":
        return 0
    if status in ("woman", "child"):
        return 1
    if status == "man":
        return 2
    return 3

def _141A_Amusing_Joke():
    a, b, c = input(), input(), input()

    x = [0] * 26

    for _ in a:
        x[ord(_) % 65] += 1
    for _ in b:
        x[ord(_) % 65] += 1
    for _ in c:
        x[ord(_) % 65] -= 1

    res = list(filter(lambda i: i != 0, x))
    
    print("YES" if not(len(res) > 0) else "NO")

def _63A_Sinking_Ship():
    n = int(input())
    res = list()

    for _ in range(n):
        # name = list(map(_convert_status, input().strip().split()))
        name, status = input().strip().split()
        res.append((name, _convert_status(status)))
    res.sort(key=itemgetter(1))

    for _ in res:
        print(_[0])

def _339A_Helpful_Maths():
    n = [int(x) for x in input().strip().split("+")]
    n.sort()
    s = "+".join([str(x) for x in n])
    print(s)

def _1155A_Reverse_a_Substring():
    n, s = int(input()), input()
    res = ()
    for i in range(1, n):
        if ord(s[i]) < ord(s[i - 1]):
            res = (i, i + 1)
            break
    print("YES \n{0} {1}".format(res[0], res[1]) if len(res) > 0 else "NO")

def _490A_Team_Olympiad():
    n, t = int(input()), [int(x) for x in input().strip().split()]
    a, b, c = [[], [], []], 10 ** 6, []

    for i in range(n):
        a[t[i] - 1].append(i + 1)
    for i in range(3):
        b = len(a[i]) if len(a[i]) < b else b
    for i in range(b):
        c.append((a[0][i], a[1][i], a[2][i]))

    print(b)

    if b > 0:
        for i in c:
            print(" ".join([str(x) for x in i]))

def _432A_Choosing_Teams():
    n, k = [int(x) for x in input().strip().split()]
    y = [int(x) for x in input().strip().split()]
    r = 0

    for p in y:
        if 5 - p >= k:
            r += 1
    print("{0}".format(int(r / 3)))

def _507A_Amr_And_Music():
    n, k = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    b, p, s = list(), 0, ""

    for i in range(n):
        b.append((i + 1, a[i]))
    b.sort(key=itemgetter(1))

    while(p < n and k - b[p][1] >= 0):
        k -= b[p][1]
        p += 1

    print(p)
    for x in range(p):
        s += str(b[x][0])
        s += " "
    print(s.lstrip())

def _1011A_Stages():
    n, k = list(map(int, input().strip().split()))
    s = sorted(list(map(ord, input().strip())))
    a, p = list(), 0

    a.append(s[p])

    for i in range(1, n):
        if s[i] - s[p] >= 2:
            a.append(s[i])
            p = i
    s = list(map(lambda x: x - ord('a') + 1, a))
    p = -1 if len(s) < k else functools.reduce(lambda a, b: a + b, s[:k])
    print("{}".format(p))

def _545D_Queue():
    n = int(input())
    s = list(map(int, input().strip().split()))
    swap = sorted(s)
    r, t = 0, 0

    for i in range(n):
        if swap[i] >= t:
            r += 1
            t += swap[i]

    print(r)

def _12C_Fruits_Solved_By_List():
    n, m = list(map(int, input().strip().split()))
    a, b, c = list(map(int, input().strip().split())), list(), 1
    r, min_val, max_val = list(), 0, 0

    for i in range(m):
        b.append(input())

    a.sort()
    b.sort()

    if m > 1:
        for i in range(1, m):
            if b[i] != b[i - 1]:
                r.append((b[i - 1], c))
                c = 1
            else:
                c += 1
            if i == m - 1:
                r.append((b[i], c))

        r.sort(key=itemgetter(1), reverse=True)

        for i in range(len(r)):
            min_val += a[i] * r[i][1]
            max_val += a[n - i - 1] * r[i][1]
    else:
        min_val += a[0]
        max_val += a[n - 1]

    print("{0} {1}".format(min_val, max_val))

def _12C_Fruits_Solved_By_Dictionary():
    n, m = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    d = dict()

    for i in range(m):
        t = input()
        d[t] = d.get(t, 0) + 1

    a.sort()
    d = sorted(d.values(), reverse=True)

    for c in a, a[::-1]:
        print(sum(d[i] * c[i] for i in range(len(d))), end=' ')

def _257A_Sockets():
    n, m, k = list(map(int, input().strip().split()))
    a, b, i = list(map(int, input().strip().split())), 0, 0

    a.sort(reverse=True)

    if m <= k:
        print(b)
    else:
        while i < len(a):
            if m <= k:
                break
            if k > 0:
                k -= 1
            elif m > 0:
                m += 1
            m -= a[i]
            b += 1
            i += 1
        print("-1" if m > k else "{}".format(b))

def _381B_Sereja_and_Stairs():
    m = int(input())
    b = list(map(int, input().split()))
    s = sorted(set(b))
    d = dict()
    r = []
    # c = Counter(b)

    for i in b:
        d[i] = d.get(i, 0) + 1

    for k in s[:-1]:
        if d[k] > 1:
            r.append(k)

    print("{0}\n{1} {2}".format(len(s) + len(r), " ".join(map(str, s)), " ".join(map(str, r[::-1]))))

def _1041A_Heist():
    n = int(input())
    b, c = list(map(int, input().split())), 0

    b.sort()

    for i in range(1, n):
        c += b[i] - b[i - 1] - 1
    print(c)

def _1430B_Barrels():
    INPUT = lambda: list(map(int, input().split()))
    t = int(input())

    for i in range(t):
        n, k = INPUT()
        a = INPUT()
        a.sort(reverse=True)
        print(sum(x for x in a[:k + 1]))

def _405A_Gravity_Flip():
    Y = lambda: list(map(int, input().split()))
    n = int(input())
    a = Y()
    a.sort()
    print(" ".join(list(map(str, a))))

def _1144B_Parity_Alternated_Deletions_By_Built_In_Filter():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())
    even, odd = list(), list()

    n = N()
    a = Y()
    a.sort()

    even = list(filter(lambda x: x % 2 == 0, a))
    odd = list(filter(lambda y: y % 2 == 1, a))
    h = len(even) - len(odd)

    if h == 0 or h == 1:
        print(0)
    else:
        print(sum(even[:h - 1]) if h > 0 else sum(odd[:(h*-1) - 1]))

def _1144B_Parity_Alternated_Deletions_By_Built_In_Pop_List():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())
    even, odd = list(), list()

    n = N()
    a = Y()
    a.sort()

    for _ in a:
        even.append(_) if _ % 2 == 0 else odd.append(_)
    while len(even) and len(odd):
        even.pop()
        odd.pop()
    if len(even):
        even.pop()
    if len(odd):
        odd.pop()
    print("{}".format(sum(even) + sum(odd)))

def _1216B_Shooting():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    n = N()
    a = Y()
    r = 0
    a = [(-a[k], k % len(a) + 1) for k in range(n)]
    a.sort()
    for i in range(n):
        r += -a[i][0] * i + 1
    print("{0}\n{1}".format(r, " ".join(map(str, [x[1] for x in a]))))

def _16B_Burglar_And_Matches():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    n, m = Y()
    a, r = list(), 0

    for i in range(m):
        a.append(Y())
    a.sort(key=itemgetter(1), reverse=True)
    # Sort by multiple keys
    # a.sort(key=lambda i: (i[1], i[0]), reverse=True)

    for i in a:
        if n <= 0:
            break
        h = n - i[0]
        r += i[0] * i[1] if h > 0 else n * i[1]
        n -= i[0]

    print(r)

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