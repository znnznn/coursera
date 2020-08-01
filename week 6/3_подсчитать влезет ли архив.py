users = list(map(int, input().split()))
memory = users[0]
count = users[1]
box = []
for item in range(count):
    b = list(map(int, input().split()))
    box.append(*b)
box.sort()
k = sum(box)
i = len(box)
while i != 0:
    if k > memory != 0:
        k -= box[i-1]
        i -= 1
    elif memory == 0:
        i = 0
    else:
        break
print(i)
