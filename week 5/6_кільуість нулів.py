a = int(input())
i = 0
null = [a]
while a != 0:
    null.append(int(input()))
    a -= 1
for item in null:
    if item == 0:
        i += 1
print(i)
