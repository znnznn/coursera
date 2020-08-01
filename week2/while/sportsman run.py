n = int(input())
g = int(input())
i = 1
if n == g or g < n:
    print(1)
while n < g:
    n = n * 1.1
    i = i + 1
    if n >= g:
        print(i)
