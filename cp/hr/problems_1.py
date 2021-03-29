import math
import os
import random
import re
import sys
import functools
from operator import itemgetter, attrgetter
from collections import Counter, defaultdict, namedtuple, OrderedDict as od, deque
from itertools import combinations, groupby, permutations

def hr_1():
    n = int(input())
    a = [chr(97 + c) for c in range(0, n)]

    for i in range(2 * n - 1):
        u = a[::-1][:(i % n + 1)] if i < n else a[(i % n + 1):][::-1]
        u.extend(u[::-1][1:])
        l = "".join(["-"] * ((4 * n - 3 - (2 * len(u) - 1))//2))
        print("%s%s%s" % (l, "-".join(u), l))

def hr_minion_game():
    s = input()
    l, r, n = 0, 0, len(s)

    for i, c in enumerate(s):
        if "AEIOU".find(c) >= 0: l += n - i
        else: r += n - i
    if l > r:
        print("Kevin", l)
    elif r > l:
        print("Stuart", r)
    else:
        print("Draw")

def hr_itertools_groupby():
    s = input()
    a, l = zip(s, s), list()
    for k, g in groupby(a, lambda x: x[0]):
        l.append((len(list(g)), int(k)))
    print(*l)

def hr_collections_defaultdict():
    n, m = map(int, input().split())
    df = defaultdict(list)

    for i in range(n):
        df[input()].append(i + 1)
    for i in range(m):
        s = " ".join(str(c) for c in df[input()])
        print([s, -1][not len(s)])

def hr_collections_namedtuple():
    n, col, std = int(input()), input().split().index("MARKS"), namedtuple("std", "x")
    print("%.2f" % (sum(c.x for c in [std(int(input().split()[col])) for _ in range(n)]) / n))

def hr_collections_ordereddict():
    n = int(input())
    d = od()

    for i in range(n):
        a = input().split()
        l = len(a)
        key = " ".join(a[i] for i in range(l - 1))
        d[key] = d.get(key, 0) + int(a[l - 1])
    for k, v in d.items():
        print(k, v)

def hr_count_words():
    n = int(input())
    d = od()

    for i in range(n):
        word = input()
        d[word] = d.get(word, 0) + 1
    print("%d\n%s" % (len(d.items()), " ".join(str(i) for i in d.values())))

def hr_collections_deque():
    n = int(input())
    d, p = deque(), ["append", "pop", "popleft", "appendleft"]

    for i in range(n):
        a = input().split()

        if len(a) > 1:
            if p.index(a[0]) == 0: d.append(a[1])
            else: d.appendleft(a[1])
        else:
            if p.index(a[0]) == 1: d.pop()
            else: d.popleft()
    print(*d)

def hr_reduce_fraction():
    n = int(input())
    a = [Fraction(*[int(i) for i in input().split()]) for _ in range(n)]
    r = ft.reduce(lambda x, y: x * y, a)
    print(r.numerator, r.denominator)

def hr_sort_itemgetter():
    n, m = map(int, input().split())
    a = [[int(i) for i in input().split()] for _ in range(n)]
    k = int(input())
    a.sort(key=itemgetter(k))
    print("\n".join(" ".join(str(i) for i in c) for c in a))

def hr_regex():
    n = int(input())
    regex = "[#]+[a-fA-F0-9]{3,6}"
    a, f = list(), False
    for i in range(n):
        t = input()
        if t.count("{") > 0 or t.count("}") > 0:
            f = not f
        elif f:
            a.extend(filter(lambda x: 4 <= len(x) < 9, re.findall(regex, t)))
    print("\n".join(a))

def hr_regex_email():
    n = int(input())
    regex = "^[a-zA-Z]+[a-z0-9\._-]+[@][a-zA-Z]+[.][a-zA-Z]{1,3}$"
    for i in range(n):
        t = input()
        address = parseaddr(t)
        g = re.search(regex, address[1])
        if g:
            print("ans: %s" % t)

def hr_regex_phonenumber():
    n = int(input())
    regex = r"^[789][0-9]{9}$"
    for i in range(n):
        t = input()
        r = re.search(regex, t)
        print("YNEOS"[not r::2])

def hr_regex_check_character_duplicate():
    n = int(input())
    regex = re.compile('^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z0-9])(?!.*\\1)){10}$')
    for i in range(n):
        t = input()
        r = regex.match(t)
        print(["Valid", "Invalid"][r is None])
    # explaination: https://stackoverflow.com/questions/51358885/regex-no-character-should-repeat/51359047

def hr_collections_counter():
    x = int(input())
    s = list(map(int, input().split()))
    s = Counter(s)
    n, r = int(input()), 0
    for i in range(n):
        a, b = map(int, input().split())
        r += b * (s[a] > 0)
        s[a] -= 1 * (s[a] > 0)
    print(r)

def hr_itertools_permutations():
    s, n = input().split()
    a = sorted(list(permutations(s, int(n))), key=[itemgetter(0), lambda x: (x[0], x[1])][int(n) != 1])
    print("\n".join("".join(p) for p in a))

def hr_set_duplicate():
    k = int(input())
    a = [int(i) for i in input().split()]
    b, c = set(), set()

    # use math logic
    print((sum(set(a)) * k - sum(a)) // (k - 1))

    # use set difference logic
    for i in a:
        if i in b:
            c.add(i)
        else:
            b.add(i)
    print(b.difference(c).pop())

def hr_sort_descending_list():
    s = input()

    # use minus (-) operator to sort descending
    c = sorted(dict(Counter(s)).items(), key=lambda x: (-x[1], x[0]))[:3]
    print("\n".join(" ".join(str(i) for i in a) for a in c))

def hr_closure_decorator():
    def convert(s):
        c = lambda a, b, c: "%s %s %s" % (a, b, c)
        t = max(len(s[::-1][:10]), len(s)) - min(len(s[::-1][:10]), len(s))

        if t == 0:
            # has 10 digits only
            return c("+91", s[:len(s)//2], s[len(s)//2:])
        if t == 1:
            # has 0 at head
            return c("+91", s[1:1 + (len(s) - 1)//2], s[1 + (len(s) - 1)//2:])
        if t == 2:
            # has 91 at head
            return c("+" + s[:2], s[2:2 + (len(s) - 2)//2], s[2 + (len(s) - 2)//2:])
        # has +91 at head
        return c(s[:3], s[3:8], s[8:])

    def mapping(func, a):
        n = len(a)
        for i in range(n):
            a[i] = func(a[i])
        return a

    def wrapper(f):
        def fun(l):
            s = lambda x: "%s %s %s" % (x[:3], x[3:8], x[8:])
            l = mapping(convert, l)
            f(l)
        return fun

    @wrapper
    def sort_phone(l):
        print(*sorted(l), sep='\n')
    
    return sort_phone

def hr_closure_decorator_person_lister():
    def person_lister(f):
        def inner(people):
            n = len(people)
            people = sorted([people[i] + [i] for i in range(n)], key=lambda x: (len(x[2]), x[2], x[4]))
            return list(map(f, people))
        return inner

    @person_lister
    def name_format(person):
        return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

def hr_zip():
    n, x = map(int, input().split())
    a = [[float(i) for i in input().split()] for _ in range(x)]
    a = list(zip(*a))

    for i in range(n):
        print("%.1f" % (sum(a[i]) / x))

def pass_as_a_tuples(*args):
    print(args)

def pass_as_a_dictionary(**kwargs):
    print(kwargs)

if __name__ == '__main__':
    n = int(input())
    
    pass_as_a_tuples(1, 2, 3, 4, 5)
    pass_as_a_tuples([1, 2, 3])
    pass_as_a_dictionary(a = 1, b = 2)