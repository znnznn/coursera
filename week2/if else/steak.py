k = int(input())
m = int(input())
n = int(input())
n1 = n * 2
n3 = ((n1 + k - 1) // k)
if n1 <= k:
    print(2 * m)
else:
    print(n3 * m)
