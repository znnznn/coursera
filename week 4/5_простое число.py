from math import sqrt
x = int(input())


def MinDivisor(x):
    i = 2
    while (x % i != 0 or x == 2) and not x == 1:
        i += 1
        if i > sqrt(x):
            return print('Yes')
    return print('NO')
MinDivisor(x)
