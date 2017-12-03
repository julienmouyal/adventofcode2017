input = """ """
arr = input.split('\n')

# Part 1

sum = 0

for i in range(len(arr)):
    line = [int(x) for x in arr[i].split()]
    sum += int(max(line)) - int(min(line))
print sum

# Part 2

def compute_line(line):
    for j in range(len(line)):
        for k in range(len(line)):
            if (j != k and line[j] % line[k] == 0):
                return line[j] / line[k]

sum = 0

for i in range(len(arr)):
    line = [int(x) for x in arr[i].split()]
    sum += compute_line(line)

print sum