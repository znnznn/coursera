inFile = int(input())
i = 0
b = []
while i < inFile:
    a = list(input().split())
    b.append(a)
    i += 1
b = sorted(b, key=lambda x: int(x[1]), reverse=True)
n = len(b)
for x, y in enumerate(b):
    print(y[0], end='\n')
