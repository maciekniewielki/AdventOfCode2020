# 0 -- east
# 1 -- north
# 2 -- west
# 3 -- south
forward = {
    0: (1, 0),
    1: (0, 1),
    2: (-1, 0),
    3: (0, -1)
}

def solve_1(commands):
    pos = [0, 0]
    direction = 0
    for command in commands:
        letter, number = command[0], command[1:]
        number = int(number)
        if letter == "N":
            pos[1] += number
        elif letter == "S":
            pos[1] -= number
        elif letter == "E":
            pos[0] += number
        elif letter == "W":
            pos[0] -= number
        elif letter == "L":
            direction = (direction + number // 90) % 4
        elif letter == "R":
            direction = (direction - number // 90) % 4
        elif letter == "F":
            x, y = forward[direction]
            pos[0] += x * number
            pos[1] += y * number
    return abs(pos[0]) + abs(pos[1])

def solve_2(commands):
    pos_w = [10, 1]
    pos = [0, 0]
    for command in commands:
        letter, number = command[0], command[1:]
        number = int(number)
        if letter == "N":
            pos_w[1] += number
        elif letter == "S":
            pos_w[1] -= number
        elif letter == "E":
            pos_w[0] += number
        elif letter == "W":
            pos_w[0] -= number
        elif letter == "L":
            how_many = number // 90
            for _ in range(how_many):
                pos_w[0], pos_w[1] = pos_w[1], pos_w[0]
                pos_w[0] = -pos_w[0]
        elif letter == "R":
            how_many = number // 90
            for _ in range(how_many):
                pos_w[0], pos_w[1] = pos_w[1], pos_w[0]
                pos_w[1] = -pos_w[1]
        elif letter == "F":
            pos[0] += pos_w[0] * number
            pos[1] += pos_w[1] * number
    return abs(pos[0]) + abs(pos[1])

        
# IO
data = [line.rstrip() for line in open("input.txt").readlines()]

#1st
print(solve_1(data))

# 2nd
print(solve_2(data))