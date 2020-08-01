myList = list(map(int, input().split()))
list_max = myList.index(max(myList))
list_min = myList.index(min(myList))
myList[list_max], myList[list_min] = myList[list_min], myList[list_max]
print(*myList)
