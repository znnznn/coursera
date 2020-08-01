a = set(map(int, input().split()))
b = set()
i = 0
for elem in a:
    if elem not in b:
        b.add(elem)
        i += 1
print(i)
