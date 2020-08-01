class Number:
    def __init__(self, a):
        self.a = a

    def division(self, b):
        print('Simple number division')
        if b != 0:
            return self.a / b
        raise ZeroDivisionError('Cannot divide by zero')

class Integer(Number):
    def division(self, b):
        print('Integer division')
        result = super().division(b)
        return int(result)

number_two = Number(1)
print(number_two.division(2))

integer_ten = Integer(10)


print(issubclass(Integer, Number))
print(issubclass(Number, Integer))