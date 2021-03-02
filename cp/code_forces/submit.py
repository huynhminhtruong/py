if __name__ == '__main__':
    cin = input
    t = int(cin())

    while t > 0:
        n = int(cin())
        a = [int(i) for i in cin().split()]
        i, j, l, s, mx = 1, n - 1, 0, 0, a[0]
        while i < j:
            s = a[i] if l else a[j]
            while i < j and s <= mx:
                i += l
                j -= not l
                s += a[i] if l else a[j]
            mx = s
            i += l
            j -= not l
            l = not l
        print("ans: %d %d" % (sum(a[:j]), sum(a[j:])))
        t -= 1

# [1] [3]     [5]     [6]   [4] [2]
# [3] [1 4 1] [5 9] [2 6] [5 3] [5]

# input
# 7
# 11
# 3 1 4 1 5 9 2 6 5 3 5
# 1
# 1000
# 3
# 1 1 1
# 13
# 1 2 3 4 5 6 7 8 9 10 11 12 13
# 2
# 2 1
# 6
# 1 1 1 1 1 1
# 7
# 1 1 1 1 1 1 1

# output
# 6 23 21
# 1 1000 0
# 2 1 2
# 6 45 46
# 2 2 1
# 3 4 2
# 4 4 3
