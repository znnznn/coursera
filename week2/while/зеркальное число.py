a = int(input())
n = 0
while a > 0:
    z = a % 10
    a //= 10
    n *= 10
    n += z
print(n)
