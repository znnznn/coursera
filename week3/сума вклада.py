p = float(input())
x = float(input())
y = float(input())
m = x * 100 + y
m1 = (m * (100 + p)) / 100
pm = m1 // 100
pk = m1 - (pm * 100)
n = 'abracadabra'.count('a')
print(int(pm), int(pk))
print(n)
message = 'Hello beautiful world!'
final_message = message[0:5] + ' ' + message[-6:] + ' Today is a ' + message[6:15] + ' day.'
print(final_message)