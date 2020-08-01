a = int(input())
b = 10 ** a - 1
a = 10 ** (a - 1)
for item in range(b, a - 1, -2):
    print(item, end=' ')
