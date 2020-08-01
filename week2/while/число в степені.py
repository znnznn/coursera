n = int(input())
i = 0
k = 0
while i <= n and k < n:
    k = 2 ** i
    if k >= n >= i:
        print(i)
    elif k < n:
        i = i + 1
    else:
        print(0)
