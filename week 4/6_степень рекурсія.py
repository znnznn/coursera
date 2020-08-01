a = float(input())
n = float(input())


def power(a, n):
    z = a * (a ** (n - 1))
    return z


print(power(a, n))
