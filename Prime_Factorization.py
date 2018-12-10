'''
Find all Prime Facotrs(if there are any) and display them.
'''

def isPrime(i):
    for j in range(2,i):
        if i % j == 0:
            return False
    return True

def prime_factorization(n):
    if n < 2:
        return '{} is not a prime number'.format(n)
    
    factor = []
    prime_factor = []
    for i in range(2,n+1):
        if n % i == 0:
            factor.append(i)

    for n in factor:
        if isPrime(n):
            prime_factor.append(n)
            continue
            
    return prime_factor
