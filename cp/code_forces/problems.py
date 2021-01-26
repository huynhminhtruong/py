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

def _75A_Life_Without_Zeros():
    N = lambda: int(input())

    a = N()
    b = N()

    r_a = ''.join([i for i in str(a) if i != '0'])
    r_b = ''.join([i for i in str(b) if i != '0'])
    r_c = ''.join([i for i in str(a + b) if i != '0'])

    print('YNEOS'[int(r_a) + int(r_b) != int(r_c)::2])

def _733A_By_Without_ZIP_Built_In():
    a = input()
    a = ' ' + a + ' '
    mx, l, vowels = 0, 0, 'AEIOUY'

    for i in range(len(a)):
        if a[i] in vowels:
            mx = max(i - l, mx)
            l = i
    print(max(mx, len(a) - l - 1))

def _733A_By_ZIP_Built_In():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())
    N = lambda: int(input())

    # enumerate return list of tuples (index, value)
    # enumerate using for any object that supports iteration
    a = [i for i, c in enumerate('A' + input() + 'A') if c in 'AEIOUY']

    # zip merges multiple iterator like list, tuples
    # ex: 
    # a = (1, 2, 3, 4, 5)
    # b = (1, 2, 3, 4, 5)
    # zip(a, b) = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5))
    # zip(a, a[1:]) = ((1, 2), (2, 3), (3, 4), (4, 5))
    print(max(b - a for a, b in zip(a, a[1:])))

def _441A_Valera_And_Antique_Items():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())

    n, v = P()
    r = list()

    for i in range(n):
        a = Y()
        m = min(a[1:])
        if v > m:
            r.append(i + 1)
    print("{0}".format(len(r)))
    print(*r)

def _1203A_Circle_Of_Students():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    q = N()

    while q > 0:
        n = N()
        a = Y()
        r = 0
        for i in range(1, n):
            if abs(a[i] - a[i - 1]) > 1:
                r += 1
        if r > 1 or (r == 1 and abs(a[n - 1] - a[0]) > 1):
            print("NO")
        else:
            print("YES")
        q -= 1

def _404A_Valera_And_X_By_List():
    N = lambda: int(input())

    n = N()
    a, b, d, r = list(), list(), 2, 0

    for i in range(n):
        s = input()
        if i < int(n / 2) + (n % 2):
            r = n - 1 - i
        else:
            r = i - d
            d += 2
        a.extend([s[i], s[r]] if i != r else s[i])
        b.extend([s[j] for j in range(n) if not (s[j] in (s[i], s[r]))])
    r, d, a, b = len(a), len(b), len(Counter(a)), len(Counter(b))
    print("YNEOS"[not ((a != 1 or b != 1) or (n**2 - r != d))::2])

def _404A_Valera_And_X():
    N = lambda: int(input())

    n = N()

    s = [input() for _ in range(n)]
    x, nx = s[0][0], s[0][1]
    r = (x != nx)

    for i in range(n):
        for j in range(n):
            if j == i or j == n - 1 - i:
                if s[i][j] != x:
                    r = 0
            else:
                if s[i][j] != nx:
                    r = 0
        if not r:
            break
    print("YNEOS"[not r::2])

