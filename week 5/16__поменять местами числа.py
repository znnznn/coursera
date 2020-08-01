myList = list(map(int, input().split()))
newMy_list = []
for y, x in enumerate(myList):
    if y % 2 != 0:
        newMy_list.insert(y-1, x)
        print(newMy_list)
    else:
        newMy_list.insert(y+1, x)
        print(*newMy_list)
print(*newMy_list)
