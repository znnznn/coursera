n = int(input())
i = n
b = 0
while n != 0:
    if n > i and n != 0:
        i = n
        b = 1
    elif n == i:
        b += 1
    n = int(input())
print(b)
