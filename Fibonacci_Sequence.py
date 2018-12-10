'''
Enter a number and have the program generate the Fibonacci sequence to the Nth number.
'''
# Method 1: print out each value. Make use of tuple packing
def fib(n):
    a = 1
    b = 1
    for x in range(n):
        print(a)
        a,b = b, a+b

# Method 2: generator. Make use of tuple packing and generator
def gen_fib(n):
    a = 1
    b = 1
    for x in range(n):
        yield a
        a,b = b, a+b
# For example, n = 10
for x in gen_fib(10):
    print(x)
