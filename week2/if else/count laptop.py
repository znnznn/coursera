a1 = int ( input () )
b1 = int ( input () )
c1 = int ( input () )
x  = int ( input () )
y = int ( input () )
z = int ( input () )

d1 = (a1 // x) * (b1 // y) * (c1 // z)
d2 = (a1 // x) * (c1 // y) * (b1 // z)
d3 = (b1 // x) * (c1 // y) * (a1 // z)
d4 = (b1 // x) * (a1 // y) * (c1 // z)
d5 = (c1 // x) * (a1 // y) * (b1 // z)
d6 = (c1 // x) * (b1 // y) * (a1 // z)


n = (c // a1) * (b // b1) * (a // c1)
m = (c // c1) * (b // a1) * (a // b1)
x = (c // b1) * (b // c1) * (a // a1)
z = (c // a1) * (b // c1) * (a // b1)
s = (c // c1) * (b // b1) * (a // a1)
f = (c // b1) * (b // a1) * (a // c1)
if d1 >= d2 :
    d2 = d1
if d3 >= d4 :
    d4 = d2
if d5 >= d6 :
    d6 = d5

if d2 >= d4 and d2 >= d6 :
    print ( d2 )
elif d4 >= d6 :
    print ( d4 )
else :
    print ( d6 )
print(d1, d2, d3, d4, d5, d6)
if n >= m:
    m = n
elif x >= z:
    z = x
elif s >= f:
    f = s
if m > z and m > f:
    print(m)
elif z > f:
    print(z)
else:
    print(f)