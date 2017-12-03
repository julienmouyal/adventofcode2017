# Part 1

input = ''
n = len(input)

sum = 0

for i in range(n):
    if input[i] == input[(i + 1) % n]:
        sum += int(input[i])

print sum

# Part 2

sum = 0

for i in range(n):
    if input[i] == input[(i + n / 2) % n]:
        sum += int(input[i])

print sum