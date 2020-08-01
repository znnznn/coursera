a = list(map(int, input().split()))
b = list(map(int, input().split()))


def merge(a, b):
    i = 0
    j = 0
    myList = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            myList.append(a[i])
            i += 1
        else:
            myList.append(b[j])
            j += 1
    myList += a[i:] + b[j:]
    return myList


print(*merge(a, b))
