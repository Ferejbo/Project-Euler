"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import numpy

"""
Sum of all primes below "below" param
:param below: int,
:return: sum of primes
"""
def sum_of_primes(below: int):
    primes = [2]
    sum = 2

    for i in range(3, below, 2):
        is_prime = True
        for prime in primes:
            if i % prime == 0:
                is_prime = False
            if prime > numpy.sqrt(i):
                break
        
        if is_prime:
            sum += i
            primes.append(i)

    return sum

print(sum_of_primes(2000000))
    