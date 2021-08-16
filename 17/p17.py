import inflect

p = inflect.engine()

count = 0
for i in range(1, 1001):
    word = p.number_to_words(i)
    
    for c in word:
        if c.isalpha():
            count += 1

print(count)