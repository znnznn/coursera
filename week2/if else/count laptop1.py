a, b, c = int(input()), int(input()), int(input())
a1, b1, c1 = int(input()), int(input()), int(input())
n = (c // a1) * (b // b1) * (a // c1)
m = (c // c1) * (b // a1) * (a // b1)
x = (c // b1) * (b // c1) * (a // a1)
z = (c // a1) * (b // c1) * (a // b1)
s = (c // c1) * (b // b1) * (a // a1)
f = (c // b1) * (b // a1) * (a // c1)
if n >= m:
    m = n
if x >= z:
    z = x
if s >= f:
    f = s
if m >= z and m >= f:
    print(m)
elif z >= m and z >= f:
    print(z)
else:
    print(f)
