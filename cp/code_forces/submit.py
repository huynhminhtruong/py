if __name__ == '__main__':
    q = int(input())
    d, i, j, f = dict(), 0, 0, True

    while q > 0:
        p, k = input().split()
        if f:
            d[k] = d.get(k, 0)
            f = not f
        else:
            if p == "L":
                i -= 1
                d[k] = d.get(k, i)
            elif p == "R":
                j += 1
                d[k] = d.get(k, j)
            else:
                print(min(abs(i - d.get(k)), abs(j - d.get(k))))
        q -= 1