a = float(input())
i = 1
k = 0
while i <= a:
    k = 1 / (i ** 2) + k
    i += 1
else:
    print(k)
