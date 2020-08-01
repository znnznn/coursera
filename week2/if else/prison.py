# зек замку іф видовбав дірку d на e перевірити чи проходить цегла розміром a,b,c
a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
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
if d > e:
    (d, e) = (e, d)
else:
    (d, e) = (d, e)
if a <= d and b <= e:
    print('YES')
else:
    print('NO')
