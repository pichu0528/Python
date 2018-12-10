'''
Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
'''

def isPrime(i):
    for j in range(2,i):
        if i % j == 0:
            return False
    return True

def find_next_prime(n):
    for i in range(2,n):
        if isPrime(i):
            print(i)
        else:
            continue
