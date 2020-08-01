words = (open('input.txt').read().split())
dictionary = {}
result = []
for word in words:
    dictionary[word] = dictionary.get(word, 0) + 1
n = max(dictionary.values())
for key, item in dictionary.items():
    if item == n:
        result.append(key)
print(min(result))
