n = int(input())
b = 1
b1 = 1
while n != 0:
    n1 = int(input())
    if n1 == n:
        b += 1
        if b > b1:
            b1 = b
    else:
        b = 1
    n = n1
print(b1)
