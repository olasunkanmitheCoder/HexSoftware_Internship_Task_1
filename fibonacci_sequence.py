print("Fibonacci Infinite series generator:")
def fib(a, b):
    
    while True:
        yield a #State preservation
        a,b=b, a+b

a, b = 0, 1
for i in fib(a, b):
    if i > 1000000000:
        break
    print(i, end=' ')





