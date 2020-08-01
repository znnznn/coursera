from math import sqrt
x = int(input())


def MinDivisor(n):
    i = 2
    while x % i != 0:
        i += 1
        if i > sqrt(x):
            return x
    return i
print(MinDivisor(x))
