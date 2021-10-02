def Fibonacci_gen(n, a=0,b=1):
    while n:
        yield a
        a, b = b, a+b
        n -= 1