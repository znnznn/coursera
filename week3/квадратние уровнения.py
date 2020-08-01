a = float(input())
b = float(input())
c = float(input())
d = (b ** 2) - (4 * a * c)
if d < 0:
    print()
if d == 0:
    r = (-b + (d ** 0.5)) / (2 * a)
    print(r)
elif d > 0:
    r = (-b + (d ** 0.5)) / (2 * a)
    r1 = (-b - (d ** 0.5)) / (2 * a)
    if r1 > r:
        print(r, r1)
    else:
        print(r1, r)
