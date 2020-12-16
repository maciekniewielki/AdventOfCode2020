import re


def parse(data):
    end_of_classes = data.index("")
    end_of_my_ticket = data.index("", end_of_classes+1)
    classes = data[:end_of_classes]
    ranges = {}
    for c in classes:
        name, rest = c.split(":")
        nums = re.findall(r'\d+', rest)
        ranges[name] = []
        for n in range(0, len(nums), 2):
            from_num, to_num = int(nums[n]), int(nums[n+1])
            ranges[name].append((from_num, to_num))

    tickets = data[end_of_my_ticket+2:]
    tickets = [to_nums(t) for t in tickets]
    my_ticket = to_nums(data[end_of_my_ticket-1])

    return ranges, tickets, my_ticket


def to_nums(t):
    ticket = []
    for num in t.split(","):
        num = int(num)
        ticket.append(num)
    return ticket


def solve_1(ranges, tickets, my_ticket):
    error_rate = 0
    for t in tickets:
        for num in t:
            if is_invalid(num, ranges):
                error_rate += num
    return error_rate


def is_invalid(number, ranges):
    return all(number > to_num or number < from_num for k in ranges for from_num, to_num in ranges[k])


def solve_2(ranges, tickets, my_ticket):
    filtered_tickets = []
    for t in tickets:
        if not is_invalid_ticket(t, ranges):
            filtered_tickets.append(t)

    fit_map = {}
    for field in ranges:
        fit_map[field] = []
        for n in range(len(ranges)):
            if fits(ranges[field], n, filtered_tickets):
                fit_map[field].append(n)

    precise_places = {}
    while len(fit_map):
        field, place = find_single_field(fit_map)
        if field is None:
            return "ARG!"
        precise_places[field] = place
        clear_place_and_field(fit_map, field, place)

    prod = 1
    for name in precise_places:
        if name.startswith("departure"):
            prod *= my_ticket[precise_places[name]]
    return prod


def is_invalid_ticket(t, ranges):
    return any(is_invalid(number, ranges) for number in t)


def fits_ticket(num, r):
    for from_num, to_num in r:
        if num <= to_num and num >= from_num:
            return True
    return False


def fits(r, place, tickets):
    for t in tickets:
        num = t[place]
        if not fits_ticket(num, r):
            return False
    return True


def find_single_field(fit_map):
    for name in fit_map:
        if len(fit_map[name]) == 1:
            return name, fit_map[name][0]
    return None, None


def clear_place_and_field(fit_map, field, place):
    fit_map.pop(field, None)
    for name in fit_map:
        fit_map[name].remove(place)


# IO
data = [line.rstrip() for line in open("input.txt").readlines()]
ranges, tickets, my_ticket = parse(data)


# 1st
print(solve_1(ranges, tickets, my_ticket))

# 2nd
print(solve_2(ranges, tickets, my_ticket))
