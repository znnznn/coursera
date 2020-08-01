a, b, c = int(input()), int(input()), int(input())
a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
v1 = a * b * c
v2 = a1 * b1 * c1
v3 = a2 * b2 * c2
v4 = v1 * v2 * v3
f1 = a + a1
f2 = b + b1
f3 = c + c1
f4 = a + b1
f5 = b + a1
if c <= c2 >= c1 and a + a1 <= a2 and b <= b2 >= b1 and v4 != 0:
    print('YES')
elif c <= c2 >= c1 and b + b1 <= b2 and a <= a2 >= a1 and v4 != 0:
    print('YES')
elif b <= b2 >= b1 and c + c1 <= c2 and a <= a2 >= a1 and v4 != 0:
    print('YES')
elif c <= c2 >= c1 and a + b1 <= b2 and b <= a2 >= a1 and v4 != 0:
    print('YES')
elif c <= c2 >= c1 and b + a1 <= b2 and a <= a2 >= b and v4 != 0:
    print('YES')
elif c <= c2 >= c1 and a + b1 <= a2 and b <= b2 >= a1 and v4 != 0:
    print('YES')
elif c <= c2 >= c1 and b + a1 <= a2 and a <= b2 >= b1 and v4 != 0:
    print('YES')
elif c <= c2 >= c1 and a + a1 <= b2 and b <= a2 >= b1 and v4 != 0:
    print('YES')
elif c <= c2 >= c1 and b + b1 <= a2 and a <= b2 >= a1 and v4 != 0:
    print('YES')
elif a <= b2 >= a1 and c + c1 <= c2 and b <= a2 >= b1 and v4 != 0:
    print('YES')
elif b <= b2 >= a1 and c + c1 <= c2 and a <= a2 >= b1 and v4 != 0:
    print('YES')
elif a <= b2 >= b1 and c + c1 <= c2 and b <= a2 >= a1 and v4 != 0:
    print('YES')
else:
    print('NO')
