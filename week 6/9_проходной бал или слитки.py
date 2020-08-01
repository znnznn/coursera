inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'a', encoding='utf8')
s = int(inFile.readline().strip())
a = []
d = []
for i in inFile:
    a.append(i.split()[-3:])
for y, digit in reversed(list(enumerate(a))):
    for x, z in reversed(list(enumerate(digit))):
        a[y][x] = int(z)
        if a[y][x] < 40:
            del a[y]
            break
for t in a:
    g = sum(t)
    d.append(g)
d.sort(reverse=True)
n = len(d)
e = 1


def func(n, s, d):
    if n <= s or s == 0:
        return 0
    elif d.count(max(d)) > s:
        return 1
    for i in range(s, 0, -1):
        if d[i] < d[i - 1]:
            return d[i - 1]


w = str(func(n, s, d))
outFile.write(w)
