a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0 and b == 0:
    print('INF')
elif a == 0 and b != 0:
    print('NO')
elif b * c / a == d or -b % a != 0:
    print('NO')
else:
    print(int(-b // a))
