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

def _263B_Squares():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())

    n, k = P()
    a = Y()
    a.sort(reverse=True)

    print("{0} {1}".format(a[k - 1], 0) if k <= n else -1)

def _242B_Big_Segment():
    P = lambda: map(int, input().split())
    N = lambda: int(input())

    n = N()
    MIN, MAX = 10 ** 9 + 1, 0
    a, f = list(), False

    for i in range(n):
        l, r = P()
        MIN = min(l, MIN)
        MAX = max(r, MAX)
        a.append((l, r))
    for i in range(n):
        if a[i][0] == MIN and a[i][1] == MAX:
            f = True
            break
    print(i + 1 if f else -1)

def _166A_Rank_List_By_Counter():
    P = lambda: map(int, input().split())

    n, k = P()
    a, r = list(), 0

    for i in range(n):
        a.append([int(x) for x in input().split()])
    a.sort(key=lambda item: (item[0], -item[1]), reverse=True)
    b = Counter(a)
    b = b.values()
    for i in b:
        r += i
        if k <= r:
            print(i)
            break

def _166A_Rank_List_By_Built_In_Count():
    P = lambda: map(int, input().split())

    n, k = P()
    a = list()

    for i in range(n):
        a.append([int(x) for x in input().split()])
    a.sort(key=lambda item: (item[0], -item[1]), reverse=True)
    print(a.count(a[k - 1]))

def _1228A_Distinct_Digits():
    P = lambda: map(int, input().split())

    l, r = P()
    f = False

    for i in range(l, r + 1):
        s = str(i)
        f = len(set(s)) == len(s)
        if f:
            break
    print(i if f else -1)

def _1230A():
    Y = lambda: list(map(int, input().split()))

    a = Y()
    s = sum(a)
    if s % 2:
        print("NO")
    else:
        s /= 2
        b = [int(s - x) for x in a if int(s - x) in a]
        print("YES" if (int(s) in a) or (len(b) == len(a)) else "NO")

def _1005A_Tanya_And_Stairways():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    n = N()
    a, b = Y(), list()
    l, r = 0, 0

    for i in range(1, n):
        if a[i] == 1:
            b.append(a[i - 1])
    b.append(a[-1])
    print("{0}\n{1}".format(len(b), " ".join([str(x) for x in b])))

def _255A_Workout():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())
    N = lambda: int(input())

    n = N()
    a = Y()
    r = [0, 0, 0]

    for i in range(n):
        r[i % 3] += a[i]
    b = max(r)
    if r[0] == b:
        print("chest")
    elif r[1] == b:
        print("biceps")
    else:
        print("back")

def _344A_Magnets():
    N = lambda: int(input())

    n = N()
    p, r = 0, 1

    for i in range(n):
        tmp = int(input())
        r += p and p != tmp
        p = tmp
    print(r)

def _448A_Rewards():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    a = Y()
    b = Y()
    n = N()

    r = math.ceil(sum(a) / 5) + math.ceil(sum(b) / 10)
    print("YES" if r <= n else "NO")

def _999A_Mishka_And_Contest():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())

    n, k = P()
    a = Y()
    l, r = 0, n - 1

    while l < r and (a[l] <= k or a[r] <= k):
        if a[l] <= k:
            l += 1
        if a[r] <= k:
            r -= 1
    print("{}".format((n if a[r] <= k else n - 1) if r == l else (n - (r - l + 1))))

def _287A_IQ_Test():
    a = list()
    f = False

    for i in range(4):
        a.append(input())
    for i in range(3):
        for c in range(3):
            r = Counter([a[i][c], a[i + 1][c], a[i][c + 1], a[i + 1][c + 1]])
            if r['#'] != 2 and r['.'] != 2:
                f = True
                break
        if f:
            break
    print("YES" if f else "NO")

def _66B_Petya_And_Countryside():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())
    N = lambda: int(input())

    n = N()
    a = Y()
    l, r, down, MAX = 0, 1, False, 0

    for i in range(1, n):
        if a[i] > a[i - 1]:
            if not down:
                r += 1
            else:
                if r > MAX:
                    MAX = r
                r = i - l + 1
                down = False
        else:
            if a[i] < a[i - 1]:
                l = i
            r += 1
            down = True
    print(r if r > MAX else MAX)

def _339B_Xenia_And_Ringroad():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())

    n, m = P()
    a = Y()
    d = 0

    for i in range(m):
        if i > 0 and a[i] < a[i - 1]:
            d += 1
    print(a[m - 1] + n * d - 1)

def _379A_New_Year_Candles():
    P = lambda: map(int, input().split())

    a, b = P()
    r, d = a, 0

    while True:
        d = int(a / b) + a % b
        r += d - a % b
        if d < b:
             break
        a = d
    print(r)

def _237A_Free_Cash():
    P = lambda: map(int, input().split())
    N = lambda: int(input())

    n = N()
    a = list()
    MAX = 1

    while n > 0:
        h, m = P()
        a.append((h, m))
        n -= 1
    b = Counter(a)
    for i in b.values():
        if i > MAX:
            MAX = i
    print(MAX, max(b.values()))

def _757A_Gotta_Catch():
    # Solved by dictionary
    d = { 'B': 0, 'u': 0, 'l': 0, 'b': 0, 'a': 0, 's': 0, 'r': 0 }
    for i in input():
        if i in d.keys():
            d[i] += 1
    d['a'] = int(d['a'] / 2)
    d['u'] = int(d['u'] / 2)
    print(min(d.values()))
    # Solved by string count characters
    s = input()
    print(min([s.count('B'), int(s.count('u') / 2), s.count('l'), s.count('b'), int(s.count('a') / 2), s.count('s'), s.count('r')]))

def _1059A_Cashier():
    P = lambda: map(int, input().split())

    n, L, a = P()
    r, p = 0, 0

    for i in range(n):
        t, l = P()
        r += int(t / a) if i == 0 else int((t - p) / a)
        p = t + l
    print(int((L - p) / a) + r)

def _583A_Asphalting_Roads():
    P = lambda: map(int, input().split())
    N = lambda: int(input())

    n = N()
    H, V = dict(), dict()
    r = ""

    n *= n

    for i in range(n):
        h, v = P()
        if not (h in H.keys() or v in V.keys()):
            H[h] = H.get(h, True)
            V[v] = V.get(v, True)
            r += str(i + 1) + " "
    print(r.strip())

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