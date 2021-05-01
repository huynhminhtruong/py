def f(n: int):
    if not n:
        return 1
    n *= f(n - 1)
    return n

def pow(a: int, b: int):
    if not b:
        return 1
    return a * pow(a, b - 1)

def lcn(a: int, b: int):
    if not b:
        return a
    return lcn(b, a % b)

def fib(a: int):
    if a == 0 or a == 1:
        return 1
    return fib(a - 1) + fib(a - 2)

def guess_number(n: int):
    if n == 1: return 1
    return 1 + guess_number(n - round(n / 2))

class Numbers:

    a = list()

    def __init__(self):
        self.length = 0
    
    def __str__(self):
        return " ".join(str(self.a[i]) for i in range(self.length))

    def add(self, value: int):
        self.a.append(value)
        self.length += 1

    def bubble_sort_leftmost(self, reverse = False):

        # Compare a pair of 2 sequence numbers
        # Move smallest number to leftmost or move lagest to rightmost

        # Using reverse to determine sort by ascending or descending

        for i in range(self.length):
            for j in range(self.length - 1, i - 1, -1):
                if not (self.a[j] < self.a[j - 1]) == reverse:
                    t = self.a[j]
                    self.a[j] = self.a[j - 1]
                    self.a[j - 1] = t

    def bubble_sort_rightmost(self, reverse = False):

        # Move lagest number to rightmost

        for i in range(self.length - 1, -1, -1):
            for j in range (i):
                if not (self.a[j] > self.a[j + 1]) == reverse:
                    self.a[j] += self.a[j + 1]
                    self.a[j + 1] = self.a[j] - self.a[j + 1]
                    self.a[j] -= self.a[j + 1]

    def insertion_sort(self, reverse = False):
        for i in range(1, self.length):
            index = i
            value = self.a[i]
            while index > 0 and not (self.a[index - 1] > value) == reverse:
                self.a[index] = self.a[index - 1]
                index -= 1
            self.a[index] = value

    def selection_sort(self, reverse = False):
        for i in range(self.length):
            k = i
            for j in range(i + 1, self.length):
                if not (self.a[k] > self.a[j]) == reverse:
                    k = j
            if k > i:
                t = self.a[k]
                self.a[k] = self.a[i]
                self.a[i] = t
    
    def shell_sort(self, reverse = False):
        # Knuth formula
        gap = self.length // 2

        # Based on Insertion Sort
        while gap > 0:
            for i in range(gap, self.length):
                index = i
                value = self.a[i]
                while index > 0 and not (self.a[index - gap] > value) == reverse:
                    self.a[index] = self.a[index - gap]
                    index -= gap
                self.a[index] = value
            gap //= 2

if __name__ == "__main__":
    n = int(input())
    a = Numbers()

    for i in range(n):
        a.add(int(input()))

    print(a)
    a.shell_sort(reverse=True)
    print(a)