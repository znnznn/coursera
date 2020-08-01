n = int(input())
m = int(input())
x = int(input())
n1 = ((n // m) * (n // x))
m1 = ((m // n) * (m // x))
x1 = ((x // m) * (x // n))
st1 = 'rectangular'
st2 = 'acute'
st3 = 'obtuse'
st4 = 'impossible'
c = (n * n1 + m * m1 + x * x1) // (n1 + m1 + x1)
p = (n + m + x)
if c ** 2 == (n ** 2 + m ** 2 + x ** 2) - c ** 2 and c < p - c:
    print(st1)
elif c ** 2 > (n ** 2 + m ** 2 + x ** 2) - c ** 2 and c < p - c:
    print(st3)
elif c ** 2 < (n ** 2 + m ** 2 + x ** 2) - c ** 2 and c < p - c:
    print(st2)
else:
    print(st4)
print(c)

#elif 0 < (c - b1) > one and c - b1 > two and c - b1 > tree and c - a1 > two:
    #print('-1')