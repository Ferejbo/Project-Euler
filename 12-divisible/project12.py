import math

def find_divisor_count(num):
    #All numbers are divisible with 1 and itself
    count = 2
    for i in range(2, math.ceil(math.sqrt(num))):
        if num % i == 0:
            count += 1
            if i != num / i:
                count += 1
    return count

def find_triangular_number(divisor_count_threshold):
    done = False
    i = 28
    increment = 7
    test = 20
    while not done:
        increment += 1
        i += increment

        divisor_count = find_divisor_count(i)
        if divisor_count > divisor_count_threshold:
            return i
        
        # print(i, divisor_count)
        test += 20
        


if __name__ == '__main__':
    print(find_triangular_number(500))