input = 347991

max_right = 0
max_up = 0
max_left = 0
max_down = 0

x = 0
y = 0

def move():
    global x, y, max_right, max_up, max_left, max_down

    if(max_right <= max_up and max_right <= max_left and max_right <= max_down):
        if(x >= max_right):
            max_right += 1
        x += 1
    elif(max_up <= max_left and max_up <= max_down):
        if(y >= max_up):
            max_up += 1
        y += 1
    elif(max_left <= max_down):
        if(-x >= max_left):
            max_left += 1
        x -= 1
    else:
        if(-y >= max_down):
            max_down += 1
        y -= 1

# Part 1

for i in range(2, input + 1):
    move()

print abs(x) + abs(y)


# Part 2

max_right = 0
max_up = 0
max_left = 0
max_down = 0

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