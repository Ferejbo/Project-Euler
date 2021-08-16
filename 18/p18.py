def txt_to_2d_array(filepath):
    pyramid = []
    with open (filepath, 'r') as f:
        for row in f:
            row = row.rstrip('\n')
            pyramid.append(row.split(' '))
    return pyramid

def find_max_path(pyramid):

    biggest_path = 0
    for row_index, row in reversed(list(enumerate(pyramid))):
        for col_index, col in enumerate(row[:-1]):
            
            if col > row[col_index + 1]:
                pyramid[row_index - 1][col_index] = int(col) + int(pyramid[row_index - 1][col_index])
            else:
                pyramid[row_index - 1][col_index] = int(row[col_index + 1]) + int(pyramid[row_index - 1][col_index])
    return pyramid[0][0]

if __name__ == '__main__':
    pyramid = txt_to_2d_array('./18/pyramid.txt')
    print(find_max_path(pyramid))
