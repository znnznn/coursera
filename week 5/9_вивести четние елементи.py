myList = list(map(int, input().split()))
a = 0
print(type(myList))
for item in myList[:]:
    if item % 2 == 0:
        a = item
        print(a)
