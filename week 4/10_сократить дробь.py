n = int(input())
m = int(input())


def ReduceFraction(n, m):
    p = n
    q = m

    def gcd(n, m):
        while n != 0 and m != 0:
            if n > m:
                n = n % m
            else:
                m = m % n
        return m + n
    return p // gcd(n, m), q // gcd(n, m)


d, d1 = ReduceFraction(n, m)
print(d, d1)
