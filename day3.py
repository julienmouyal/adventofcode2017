input = 347991

maxRight = 0
maxUp = 0
maxLeft = 0
maxDown = 0

x = 0
y = 0

def move():
    global x, y, maxRight, maxUp, maxLeft, maxDown

    if(maxRight <= maxUp and maxRight <= maxLeft and maxRight <= maxDown):
        if(x >= maxRight):
            maxRight += 1
        x += 1
    elif(maxUp <= maxLeft and maxUp <= maxDown):
        if(y >= maxUp):
            maxUp += 1
        y += 1
    elif(maxLeft <= maxDown):
        if(-x >= maxLeft):
            maxLeft += 1
        x -= 1
    else:
        if(-y >= maxDown):
            maxDown += 1
        y -= 1

# Part 1

for i in range(2, input + 1):
    move()

print abs(x) + abs(y)


# Part 2

maxRight = 0
maxUp = 0
maxLeft = 0
maxDown = 0

x = 0
y = 0

def compute_square():
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if(i == 0 and j == 0):
                continue
            sum += values_map.get(''.join([str(x + i), str(y + j)]), 0)
    return sum

values_map = {}
values_map[''.join([str(x), str(y)])] = 1

last_value = 1

while True:
    move()
    last_value = compute_square()
    values_map[''.join([str(x), str(y)])] = last_value
    if last_value > input:
        break

print last_value