CYCLES = 6


def simulate_for_cycles(starting_data, cycles):
    data = copy_data(starting_data)
    next_state = copy_data(data)
    for _ in range(cycles):
        next_state = simulate_step(data)
        data = next_state
    return count_active_all(data)


def simulate_step(data):
    next_step = copy_data(data)
    for z, rest in enumerate(data):
        for y, row in enumerate(rest):
            for x, seat in enumerate(row):
                neighbours = count_neighbours(data, x, y, z)
                if seat == "." and neighbours == 3:
                    next_step[z][y][x] = "#"
                elif seat == "#" and not (3 >= neighbours >= 2):
                    next_step[z][y][x] = "."
    return next_step


def count_neighbours(data, x, y, z):
    active = 0
    for h in range(z-1, z+2):
        for i in range(y-1, y+2):
            for j in range(x-1, x+2):
                if i == y and j == x and h == z:
                    continue
                seat = get_seat(data, j, i, h)
                if seat is None:
                    continue
                if seat == "#":
                    active += 1
    return active


def get_seat(data, x, y, z):
    if z >= 0 and z < len(data):
        if y >= 0 and y < len(data[z]):
            if x >= 0 and x < len(data[z][y]):
                return data[z][y][x]
    return None


def count_active_all(data):
    active = 0
    for _, rest in enumerate(data):
        for _, row in enumerate(rest):
            for _, seat in enumerate(row):
                if seat == "#":
                    active += 1
    return active


def get_empty_slice(data):
    return [["."] * len(row) for row in data]


def copy_data(data):
    copied = [[["."] * len(row) for row in data_2d] for data_2d in data]
    for z, rest in enumerate(data):
        for y, row in enumerate(rest):
            for x, val in enumerate(row):
                copied[z][y][x] = val
    return copied


# IO
starting_data = [CYCLES*["."]+list(line.rstrip())+CYCLES*["."]
                 for line in open("input.txt").readlines()]
starting_data = [["."] * len(starting_data[0]) for _ in range(CYCLES)] + \
    starting_data + [["."] * len(starting_data[0]) for _ in range(CYCLES)]
data_3d = [starting_data]
for _ in range(CYCLES):
    data_3d.insert(0, get_empty_slice(starting_data))
for _ in range(CYCLES):
    data_3d.append(get_empty_slice(starting_data))

# 1st
print(simulate_for_cycles(data_3d, CYCLES))
