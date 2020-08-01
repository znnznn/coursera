from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, a):
        self.s = deepcopy(a)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.s)

    def size(self):
        sizepair = (len(self.s), len(self.s[0]))
        return sizepair

    def __getitem__(self, idx):
        return self.s[idx]

    def __add__(self, other):
        if len(self.s) == len(other.s):
            lenght_m = len(self.s[0])
            for row in self.s:
                if len(row) != lenght_m:
                    raise MatrixError(self, other)
            for row2 in other:
                if len(row2) != lenght_m:
                    raise MatrixError(self, other)
            result = []
            numbers = []
            for i in range(len(self.s)):
                for j in range(len(self.s[0])):
                    summa = other[i][j] + self.s[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.s[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = [[other * j for j in i] for i in self.s]
            return Matrix(result)

    __rmul__ = __mul__

    def transpose(self):
        transMatrix = list(map(list, zip(*self.s)))
        self.s = transMatrix
        return Matrix(transMatrix)

    def transposed(self):
        transMatrix = list(map(list, zip(*self.s)))
        return Matrix(transMatrix)


exec(stdin.read())
