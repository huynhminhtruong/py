if __name__ == '__main__':
    s = list()
    for _ in range(4):
        s.append(len(input()) - 2)
    l = sorted(s)
    mn, mx = l[0], l[3]
    mn = l[0] if l[0] <= l[1] / 2 else 0
    mx = l[3] if l[3] >= l[2] * 2 else 0
    if not mn and mx:
        print(chr(s.index(mx) + ord("A")))
    elif mn and not mx:
        print(chr(s.index(mn) + ord("A")))
    else:
        print("C")