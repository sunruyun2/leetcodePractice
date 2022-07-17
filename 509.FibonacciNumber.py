def fib(n):
    if n<=1:
        return n
    opt1 , opt2 = 0 ,1 
    for i in range(2, n+1):
        res = opt1 + opt2
        opt1 = opt2
        opt2 = res
    return res

for i in range(0, 7):
    print(fib(i))