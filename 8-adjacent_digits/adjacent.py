"""Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. 
What is the value of this product?"""

"""
Converts txt file to array. Element in array equals one line in txt
:param txtfile: path(string) to txt file
:return: array
"""
def txt_to_array(txtfile: str):
    file_object  = open(txtfile, "r")
    result_arr = []

    readlines = file_object.read().splitlines()
    for r in readlines:
        result_arr.append(r)

    return result_arr


"""
Finds biggest product of n adjacent digits in 'digits'
:param digits: string to be analyzed
:param n: int, states how many adjacent digits were looking for. Cant be bigger than len of digits or equal to 0
:param biggest_product: biggest product so far. 
:return: biggest product in digits. None if invalid params
"""
def biggest_adjacent_digitproduct(digits: str, n: int, biggest_product: int):

    if n > len(digits) or n == 0:
        return None
    
    for i in range (0, len(digits) - (n - 1)):
        last_digit = i + n - 1

        # break out of loop if out if scope
        if last_digit >= len(digits):
            break
        
        temp_product = 1
        for x in range(i, last_digit + 1):
            temp_product *= int(digits[x])
        
        if temp_product > biggest_product:
            biggest_product = temp_product

    return biggest_product

"""
Finds biggest product of n adjacent digits in array. Uses biggest_adjacent_digitproduct() on each respective row.
:param digits_arr: list of long numbers
:param n: how many adjacent digits were calculating product from
:return: biggest product in list
"""
def biggest_product_of_rows_of_digits(digits_arr: list, n: int):
    biggest_product = 0

    for digits in digits_arr:
        temp_product = biggest_adjacent_digitproduct(digits, n, biggest_product)

        if temp_product > biggest_product:
            biggest_product = temp_product
    
    return biggest_product

numbers_arr = txt_to_array("8-adjacent_digits/digits.txt")

check = ""
for num in numbers_arr:
    check += num

# misunderstood question. The answer lies in this print statement
print(biggest_adjacent_digitproduct(check, 13, 0))
