import math
p = float(input())
x = float(input())
y = float(input())
k = int(input())
i = 0
m = x * 100 + y
while k > i:
    m1 = ((m * (100 + p)) / 100)
    m = int(m1)
    x = int(m1 // 100)
    y = int(m1 - (x * 100))
    i += 1
print(int(x), int(y))
