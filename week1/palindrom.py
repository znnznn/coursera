n = int(input())
n1 = (n // 1000)
n2 = (n // 100 % 10)
n3 = (n // 10 % 10)
n4 = (n % 10)
m = (n4 * 1000 + n3 * 100 + n2 * 10 + n1)
print(m - n + 1)