import math
from operator import itemgetter

def is_prime(n: int)->bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if not (n % i):
            return False
    return True

def col_array_input():
    n = int(input())
    a = list()
    for i in range(n):
        t = int(input())
        if is_prime(t):
            a.append(t)
    print(*a)

def col_array_count():
    n = int(input())
    d = dict()
    for i in range(n):
        t = int(input())
        d[t] = d.get(t, 0) + 1
    d = sorted(d.items(), key=itemgetter(0))
    print("".join("{0} - {1};".format(x[0], x[1]) for x in d))

def sum_int_digits(n: int):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def sum_string_digits(n: str):
    return sum(list(map(int, n)))

def hr_sort_string_numbers_by_sum_of_digits():
    # O(N * log(number))
    # Case int numbers
    n = int(input())
    t = input().split()
    a = sorted([int(i) for i in t], key=lambda x: sum_int_digits(x))
    print(*a)
    # Case big string number
    # Need convert for every digit from string to int
    n = int(input())
    b = sorted([i for i in t], key=lambda x: sum_string_digits(x))
    print(*b)

def hr_sort_string_numbers_lexicographically():
    # O(based on algorithm of build-in sorted)
    n = int(input())
    a = input().split()
    mx = "9"

    # Find min string number by lexicographically
    for i in a:
        mx = min(mx, i)
    print(mx)

    # Sort string by lexicographically
    a.sort()
    print(*a)

if __name__ == "__main__":
    pass