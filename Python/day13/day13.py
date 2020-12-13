import math
from functools import reduce


def solve_1(data):
    timestamp = int(data[0])
    all_ids = data[1].split(",")
    mins = {}
    for x in all_ids:
        if x == "x":
            continue
        x = int(x)
        minutes = math.ceil(timestamp / x) * x - timestamp
        mins[minutes] = x
    bus = min(_ for _ in mins)
    bus_id = mins[bus]
    return bus * bus_id


def solve_2(data):
    all_ids = data[1].split(",")
    ids = []
    mins = []
    for i, x in enumerate(all_ids):
        if x == "x":
            continue
        x = int(x)
        ids.append(x)
        mins.append(-i % x)
    return chinese_remainder(ids, mins)


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


# IO
data = [line.rstrip() for line in open("input.txt").readlines()]

# 1st
print(solve_1(data))

# 2nd
print(solve_2(data))