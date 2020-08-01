a = float(input())
n = float(input())


def power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return power(a, n / 2) ** 2
    return power(a, n - 1) * a


print(power(a, n))
