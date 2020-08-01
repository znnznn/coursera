myList = list(map(int, input().split()))
i = 0
f = 0
for y, item in enumerate(myList):
    if item >= i:
        i = item
        f = y
print(i, f)
