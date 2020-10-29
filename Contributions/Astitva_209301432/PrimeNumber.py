"""
Optimized approach to check prime number.
Any negative number can never be prime and 1 is not prime.
For all other numbers, if a factor does not exist in range 2 till root of the number, it will not have a factor and will be prime.
"""

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)):
        if num%i == 0:
            return False
    return True
    
num = int(input('Enter number: '))
print(num, 'is prime' if isPrime(num) else 'is not prime')