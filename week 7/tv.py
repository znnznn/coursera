class ControllerTV:

    def __init__(self, name='no name', number=0):
        self.name = name
        self.number = number

    def __str__(self):
        return f'{self.number} - {self.name}'

    def __next__(self, d):
        d += 1
        return f'{self.number} - {self.name}'

    def first_channel(self, k, *list_channel):

        for i, x in list_channel:
            if i == k:
                return i
            return i

    def find_f(self, channels_obj):
        for i, obj in channels_obj.__getitem__():
            print(i, obj)
            if obj.name == self:
                return i, obj

    def __contains__(self, item):
        pass


# функція перевірки операції на валідність
def choice_valid(operation):
    oper_user = None
    for t in operation:
        if t in operation_valid:
            oper_user = t
            break
    return oper_user

channels = ["BBC", "Discovery", "TV1000", "MTV", "Sci-Fi", "GALAXY TV", "CNN"]
channels_obj = []
for number, name in enumerate(channels, 1):
    channels_obj.append(ControllerTV(name, number))
print(*channels_obj, sep='\n')

d = channels_obj[6]
print(d)
#print(channels_obj.__next__(d))
print(dir(channels_obj))
#print(channels_obj.__getitem__(6))
a = ([i for i in enumerate(channels, 1)])
print(channels_obj.__class__.__len__(channels_obj))

#print(channels_obj.__class__.__next__(d))
#list_oper1 = {'10-+?'}
operation_valid = {
    '1': 'Ввімкнеться перший канал у списку',
    '-': 'Ввімкнеться попередній канал у списку',
    '+': 'Ввімкнеться наступний канал у списку',
    '?': 'Ввімкнеться канал у списку який ви оберете.',
    '0': 'Ввімкнеться останній канал у списку'
}
operationToprint = [' : '.join(pretty) for pretty in operation_valid.items()]
print(*operationToprint, sep='\n')
k = '6'
print(' o o o o', ControllerTV.first_channel((ControllerTV, k, *channels_obj)))
#print(channels_obj.__class__.__getitem__(ControllerTV))
try:
    while True:
        print('Оберіть операцію для управління каналами: ')
        tv_oper = (input('> ')).strip()
        tv_oper = {''.join(tv_oper)}
        tv_oper = (choice_valid(tv_oper))
        index_tv = 1
        tv = channels_obj[index_tv]
        if tv_oper == '1':
            index_tv = 0
            print(channels_obj[index_tv])
        elif tv_oper == '0':
            index_tv = -1
            print(channels_obj[index_tv])
        elif tv_oper == '-':
            if index_tv == 0:
                index_tv = -1
                print(channels_obj[index_tv])
            else:
                index_tv -= 1
                print ( channels_obj[index_tv] )
            print('Натисніть номер каналу для перегляду: ')
            tv = (input('> '))
            len_obj = channels_obj.__class__.__len__(channels_obj)
            while not tv.isdigit() or int(tv) > len_obj:
                if not tv.isdigit():
                    print('Номер каналу місчтить не лише цифри: ')
                    tv = input('> ')
                else:
                    print('Даного TV каналу не існує: ')
                    tv = input('> ')
            tv = int(tv)
            print(channels_obj[tv-1])
except:
    print('gjg')
