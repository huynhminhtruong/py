import functools as ft

def d(n):
    f = False
    for i in n[-1::-1]:
        if i == '0' and f:
            return True
        if i != '0' and not f:
            f = not f
    return False

if __name__ == '__main__':
    s = input()
    print(d(s))