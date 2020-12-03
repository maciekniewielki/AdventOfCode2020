def find_trees(data, right, down):
    x, y, acc = 0, 0, 0
    while y < len(data):
        if data[y][x % len(data[y])] == "#":
            acc += 1
        x += right
        y += down
    return acc

# IO
data = [line.rstrip() for line in open("input.txt").readlines()]

# 1st
print(find_trees(data, 3, 1))

# 2nd
print(find_trees(data, 1, 1) * find_trees(data, 3, 1) * find_trees(data, 5, 1) * find_trees(data, 7, 1) * find_trees(data, 1, 2))