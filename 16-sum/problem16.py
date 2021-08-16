

def digit_sum_of_int(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum

print(digit_sum_of_int(2**1000))