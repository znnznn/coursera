n = int(input().strip())
a = {}
for i in range(n+1):
    words = input().split()
    if len(words) > 1:
        a[words[0]] = words[1]
    else:
        for key, y in a.items():
            if key == words[0]:
                print(y)
            elif y == words[0]:
                print(key)
