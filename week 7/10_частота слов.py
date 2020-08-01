words = (open('input.txt').read().split())
dictionary = {}
result = []
for word in words:
    dictionary[word] = dictionary.get(word, 0) + 1
n = sorted(dictionary.items())
y = (sorted(n, key=lambda x: x[1], reverse=True))
for i in y:
    print(i[0])
