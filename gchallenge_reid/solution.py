import math

def is_prime(n):
    isprime = True
    
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0: 
            isprime = False
            return isprime
    if isprime:
        return isprime

def answer(n):
    count = 2
    prime = []
    while len(prime) <= 1000:
        if is_prime(count):
            prime.append(count)
        count+=1
    
    string_prime = ''.join(str(e) for e in prime)
    return string_prime[n:n+5]
