myList = list(map(int, input().split()))
f = 0
i = 1
for item in myList:
    if item < i and f != 0:
        i = item
        print(i)
    else:
        i = item
    f += item
