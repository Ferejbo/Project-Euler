"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import numpy

def find_triplet():
    for b in range(0, 1000):
        for a in range(0, b):
            c = numpy.sqrt(a**2 + b**2)

            if c > b and b > a:
                if a + b + c == 1000:
                    return a * b * c

    return None

print(find_triplet())