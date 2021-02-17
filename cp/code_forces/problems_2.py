import math
import os
import random
import re
import sys
import functools
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