def min5(a, b, c, d):
    min1 = min(a, b)
    min2 = min(c, d)
    min5 = min(min1, min2)
    return min5
a = input()
b = input()
c = input()
d = input()
print(min5(a, b, c, d))
