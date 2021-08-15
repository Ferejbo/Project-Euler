def find_sequence_count(num):
    count = 1
    while True:
        if num == 1:
            return count
        elif num % 2 == 0:
            num = num / 2
            count += 1
        else:
            num = 3 * num + 1
            count += 1

        
def find_biggest_sequence(biggest_starting_number):
    i = 2
    biggest_seq = 1
    starting_number_with_biggest_seq = 1
    while i < biggest_starting_number:
        seq_count = find_sequence_count(i)

        if seq_count > biggest_seq:
            biggest_seq = seq_count
            starting_number_with_biggest_seq = i

        i += 1
    
    return starting_number_with_biggest_seq, biggest_seq

print(find_biggest_sequence(1000000))