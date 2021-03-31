from collections import Counter
from itertools import combinations

def is_subsequences(s_1, s_2) -> bool:
    i = j = 0
    while i < len(s_1) and j < len(s_2):
        if s_1[i] == s_2[j]:
            i += 1
        j += 1
    return i == len(s_1)

if __name__ == '__main__':
    q = int(input())

    while q > 0:
        s, t, p = input(), input(), input()

        if not is_subsequences(s, t):
            print("NO")
        else:
            s, t, p = Counter(s), Counter(t), Counter(p)

            for k in t:
                if not t.get(k) <= s.get(k, 0) + p.get(k, 0):
                    print("NO")
                    break
            else:
                print("YES")

        q -= 1