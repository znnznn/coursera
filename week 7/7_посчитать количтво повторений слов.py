words = open('input.txt').read().split()
dictionary = {}
for word in words:
    if word not in dictionary:
        dictionary[word] = 0
    else:
        dictionary[word] += 1
    print(dictionary[word], end=" ")
