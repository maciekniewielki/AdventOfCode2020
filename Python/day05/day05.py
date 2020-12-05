def to_id(line):
    return int(line.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0"), 2)

# IO
data = [line.rstrip() for line in open("input.txt").readlines()]
taken_seats = set(to_id(line) for line in data)

# 1st
print(max(taken_seats))

# 2nd
possible_seats = set(range(min(taken_seats), max(taken_seats)))
print((possible_seats - taken_seats).pop())