myList = list(map(int, input().split()))
f = 0
i = 1001
for item in myList:
    if item <= 0:
        continue
    elif item < i:
        i = item
print(i)
