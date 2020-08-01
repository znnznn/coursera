n = int(input())
a = map(int, input().split())
m = int(input())
b = list(map(int, input().split()))

for i in range(len(b)):
    b[i] = [i + 1, b[i]]
b.sort(key=lambda x: x[1])


def find_value(v):
    if v < b[0][1]:
        return b[0][0]
    if v > b[-1][1]:
        return b[-1][0]
    l = 0
    r = len(b) - 1
    while r - l > 1:
        m = (r + l) >> 1
        if b[m][1] < v:
            l = m
        else:
            r = m
    if v - b[l][1] < b[r][1] - v:
        return b[l][0]
    else:
        return b[r][0]


print(*[find_value(v) for v in a])
