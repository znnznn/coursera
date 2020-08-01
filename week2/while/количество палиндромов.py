k = int(input())
i = 1
ii = 0
while i <= k:
    a = i
    n = 0
    while a > 0:
        z = a % 10
        a //= 10
        n *= 10
        n += z
    if n == i:
        ii += 1
    i += 1
print(ii)
