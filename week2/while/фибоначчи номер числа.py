n = int(input())
if n == 0:
    print(0)
else:
    fp1 = 0
    fn2 = 1
    i = 1
    fib = 1
    while fib <= n:
        fib = fp1 + fn2
        fp1 = fn2
        fn2 = fib
        i += 1
        if fib == n:
            print(i)
            break
    else:
        print(-1)
