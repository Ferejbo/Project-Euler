
with open('./13-number/yikes.txt', 'r') as f:
    sum = 0
    for row in f:
        row = row.rstrip('\n')
        sum += int(row)
    print(str(sum)[0:10])