"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


# def primes(number_of_primes):
#     list = []
#     for possiblePrime in range(2, 90):
    
#         isPrime = True
#         for num in range(2, possiblePrime):
#             if possiblePrime % num == 0:
#                 isPrime = False
            
#         if isPrime:
#             list.append(possiblePrime)
            
#     return list[0:number_of_primes]
def primes (number_of_primes) :
    list = []
    num = 2
    i=0
    while i < number_of_primes:
        prime = True
        for j in range (2, num) :
            if num % j == 0:
                prime = False
        if prime:
            list.append (num)
            i=i
        num = num +1
    return list