y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())
a = (x2 - x1)
b = (y2 - y1)
if b > 1 or a > 1:
    print('NO')
elif a < -1 or b < -1:
    print('NO')
else:
    print('YES')
