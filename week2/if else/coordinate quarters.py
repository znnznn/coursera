x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 >= 0 and x2 >= 0 and y1 >= 0 and y2 >= 0:
    print('YES')
elif x1 > 0 > y1 and x2 > 0 > y2:
    print('YES')
elif x1 < 0 and x2 < 0 and y1 < 0 and y2 < 0:
    print('YES')
elif x1 < 0 < y1 and x2 < 0 < y2:
    print('YES')
else:
    print('NO')
