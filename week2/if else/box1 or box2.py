a, b, c = int(input()), int(input()), int(input())
a1, b1, c1 = int(input()), int(input()), int(input())
if a >= b and a >= c:
    if b >= c:
        (a, b, c) = (c, b, a)
    else:
        (a, b, c) = (b, c, a)
elif b >= a and b >= c:
    if a >= c:
        (a, b, c) = (c, a, b)
    else:
        (a, b, c) = (a, c, b)
elif c >= a and c >= b:
    if a >= b:
        (a, b, c) = (b, a, c)
    else:
        (a, b, c) = (a, b, c)
if a1 >= b1 and a1 >= c1:
    if b1 >= c1:
        (a1, b1, c1) = (c1, b1, a1)
    else:
        (a1, b1, c1) = (b1, c1, a1)
elif b1 >= a1 and b1 >= c1:
    if a1 >= c1:
        (a1, b1, c1) = (c1, a1, b1)
    else:
        (a1, b1, c1) = (a1, c1, b1)
elif c1 >= a1 and c1 >= b1:
    if a1 >= b1:
        (a1, b1, c1) = (b1, a1, c1)
    else:
        (a1, b1, c1) = (a1, b1, c1)
if a == a1 and b == b1 and c == c1:
    print('Boxes are equal')
elif a <= a1 and b <= b1 and c <= c1:
    print('The first box is smaller than the second one')
elif a >= a1 and b >= b1 and c >= c1:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
