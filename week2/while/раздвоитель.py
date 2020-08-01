a = int(input())
b = int(input())
while a != b:
    if a >= b * 2 and a % 2 == 0:
        a /= 2
        print(":2")
    else:
        a -= 1
        print(-1)
