a = list(map(int, input().split()))
b = set()
for elem in a:
    if elem in b:
        print('YES')
    else:
        b.add(elem)
        print('NO')
