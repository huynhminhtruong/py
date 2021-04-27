import copy as cp

if __name__ == '__main__':
    a = [1, 2, (1, 2), "something", [1, 2, 3]]
    b = cp.deepcopy(a)

    # a[0] = 2
    # b[0] = 3
    # a[3] = a[3][:-2]
    # a[4][1] += 2
    # a[2] = (2, 3)
    # # a[4] = [3, 4, 5]
    # a[4][0] += 12

    print(id(a[4]))
    print(id(b[4]))

    print(a)
    print(b)