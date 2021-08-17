factorial = 1

for i in range(100, 1, -1):
    factorial *= i

sum = 0

for c in str(factorial):
    sum += int(c)

print(sum)