myList = list(map(int, input().split()))
k = int(input())
v = myList.pop(k)
print(*myList, v)
