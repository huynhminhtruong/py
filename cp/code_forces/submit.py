if __name__ == '__main__':
    x_1, y_1, x_2, y_2 = map(int, input().split())
    l, d = abs(x_1 - x_2), abs(y_1 - y_2)

    if x_1 == x_2:
        print(x_1 + d, y_1, x_2 + d, y_2)
    elif y_1 == y_2:
        print(x_1, y_1 + l, x_2, y_2 + l)
    elif l == d:
        print(x_1, y_2, x_2, y_1)
    else:
        print(-1)