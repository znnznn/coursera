inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'a', encoding='utf8')
b = []
for item in sorted(inFile):
    a = item
    b.append(a)
    b = a.split()
    del b[-2]
    f = ' '.join(b)
    outFile.write(f)
    outFile.write('\n')
inFile.close()
outFile.close()
c = [0] * 3
print(c)