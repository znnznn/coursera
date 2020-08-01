x = input()
x1 = x.find('f')
x2 = f'{x[x1 + 1:]}'
x3 = x2.find('f')
if x1 == -1:
    print(-2)
elif x3 >= 0 <= x1:
    print(x3 + x1 + 1)
else:
    print(-1)
