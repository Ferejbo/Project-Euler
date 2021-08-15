def numbers_to_list(filepath):
    result = []
    with open(filepath, 'r') as f:
        for row in f:
            row = row.rstrip('\n')
            result.append(row.split(' '))
    return result

def product_diagonal(numbers, row, col, adjacent_numbers, reversed):
    temp_product = 1
    count = 0

    if reversed:
        increment = -1
    else:
        increment = 1
    
    col_end = col + increment * adjacent_numbers
    
    for r, c in zip(range(row, row + adjacent_numbers), range(col, col_end, increment)):
        try:
            temp_product *= int(numbers[r][c])
            count += 1
        except IndexError:
            return 0
    
    if count == adjacent_numbers:
        return temp_product
    else:
        return 0

def biggest_product(numbers, adjacent_numbers):
    biggest_product = 0

    for index1, row in enumerate(numbers):
        for index2 in range(0, len(row)):
            print(index1, index2)
            temp_products = []

            temp_products.append(product_diagonal(numbers, index1, index2, adjacent_numbers, False))
            temp_products.append(product_diagonal(numbers, index1, index2, adjacent_numbers, True))
            
            temp_product_horizontal = 1
            temp_product_vertical = 1

            if index2 < len(row) - (adjacent_numbers - 1):
                for x in range(index2, index2 + adjacent_numbers):
                    temp_product_horizontal *= int(numbers[index1][x])
                    temp_product_vertical *= int(numbers[x][index1])

                    temp_products.append(temp_product_horizontal)
                    temp_products.append(temp_product_vertical)

            biggest_temp_product = max(temp_products)

            print(temp_products)

            if biggest_temp_product > biggest_product:
                biggest_product = biggest_temp_product
    
    return biggest_product

def main():
    numbers = numbers_to_list('./11-product/numbers.txt')
    test = [['5', '3', '9'], 
            ['2', '4', '2'], 
            ['1', '2', '1']]
    print(f'Resultat {biggest_product(numbers, 4)}')

if __name__ == '__main__':
    main()
