myList = list(map(int, input().split()))
i = 0
for item in myList[:]:
    if item > 0:
        i += 1
print(i)
