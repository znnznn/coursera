a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(a)
elif a < b and b >= c:
    print(b)
elif a == b and b == c:
    print(a)
elif a <= b and c <= b:
    print(b)
else:
    print(c)
