from sys import stdin


class Matrix:

    def __init__(self, a):
        self.s = a[:]

    def __str__(self):
        res = ""
        k = 0
        for i in self.s:
            res += '\t'.join(map(str, i))
            k += 1
            if k < len(self.s):
                res += '\n'
        return res

    def size(self):
        return len(self.s), len(self.s[0])

    def __add__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.s)):
            for j in range(len(self.s[0])):
                summa = other[i][j] + self.s[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.s):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


m = Matrix([[1, 0], [0, 1]])
print(m)
m = Matrix([[2, 0, 0], [0, 1, 10000]])
print(m)
m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])
print(m)

exec(stdin.read())