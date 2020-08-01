n = int(input())
myList = list(map(int, input().split()))
x = int(input())
i = 2001
new_list = []
myIndex = 0
for item in myList:
    new_list.append(abs(item - x))
    for index, result in enumerate(new_list):
        if result < i:
            i = result
            myIndex = index
print(myList[myIndex])
