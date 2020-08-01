y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())
a = (x2 - x1)
b = (y2 - y1)
c = ((b + a) % 2)
if c > 0 or c < 0:
    print('NO')
else:
    print('YES')
