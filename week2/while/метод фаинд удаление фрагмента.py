x = input()
x2 = x.rfind('h')
x1 = x.find('h')
if 0 <= x1 < x2:
    print(f'{x[:x1]}{x[x2+1:]}')
elif x1 == x2 != -1 or x1 >= 0 < x2:
    print(f'{x[:x1]} ')
elif x2 > x1 == -1:
    print(f'{x[x2+1:]}')
else:
    print()
