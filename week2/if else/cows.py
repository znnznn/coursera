n = int(input())
f1 = 'korova'
fy = 'korov'
fs = 'korovy'
yy = (n % 10)
if 10 <= n < 20 or yy == 0 or yy >= 5:
    print(n, fy)
elif n == 1 or yy == 1:
    print(n, f1)
else:
    print(n, fs)
