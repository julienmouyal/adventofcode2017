input = """ """


def escape_maze(part):
    line = [int(x) for x in input.split('\n')]
    index = 0
    count = 0

    while True:
        count += 1
        jump = line[index]
        increment = -1 if jump >= 3 and part == 2 else 1
        line[index] = line[index] + increment
        index += jump
        if index >= len(line):
            break

    print count

# Part 1
escape_maze(1)
# Part 2
escape_maze(2)
