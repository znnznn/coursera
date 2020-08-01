a = int(input())
b = int(input())
if a <= b:
    for item in range(a, b + 1):
        print(item, end=' ')
else:
    for item in range(a, b - 1, -1):
        print(item, end=' ')
