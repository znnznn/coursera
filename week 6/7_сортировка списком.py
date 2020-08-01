def CountSort(a):
    n = max(a) + 1
    cntMarks = [0] * n
    for i in a:
        cntMarks[i] += 1
    a[:] = []
    for newMark in range(n):
        a += [newMark] * cntMarks[newMark]
    return a


a = list(map(int, input().split()))
b = CountSort(a)
print(*b)
