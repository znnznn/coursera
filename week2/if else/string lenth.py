a = int(input())
a1 = int(input())
b = int(input())
b1 = int(input())
c = int(input())
c1 = int(input())
one = a1 - a
two = b1 - b
tree = c1 - c
if c <= b1 and b <= a1 and not a > c or c < a1 and b1 < c1 and not a > b1:
    print('0')
elif b > a1 and a1 < c <= b1 and b - a1 <= one:
    print('1')
elif a < c <= a1 and b > c1 and b - c1 <= two:
    print('2')
elif b < a1 > b1 < c and c - b1 <= tree and b != 0:
    print('3')
elif b1 < a and 0 < a - b1 < tree and not a > c:
    print('3')
elif 0 < b - a1 > one and c - b1 <= tree > two:
    print('3')
elif b <= a1 and c > b1 and c - b1 <= tree and not c - a1 <= two and not a > c:
    print('3')
elif b > a1 and c > b1 and c - b1 <= one:
    print('1')
elif a1 < c1 < b and b - c1 <= one:
    print('1')
elif b < c < b1:
    print('1')
elif c1 < b > a1 and c - a1 <= two and not c < a and not b - a1 <= one:
    print('2')
elif 0 < c - a1 <= two and c > a and b1 > c1:
    print('2')
elif 0 < c - a1 <= two and c > a:
    print('2')
elif a < c < a1:
    print('2')
elif a > c1 and b > c1 and a - c1 <= two:
    print('2')
elif 0 < c - a1 <= two and c > b1 < a:
    print('2')
elif b1 <= c < a < c1 and c - b1 <= one:
    print('1')
elif (b - a1) > one and b - a1 > two and b - a1 > tree:
    print('-1')
elif b - a1 < 0 and not tree >= c - a1 or c - b1 < 0:
    print('-1')
elif 0 < (c - b1) > one and c - b1 > two and c - b1 > tree and c - a1 > two:
    print('-1')
else:
    print('1')
