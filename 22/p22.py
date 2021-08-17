import re

names = []

with open('./22/p022_names.txt', 'r') as f:
    for l in f:
        l = re.sub('[^A-Z,]', '', l)
        names = list(l.split(','))

names.sort()

subtract_ascii_value = 64
total_points = 0

for index, name in enumerate(names):

    index += 1
    sum_of_value_of_letters = 0
    for char in name:
        sum_of_value_of_letters += ord(char) - subtract_ascii_value
    
    total_points += sum_of_value_of_letters * index

print(total_points)
    