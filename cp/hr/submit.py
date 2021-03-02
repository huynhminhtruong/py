from itertools import groupby
from collections import OrderedDict as od

if __name__ == '__main__':
    n = int(input())
    d = od()

    for i in range(n):
        word = input()
        d[word] = d.get(word, 0) + 1
    print("%d\n%s" % (len(d.items()), " ".join(str(i) for i in d.values())))