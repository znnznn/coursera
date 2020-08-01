n = int(input())
fp1 = 0
fn2 = 1
i = 1
fib = 1
while i < n:
    fib = fp1 + fn2
    fp1 = fn2
    fn2 = fib
    i += 1
print(fib)