import math
import os
import random
import re
import sys
import functools as ft
from operator import itemgetter, attrgetter
from collections import Counter
from itertools import combinations

def _722B_Verse_Pattern_1st_Implement():
    # Solved by dictionary
    cin = input
    n = int(cin())
    a = [int(i) for i in input().split()]
    d = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0, 'y': 0}

    for i in range(n):
        for c in cin():
            if c in d.keys():
                d[c] += 1
        if sum(d.values()) != a[i]:
            print("NO")
            break
        d = d.fromkeys(d, 0) # Reset values of dictionary
    else:
        print("YES")

def _722B_Verse_Pattern_2nd_Implement():
    # Solved by string count()
    cin = input
    n = int(cin())
    a = [int(i) for i in input().split()]

    for i in range(n):
        t = cin()
        if a[i] != sum(t.count(c) for c in "ueoaiy"):
            print("NO")
            break
    else:
        print("YES")

def _1121B_1st_Implement():
    cin = input
    n = int(cin())
    a = [int(i) for i in input().split()]
    b = list()

    for i in range(n - 1):
        for j in range(i + 1, n):
            b.append(a[i] + a[j])

    # Sort dictionary by value
    # b = sorted(Counter(b).items(), key=lambda x: x[1])
    # print(b[-1][1])

    # Get max of dictionary values
    print(max(Counter(b).values))

def _1121B_2nd_Implement():
    cin = input
    n = int(cin())
    a = [int(i) for i in input().split()]
    print(max(Counter(map(sum, combinations(a, 2))).values()))

def _31A_Worms_Evolution():
    cin = input
    n = int(cin())
    a = [int(i) for i in input().split()]
    # itertools.combinations() return possible tuples
    b = list(combinations(range(n), 2))
    for i in range(n):
        for c in b:
            if a[i] == a[c[0]] + a[c[1]]:
                print("%s %s %s" % (i + 1, c[0] + 1, c[1] + 1))
                exit()
    else:
        print(-1)

def _47B_Coins_1st_Implement():
    a = {0: 0, 1: 0, 2: 0}
    for i in range(3):
        t = input()
        if t.count(">"):
            a[ord(t[0]) % 65] += 1
        else:
            a[ord(t[2]) % 65] += 1
    else:
        if max(a.values()) != 2:
            print("Impossible")
            exit()
    a = sorted(a.items(), key=lambda x: x[1])
    print("".join(chr(a[i][0] + 65) for i in range(3)))

def _47B_Coins_2nd_Implement():
    a = [0] * 3
    for i in range(3):
        t = input()
        a["ABC".index(t[0] if t[1] == ">" else t[2])] += 1
    else:
        if max(a) != 2:
            print("Impossible")
            exit()
    print("".join("ABC"[a.index(i)] for i in range(3)))

def _920B_Tea_Queue():
    cin = input
    t = int(cin())

    while t > 0:
        n = int(cin())
        a, cnt = [0] * n, 0
        for i in range(n):
            l, r = map(int, cin().split())
            cnt += l - cnt if l > cnt else 1
            if r >= cnt:
                a[i] += cnt
            else:
                cnt -= 1
        print(*a)
        t -= 1

def _check_string_digits():
    s = input()
    # Regex check digits
    regex = "^[0-9]+$" # Start with digit and end with digit
    t = re.search(regex, s)
    print("YNEOS"[t is None::2])

    # Iteration check digits
    for c in s:
        if ord(c) < 48 or ord(c) > 57:
            print("NO")
            break
    else:
        print("YES")

def _958B_Switches_And_Lamps():
    cin = input
    n, m = map(int, cin().split())
    s, l, f = [[] for _ in range(n)], [0] * m, 0

    for i in range(n):
        t = cin()
        for j in range(m):
            if t[j] == "1":
                l[j] += int(t[j])
                s[i].append(j)
    for i in range(n):
        r = set(l[c] - 1 for c in s[i])
        if not 0 in r:
            f = not f
            break
    print("YNEOS"[not f::2])

def _960A_Check_The_String():
    cin = input
    s = list(cin())
    a = [0] * 3
    if len(set(s)) < 3 or s != sorted(s):
        print("NO")
    else:
        for c in s:
            a["abc".index(c)] += 1
        print("YNEOS"[not (a[0] == a[2] or a[1] == a[2])::2])

def _828A_Restaurant_Tables():
    cin = input
    n, a, b = map(int, cin().split())
    p = [int(i) for i in cin().split()]
    cnt, c = 0, 0

    for t in p:
        if t == 1:
            if a: a -= 1
            elif b:
                b -= 1
                c += 1
            elif c:
                c -= 1
            else: cnt += t
        else:
            if b: b -= 1
            else: cnt += t
    print(cnt)

def _208D():
    cin = input
    n = int(cin())
    a = [int(v) for v in cin().split()]
    b = [int(v) for v in cin().split()]
    c, r = [0] * 5, 0
    for i in a:
        r += i
        for j in range(4, -1, -1):
            c[j] += r // b[j]
            r %= b[j]
    print("%s\n%d" % (" ".join(str(i) for i in c), r))

def _413A_Data_Recovery():
    cin = input
    n, m, ln, rn = map(int, cin().split())
    a = [int(v) for v in cin().split()]

    if ln < min(a) <= max(a) < rn:
        print(["Incorrect", "Correct"][n - m > 1])
    else:
        print(["Correct", "Incorrect"][min(a) < ln or max(a) > rn])

def _1352D():
    cin = input
    t = int(cin())

    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        mx, i, j, l, cnt = 0, -1, n, 1, 0
        alice, bob = 0, 0

        while i < j:
            s = 0
            if l:
                # Alice moves
                i += 1
                while i < j:
                    s += a[i]
                    if s > mx:
                        break
                    i += 1
                alice += s
            else:
                # Bob moves
                j -= 1
                while j > i:
                    s += a[j]
                    if s > mx:
                        break
                    j -= 1
                bob += s
            cnt += 1 * (s > 0)
            mx = s
            l = not l
        print(cnt, alice, bob)
        t -= 1

def _99B_Help_Chef_Gerasim():
    n = int(input())
    s = lambda v, a, b: "%s ml. from cup #%s to cup #%s." % (v, a, b)
    a, d, ans = list(), dict(), ["Exemplary pages.", "Unrecoverable configuration."]

    for i in range(n):
        k = int(input())
        a.append(k)
        d[k] = d.get(k, 0) + 1

    k, t = -1, 0
    d = sorted(d.items(), key=itemgetter(1))

    while k < n - 1 and d[k + 1][1] == 1:
        k += 1
        t += d[k][0]

    if len(d) == 1:
        print(ans[0])
    elif (len(d) == 2 or len(d) == 3) and k > 0:
        mx, mn = max(d[:k + 1]), min(d[:k + 1])
        if k == 1 and (k == len(d) - 1 and t % 2 == 0) or (k == len(d) - 2 and abs(mx[0] - d[k + 1][0]) + mn[0] == d[k + 1][0]):
            print(s(abs(mx[0] - mn[0]) // 2 if k == len(d) - 1 else abs(mx[0] - d[k + 1][0]), a.index(mn[0]) + 1, a.index(mx[0]) + 1))
        elif k == 2 and k == len(d) - 1 and t // 3 == t - (mx[0] + mn[0]) and t - (mx[0] + mn[0]) == 2 * (mx[0] + mn[0]) - t:
            print(s(t - (mx[0] + mn[0]), a.index(mn[0]) + 1, a.index(mx[0]) + 1))
        else:
            print(ans[1])
    else:
        print(ans[1])

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