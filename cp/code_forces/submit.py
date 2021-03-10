if __name__ == '__main__':
    cin = input
    t = int(cin())

    while t > 0:
        n = int(input())
        a = list(map(int, input().split()))
        mx, i, j, l, cnt = 0, -1, n, 1, 0
        bob, alice = 0, 0

        while i < j:
            s = 0
            if l:
                i += 1
                while i < j:
                    s += a[i]
                    if s > mx:
                        break
                    i += 1
                alice += s
            else:
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
