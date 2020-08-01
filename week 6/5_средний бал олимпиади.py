inFile = open('input.txt', 'r', encoding='utf8')
nine = []
ten = []
eleven = []
for item in inFile:
    a = item
    b = a.split()
    if b[-2] == '9':
        nine.append(int(b[-1]))
    elif b[-2] == '10':
        ten.append(int(b[-1]))
    elif b[-2] == '11':
        eleven.append(int(b[-1]))
nine_result = sum(nine) / len(nine)
ten_result = sum(ten) / len(ten)
eleven_result = sum(eleven) / len(eleven)
print(nine_result, ten_result, eleven_result, sep=' ')
