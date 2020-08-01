n = int(input())
m = int(input())
k = int(input())
h = (k % n)
j = (k % m)
q = (n * m)
if k < q:
    if h == 0:
        print('YES')
    elif j == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
