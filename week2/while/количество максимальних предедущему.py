n = int(input())
i = n
b = 0
while n != 0:
    if n > i and n != 0:
        i = n
        b += 1
    elif i > n:
        i = n
    n = int(input())
print(b)
