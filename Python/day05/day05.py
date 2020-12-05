def to_id(line):
    return int(line.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0"), 2)

def pick_middle(seats):
    prev = None
    for seat in sorted(seats):
        if prev is None:
            prev = seat
            continue
        if seat - prev != 1:
            return seat
        prev = seat


# IO
data = [line.rstrip() for line in open("input.txt").readlines()]
ids = [to_id(line) for line in data]

# 1st
print(max(ids))

# 2nd
free_seats = set(range(2**10)) - set(ids)
print(pick_middle(free_seats))