def _334A():
    N = lambda: int(input())

    n = N()
    a = list()

    # Using // to cast float to int
    for i in range(n**2 // 2):
        a.extend([i + 1, n**2 - i])
        if (i + 1) % (n / 2) == 0:
            print(*a)
            a.clear()

def _1253A_Single_Push():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    t = N()

    while t > 0:
        n = N()
        a = Y()
        b = Y()
        l, r, ok = -1, -1, 1
        for i in range(n):
            if b[i] - a[i] > 0:
                if l < 0:
                    l = i
                r = i
            elif b[i] - a[i] != 0:
                ok = 0
        if ok and len(Counter([b[i] - a[i] for i in range(l, r + 1)])) > 1:
            ok = 0
        print("YNEOS"[not ok::2])
        t -= 1

def _139A_Petr_And_Book():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    n = N()
    a = Y()
    i = 0

    while n - a[i] > 0:
        n -= a[i]
        i = 0 if i == 6 else i + 1
    print(i + 1)

def _165A_Supercentral_Point():
    P = lambda: map(int, input().split())
    N = lambda: int(input())

    n = N()
    a, cnt = list(), 0
    for _ in range(n):
        x, y = P()
        a.append((x, y))
    for i in range(n):
        x, y = a[i][0], a[i][1]
        l, r, u, d = 0, 0, 0, 0
        for j in range(n):
            if x == a[j][0] and y != a[j][1]:
                if y < a[j][1]:
                    u = 1
                else:
                    d = 1
            if y == a[j][1] and x != a[j][0]:
                if x < a[j][0]:
                    r = 1
                else:
                    l = 1
        cnt += (l and r and u and d)
    print(cnt)

def _1133A():
    Y = lambda: list(map(int, input().split(":")))

    a = Y()
    b = Y()
    r = (b[0]*60 + b[1]) - (a[0]*60 + a[1])
    r = r / 2 + a[0]*60 + a[1]
    x, y = int(r / 60), int(r % 60)
    print("{0}:{1}".format(str(x) if x > 9 else "0" + str(x), str(y) if y > 9 else "0" + str(y)))

def _1100A_First_Implement():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())

    n, k = P()
    a = Y()
    r, s, mx = 0, 0, 0
    for i in range(n):
        for j in range(n):
            if j % k != i % k:
                if a[j] < 0:
                    s += 1
                else:
                    r += 1
        mx = max(mx, abs(r - s))
        r, s = 0, 0
    print(mx)

def _1100A_Second_Implement():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())

    n, k = P()
    a = Y()
    r, s, mx = 0, 0, 0
    for _ in a:
        if _ < 0:
            s += 1
        else:
            r += 1
    for i in range(k):
        mx = max(abs((s - a[i::k].count(-1)) - (r - a[i::k].count(1))), mx)
    print(mx)

def _1073B_Vasya_And_Books():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())
    N = lambda: int(input())

    n = N()
    a = Y()
    b = Y()
    top, r, c = 0, [False]*(n + 1), []

    for i in range(n):
        if r[b[i]]:
            c.append(0)
        else:
            nxt = top
            while nxt < n and b[i] != a[nxt]:
                r[a[nxt]] = True
                nxt += 1
            c.append(nxt - top + 1)
            r[b[i]] = True
            top = nxt + 1
    print(*c)

def _991A():
    P = lambda: map(int, input().split())

    a, b, c, n = P()
    r = 0 if a < c or b < c else n - (a + b - c)
    print(-1 if r <= 0 else r)

def _670B_Game_Of_Robots_First_Implement():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())

    n, k = P()
    s, a = [int(i * (i + 1) / 2) for i in range(n + 1)], Y()

    for i in range(len(s) - 1, 0, -1):
        if k >= s[i]:
            p = k - s[i] - 1 if k > s[i] else k - s[i - 1] - 1
            print(a[p])
            break

def _670B_Game_Of_Robots_Second_Implement():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())

    n, k = P()
    s, i, a = 0, 1, Y()

    while s + i < k:
        s += i
        i += 1
    print(a[k - s - 1])

def _465B_Inbox_First_Implement():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    n = N()
    a = Y()
    i, j = 0, n - 1

    while i < j and not (a[i] and a[j]):
        if not a[i]:
            i += 1
        if not a[j]:
            j -= 1
    f, cnt = 0, a[i:j+1].count(1)
    for i in a[i:j+1]:
        if not i:
            f = 1
        elif f:
            cnt += 1
            f = 0
    print(cnt)

def _465B_Inbox_Second_Implement():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    n = N()
    a = Y()
    f, cnt = 0, 0
    
    for i in a:
        if i:
            cnt += 1
            f = 1
        else:
            if f:
                cnt += 1
            f = 0
    print(cnt if (a[n - 1] or not cnt) else cnt - 1)

def _939B_Hamster_Farm():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())

    n, k = P()
    a = Y()
    p = 0

    for i in range(k):
        if n % a[i] < n % a[p]:
            p = i
    # Use floor division (//) to ignore values after the decimal point
    print("%s %s" % (p + 1, n // a[p]))

def _831A_Unimodal_Array():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    n = N()
    a = Y()
    f, i, j = 0, 0, n - 1

    while i < n - 1 and a[i] < a[i + 1]:
        i += 1
    while j > 0 and a[j] < a[j - 1]:
        j -= 1
    f = (j - i + 1 == a[i:j+1].count(a[i]))
    print("YNEOS"[not f::2])

def _435A():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())

    n, m = P()
    a = Y()
    i, s, cnt = 0, 0, 1

    while i < n:
        if s + a[i] <= m:
            s += a[i]
            i += 1
        else:
            cnt += 1
            s = 0
    print(cnt)

def _849A():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    n = N()
    a = Y()

    f = 0 if not (n % 2 and a[0] % 2 and a[n - 1] % 2) else 1
    print("YNEOS"[not f::2])

def _604A_Uncowed_Forces():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())

    m = Y()
    w = Y()
    hs, hu = P()
    pt, ans = [500, 1000, 1500, 2000, 2500], 0

    mx_pt = lambda x, m, w: max((30 * x) / 100, (1 - m / 250) * x - 50 * w)
    for i in range(5):
        ans += mx_pt(pt[i], m[i], w[i])
    ans = ans + (hs * 100 - hu * 50)
    print(int(ans))

