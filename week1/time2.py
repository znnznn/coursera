# скільки годин і хвилин знаючи скільки пройшло секунд
seconds = int(input())
hours = (seconds // 60 // 60 % 24)
minuts1 = ((seconds // 60) % 60 // 10)
minuts2 = ((seconds // 60) % 60 % 10)
sec1 = (seconds % 60 // 10)
sec2 = (seconds % 60 % 10)
print(hours, ':', minuts1, minuts2, ':', sec1, sec2, sep='')
