import math

def find_sum_of_proper_divisors(num):
    #All numbers are divisible with 1 and itself
    sum = 0
    for i in range(1, math.ceil(num / 2) + 1):
        if num % i == 0:
            sum += i 
    return sum

sum_of_proper_divisors_dict = {}
for i in range(1, 10000):
    sum = find_sum_of_proper_divisors(i)
    sum_of_proper_divisors_dict[i] = sum

sum_total = 0
for key, value in sum_of_proper_divisors_dict.items():
    for key2, value2 in sum_of_proper_divisors_dict.items():
        if value == key2 and value2 == key and key2 != key:
            sum_total += key

print(sum_total)