def _count_digits(n) -> int:
    s, i = 0, 1
    while i < n + 1:
        s += n - i + 1
        i *= 10
    return s

def _620B():
    P = lambda: map(int, input().split())

    a, b = P()
    cnt, l = 0, [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    n = str(list(range(a, b + 1)))
    
    for i in range(10):
        cnt += l[i] * n.count(str(i))
    print(cnt)

def _920A():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())
    N = lambda: int(input())

    t = N()

    while t > 0:
        n, k = P()
        a = Y()
        mx, s = a[0] - 1, a[0]

        for i in range(1, k):
            mx = max(mx, (a[i] - s) // 2)
            s = a[i]
        mx = max(mx, n - s) + 1
        print("%s" % (mx if not (n == k) else 1))

        t -= 1

def _5A():
    p, ans = 0, 0

    try:
        while True:
            t = input()
            c = t.find(":")
            if c != -1:
                ans += p * (len(t) - c - 1)
            else:
                p += 1 if t[0] == "+" else -1
    except:
        pass
    print(ans)

def _368B():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())
    N = lambda: int(input())

    n, d = P()
    a = Y()
    m = N()

    a.sort()
    mx = min(n, m)
    ans = sum(a[:mx])
    if mx == n:
        ans += (n - m) * d
    print(ans)

def _724A_Checking_The_Calendar():
    a = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    c = input()
    n = input()
    # Difference day of the week between adjective months are (0, 2, 3)
    print("YNEOS"[not ((a.index(n) - a.index(c) + 7) % 7 in (0, 2, 3))::2])

