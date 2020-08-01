def n():
    a = int(input())
    if a == 0:
        print(0)
    else:
        n()
        print(a)


(n())
