n = int(input())
m = int(input())
print('YES' * (0 ** (n % m)), 'NO' * (1 - 0 ** (n % m)), sep='')
