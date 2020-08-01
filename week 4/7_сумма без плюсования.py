a = int(input())
n = int(input())


def power(a, n):
    if n != 0:
        a += 1
        n -= 1
        return power(a, n)
    else:
        return a


print(power(a, n))