def _400A_Inna_And_Choose_Options():
    N = lambda: int(input())

    t = N()
    a, r = [1, 2, 3, 4, 6, 12], list()

    while t > 0:
        s = input()
        for i in a:
            for j in range(12//i):
                if s[j::12//i].count("X") == i:
                    r.append("%sx%s" % (i, 12//i))
                    break
        print(len(r), *r)
        r.clear()
        t -= 1

def _725A_Jumping_Ball():
    N = lambda: int(input())

    n = N()
    s = input()
    l, r, ans = 0, 0, 0

    if not (s[0] == '>' and s[len(s) - 1] == '<'):
        l = s.find('>')
        r = s[::-1].find('<')
        ans = n if l == -1 or r == -1 else l + r
    print(ans)

def _1054B_Appending_Mex():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    n = N()
    a = Y()
    ans, mx = 0, -1

    for i in range(n):
        if not(a[i] <= mx + 1):
            ans = i + 1
            break
        else:
            mx = max(mx, a[i])
    print(-1 if (not ans) else ans)

def _106A_Card_Game():
    c = input()
    a = ["6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    b = ["S", "H", "D", "C"]
    x, y = input().split()    

    if b.index(x[1]) == b.index(y[1]):
        ans = 0 if a.index(x[0]) <= a.index(y[0]) else 1
    else:
        ans = 0 if x[1] != c else 1

    print("YNEOS"[not ans::2])

def _641A():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    n = N()
    s = input()
    a = Y()
    nxt, ans = 0, 0

    for i in range(n):
        nxt += a[nxt] if s[nxt] == '>' else -a[nxt]
        # nxt += [a[nxt], -a[nxt]][s[nxt] == '<']
        if nxt >= n or nxt < 0:
            ans = 2
            break
    print("INFINITE"[ans:])

def _56A_Bar():
    N = lambda: int(input())

    n = N()
    cnt, a = 0, ["ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN", "RUM", "SAKE", "TEQUILA", "VODKA", "WHISKEY", "WINE"]

    while n > 0:
        t = input()
        cnt += ((t.isnumeric() and int(t) < 18) or (t in a))
        n -= 1
    print(cnt)

def _127B_Canvas_Frames():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    n = N()
    a = Y()
    d = dict()

    for i in range(n):
        d[a[i]] = d.get(a[i], 0) + 1
    for v in d.keys():
        d[v] = d[v]//2
    print(sum(d.values())//2)

def _182B_Vasyas_Calendar():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    d = N()
    n = N()
    a = Y()
    cnt = 0

    for i in range(n - 1):
        cnt += d - a[i]
    print(cnt)

def _420A_Start_Up():
    t = input()
    s = "AHIMOTUWVXY"
    ans = 1

    for i in t:
        if s.find(i) == -1:
            ans = 0
            break
    print("YNEOS"[not (ans and t == t[::-1])::2])

def _660B_Seating_On_Bus():
    P = lambda: map(int, input().split())

    n, m = P()
    l = list()

    for i in range(m):
        if (i + 1) <= 2 * n:
            l.append([i + 1])
        else:
            l[i % (2 * n)].append(i + 1)
    for i in l:
        print(*i[::-1], end=" ")

def _35A_Shell_Game():
    # Requires input and output files
    cin = open("input.txt","r")
    cout = open("output.txt","w")
    n = int(cin.readline())

    for i in range(3):
        j, k = map(int, cin.readline().split())
        if n in (j, k):
            n = j if n == k else k
    cout.write(str(n))

def _14B_Young_Photographer():
    P = lambda: map(int, input().split())

    n, x = P()
    a, b = -1, 1001

    for i in range(n):
        l, r = P()
        a = max(a, min(l, r))
        b = min(b, max(l, r))
    print(-1 if b < a else [min(abs(x - a), abs(x - b)), 0][x >= a and x <= b])

def _1090M_The_Pleasant_Walk():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())

    n, k = P()
    a = Y()
    nxt, mx = 0, 0

    for i in range(1, n):
        if a[i] == a[i - 1]:
            mx = max(mx, i - nxt)
            nxt = i
    print(max(mx, n - nxt))

def _1177A_Digits_Sequence():
    N = lambda: int(input())

    n = N()
    cnt, i = 0, 1

    while cnt + int(math.log10(i) + 1) < n:
        cnt += int(math.log10(i) + 1)
        i += 1
    print(str(i)[n - cnt - 1])

def _958B1_Maximum_Control():
    P = lambda: map(int, input().split())
    N = lambda: int(input())

    n = N()
    a = [0]*n

    while n > 1:
        u, v = P()
        a[u - 1] += 1
        a[v - 1] += 1
        n -= 1
    # Comprehension in Python
    print(len([i for i in range(len(a)) if a[i] < 2]))

def _125B_Simple_XML_1st_Implement():
    s = input()
    lv, pad, nst = 0, -1, 1

    for i in range(len(s)):
        if s[i] == "<":
            pad += nst
            nst = 1
        elif s[i] == "/":
            pad -= 1
            nst = 0
        elif s[i] == ">":
            print(" "*(2 * pad) + s[lv:i+1])
            lv = i + 1

def _125B_Simple_XML_2st_Implement():
    s = input().split(">")
    pad = -1

    for c in s:
        if not len(c):
            continue
        if c[1] == "/":
            print(" "*(2*pad) + c + ">")
            pad -= 1
        else:
            pad += 1
            print(" "*(2*pad) + c + ">")

def _478A_Initial_Bet():
    a = list(map(int, input().split()))
    print(-1 if ((not sum(a)) or (sum(a) % 5)) else sum(a)//5)

def _719A_Countryside_1st_Implement():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    n = N()
    a = Y()
    k, ans = -1, -1

    for i in range(n, 0, -1):
        if a[i - 1] == 0:
            ans = 1
            break
        if a[i - 1] == 15:
            ans = 0
            break
        if k >= 0:
            ans = not (a[i - 1] > k)
            break
        else:
            k = a[i - 1]
    print(["DOWN", "UP", -1][ans if ans != -1 else 2])

def _719A_Countryside_2nd_Implement():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    n = N()
    a = Y()

    if a[-1] == 0:
        print("UP")
    elif a[-1] == 15:
        print("DOWN")
    elif n == 1:
        print(-1)
    else:
        print(["DOWN", "UP"][a[-2] < a[-1]])

def _570A_Elections():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())

    n, m = P()
    c = [0]*n

    while m > 0:
        a = Y()
        c[a.index(max(a))] += 1
        m -= 1
    print(c.index(max(c)) + 1)

def _471A_MUH_And_Sticks_1st_Implement():
    Y = lambda: list(map(int, input().split()))

    a = Y()
    d = dict()

    for i in a:
        d[i] = d.get(i, 0) + 1
    mx = max(d.values())
    if mx >= 4:
        a = [i for i in d.keys() if d[i] != mx]
        print(["Bear", "Elephant"][not len(a) or d[a[-1]] == 2])
    else:
        print("Alien")

def _471A_MUH_And_Sticks_2nd_Implement():
    Y = lambda: list(map(int, input().split()))

    a = Y()
    a = sorted(a, key=a.count)
    print("Alien" if a[2] != a[-1] else "Elephant" if a[0] == a[1] else "Bear")

def _227B_Effective_Approach():
    Y = lambda: list(map(int, input().split()))
    N = lambda: int(input())

    n = N()
    a = Y()
    ind = [0]*n
    m = N()
    b = Counter(Y())
    v, p = 0, 0

    for i in range(n):
        ind[a[i] - 1] = i

    for i in b:
        cnt = ind[i - 1]
        v += (cnt + 1) * b[i]
        p += (n - cnt) * b[i]
    print(v, p)

def _799A_Carrot_Cakes():
    P = lambda: map(int, input().split())

    n, t, k, d = P()
    
    # Remaining of cakes after d // t minutes
    print("YNEOS"[not n - (d // t) * k > k::2])

def _259B_Little_Elephant_And_Magic_Square_1st_Implement():
    Y = lambda: list(map(int, input().split()))

    ans = list()
    a = [0]*3

    for i in range(3):
        ans.append(Y())
        a[i] += sum(ans[i])
    mx = max(a) + 1
    while sum([mx - a[i] for i in range(3)]) != mx:
        mx += 1
    for i in range(3):
        ans[i][i] = mx - a[i]
    print("\n".join([" ".join(["{}".format(i) for i in row]) for row in ans]))

def _259B_Little_Elephant_And_Magic_Square_2nd_Implement():
    # Comprehensions
    ans = [[int(i) for i in input().split()] for _ in range(3)]
    s = sum([sum(i) for i in ans]) // 2
    for i in range(3):
        ans[i][i] = s - sum(ans[i])
    # Comprehensions and join to print matrix
    print("\n".join([" ".join(["{}".format(i) for i in row]) for row in ans]))

def _433A_Kitahara_Harukis_Gift():
    n = int(input())
    w = [int(i) for i in input().split()]
    k, d = w.count(100), w.count(200)
    d *= 2 if k > 0 else 1
    print("YNEOS"[(k + d) % 2::2])

def _911A_Nearest_Minimums_1st_Implement():
    n = int(input())
    a = [int(i) for i in input().split()]
    mx, d = 0, 10**5 + 1

    for i in range(1, n):
        if a[i] < a[mx]:
            mx = i
            d = 10**5 + 1
            continue
        if a[i] == a[mx]:
            d = min(d, i - mx)
            mx = i
    print(d)

def _911A_Nearest_Minimums_2nd_Implement():
    n = int(input())
    a = [int(i) for i in input().split()]
    mx = min(a)
    a = [i for i in range(n) if a[i] == mx]
    d = [a[i] - a[i - 1] for i in range(1, len(a))]
    print(min(d))

def _1413B_A_New_Technique():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())
    N = lambda: int(input())

    t = N()

    while t > 0:
        n, m = P()
        a, order = list(), list()
        d = dict()

        for i in range(n):
            a = Y()
            d[a[0]] = d.get(a[0], a)
        for i in range(m):
            a = Y()
            if not d.get(a[0]) is None:
                order = a
        for i in order:
            print(*d[i])
            
        t -= 1

def _218B_Airport():
    Y = lambda: list(map(int, input().split()))
    P = lambda: map(int, input().split())

    n, m = P()
    a = Y()
    b = a.copy()
    x, y = 0, 0

    for i in range(n):
        a.sort()
        x += a[m - 1]
        if b[0] == 0:
            b[0] = 1001
        b.sort()
        y += b[0]
        a[m - 1] -= 1
        b[0] -= 1
    print(x, y)

def _365A_Good_Number():
    P = lambda: map(int, input().split())

    n, k = P()
    cnt = 0

    # Number contains all digits <= k
    for _ in range(n):
        s = input()
        b = [0] * (k + 1)
        for i in s:
            if int(i) <= k:
                b[int(i)] += 1 * (not b[int(i)])
        cnt += (sum(b) == k + 1)
    print(cnt)

def _548A_Mike_And_Fax():
    s = input()
    k = int(input())

    if len(s) % k:
        print("NO")
    else:
        d = len(s) // k
        cnt = 0
        for c in range(0, len(s), d):
            cnt += (s[c:c + d] == s[c:c + d][::-1])
        print("YNEOS"[not cnt == k::2])

def _495A_Digital_Counter():
    s = input()
    d = [2, 7, 2, 3, 3, 4, 2, 5, 1, 2]
    print(d[int(s[0])] * d[int(s[1])])

def _6B_Presidents_Office():
    n, m, c = input().split()
    a, s = list(), set()
    n, m = int(n), int(m)

    a = ["." * (m + 2)] + ["." + input() + "." for i in range(n)] + ["." * (m + 2)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i][j] == c:
                # top
                s.add(a[i - 1][j])
                # bot
                s.add(a[i + 1][j])
                # left
                s.add(a[i][j - 1])
                # right
                s.add(a[i][j + 1])
    s.discard(".")
    s.discard(c)
    print(len(s))

def _43B_Letter():
    s, t = input(), input()
    d, a = dict(), dict()

    for i in s:d[i] = d.get(i, 0) + 1
    for i in t:a[i] = a.get(i, 0) + 1

    for k in a.keys():
        if k != " " and (not k in d.keys() or d[k] < a[k]):
            print("NO")
            break
    else:
        print("YES")

def _556B_Case_Of_Fake_Numbers_1st_Implement():
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(1, n + 1):
        a = [(a[j] + 1) % n if not j % 2 else (a[j] - 1) % n for j in range(n)]
        cnt = ft.reduce(lambda x, y: x + y, [a[j] == j for j in range(n)])
        if cnt == n:
            print("YES")
            break
    else:
        print("NO")

def _556B_Case_Of_Fake_Numbers_2nd_Implement():
    n = int(input())
    a = list(map(int, input().split()))
    d = a[0] - n # Distance of the first element and round n that value of the first element equals 0

    for i in range(1, n):
        # Determine current number will be standing left or right round n
        if (a[i] + n + d) % n != i:
            print("NO")
            break
        d = -d
    else:
        print("YES")

def _1105A_Salem_And_Sticks():
    n = int(input())
    a = list(map(int, input().split()))
    p, cost = -1, 10**6 + 1

    for i in range(1, 101):
        mx = 0
        for k in a:
            # Calculate cost of a[k] into i then get cost of a[k] into consecutive of i
            mx += max(abs(k - i) - 1, 0)
        if mx < cost:
            cost = mx
            p = i
    print(p, cost)

def _The_Artful_Expedient():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    # Explaination: https://codeforces.com/blog/entry/55009
    print("Karen")

def _984B_Minesweeper():
    n, m = map(int, input().split())
    a = ["." * (m + 2)] + [".%s." % (input()) for _ in range(n)] + ["." * (m + 2)]
    b = [["."] * (m + 2) for i in range(n + 2)]

    convert = lambda c: 1 if str(c) == "." else c if str(c) == "*" else c + 1

    for i in range(1, n + 1):
        if "*" in set(a[i]):
            for d in range(m + 2):
                if a[i][d] == "*":
                    b[i][d] = "*" # has bomb
                    b[i][d - 1] = convert(b[i][d - 1]) # left
                    b[i][d + 1] = convert(b[i][d + 1]) # right
                    b[i - 1][d] = convert(b[i - 1][d]) # top
                    b[i - 1][d - 1] = convert(b[i - 1][d - 1]) # top left
                    b[i - 1][d + 1] = convert(b[i - 1][d + 1]) # top right
                    b[i + 1][d] = convert(b[i + 1][d]) # bot
                    b[i + 1][d - 1] = convert(b[i + 1][d - 1]) # bot left
                    b[i + 1][d + 1] = convert(b[i + 1][d + 1]) # bot right
    for i in range(1, n + 1):
        if a[i][1:m + 1] != "".join(["%s" % (i) for i in b[i]])[1:m + 1]:
            print("NO")
            break
    else:
        print("YES")

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