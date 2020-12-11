possible_vectors = [
    (y,x) for x in range(-1, 2) for y in range(-1, 2) if not (x == 0 and y == 0)
]

def simulate_until_eq(starting_data, weird_counting = False):
    data = copy_data(starting_data)
    next_state = copy_data(data)
    while True:
        next_state = simulate_step(data, weird_counting)
        if (check_equal(data, next_state)):
            break
        data = next_state
    return count_occupied_all(data)

def simulate_step(data, weird_counting = False):
    next_step = copy_data(data)
    for y, row in enumerate(data):
        for x, seat in enumerate(row):
            if seat == "L" and count_neighbours(data, x, y, weird_counting) == 0:
                next_step[y][x] = "#"
            elif seat == "#" and count_neighbours(data, x, y, weird_counting) >= 4 + weird_counting:
                next_step[y][x] = "L"
            else:
                next_step[y][x] = seat
    return next_step

def count_neighbours(data, x, y, weird_counting = False):
    if not weird_counting:
        return count_normal(data, x , y)
    else:
        return count_weird(data, x, y)

def count_normal(data, x, y):
    occupied = 0
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if i == y and j == x:
                continue
            seat = get_seat(data, j, i)
            if seat is None:
                continue
            if seat == "#":
                occupied += 1

    return occupied

def count_weird(data, x, y):
    occupied = 0
    for v in possible_vectors:
        i = 0
        while True:
            i += 1
            v_y, v_x = v
            seat = get_seat(data, x+v_x*i, y+v_y*i)
            if seat == ".":
                continue
            if seat == "#":
                occupied += 1
            break
    return occupied

def get_seat(data, x, y):
    if y >= 0 and y < len(data):
        if x >= 0 and x < len(data[0]):
            return data[y][x]
    return None

def count_occupied_all(data):
    occupied = 0
    for _, row in enumerate(data):
        for _, seat in enumerate(row):
            if seat == "#":
                occupied += 1
    return occupied

def check_equal(state1, state2):
    for y, row in enumerate(state1):
        for x, _ in enumerate(row):
            if state1[y][x] != state2[y][x]:
                return False
    return True

def copy_data(data):
    copied = [[" "] * len(row) for row in data]
    for y, row in enumerate(data):
        for x, seat in enumerate(row):
            copied[y][x] = seat
    return copied
        
# IO
starting_data = [list(line.rstrip()) for line in open("input.txt").readlines()]

#1st
print(simulate_until_eq(starting_data))

# 2nd
print(simulate_until_eq(starting_data, True))