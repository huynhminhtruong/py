if __name__ == '__main__':
    h, a = input(), input()
    s = lambda x, n, m: "%s %s %s" % (x, n, m)
    t = int(input())
    b, c = dict(), dict()

    def is_red(d, key, name, m, func):
        if d[key] in (2, 3):
            print(func(name, key, m))

    while t > 0:
        d = input().split()
        cnt = 1 if d[3] == "y" else 2
        if d[1] == "h":
            if b.get(d[2], 0) < 2 and 1 < b.get(d[2], 0) + cnt < 4:
                print(s(h, d[2], d[0]))
            b[d[2]] = b.get(d[2], 0) + cnt
        else:
            if c.get(d[2], 0) < 2 and 1 < c.get(d[2], 0) + cnt < 4:
                print(s(a, d[2], d[0]))
            c[d[2]] = c.get(d[2], 0) + cnt
        t -= 1