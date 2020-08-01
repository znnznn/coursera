inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
words = inFile.read().splitlines()
dictionary = dict()
result = dict()
result2 = dict()
for word in words:
    dictionary[word] = dictionary.get(word, 0) + 1
res = dictionary.copy()
n = dictionary.items()
y = (sorted(n, key=lambda x: x[1], reverse=True))
i = 0
k = 0
for item in y:
    if int(item[1]) / sum(dictionary.values()) * 100 > 50:
        result[item[0]] = item[1]
        print(item[0], end='', file=outFile)
        k = int(item[1]) / sum(dictionary.values()) * 100
        i += 1
    if item[1] == max(dictionary.values()):
        k += int(item[1]) / sum(dictionary.values()) * 100
        result[item[0]] = item[1]
        del res[item[0]]
    elif item[1] == max(res.values()) and k <= 50:
        result2[item[0]] = item[1]
if i == 0:
    print(*result.keys(), file=outFile)
    print(*result2.keys(), file=outFile)
outFile.close()
inFile.close()
