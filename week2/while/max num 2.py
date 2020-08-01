n = int(input())
x = 0
while n != 0:
    z = int(input())
    if n <= z and n != 0:
        x = n
        n = z
    elif x < z < n:
        x = z
    elif z == 0:
        n = z
print(x)
