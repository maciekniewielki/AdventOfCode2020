import re

def parse(data):
    groups = []
    i = -1
    for n, line in enumerate(data):
        if line == "" or n == 0:
            i += 1
            groups.append(line)
        else:
            groups[i] += " " + line
    return [p.lstrip() for p in groups]


def answered_all(group):
    answers = group.split(" ")
    all_answered = None
    for answer in answers:
        if all_answered is None:
            all_answered = set(answer)
        else:
            all_answered &= set(answer)
    return len(all_answered)



# IO
data = [line.rstrip() for line in open("input.txt").readlines()]
groups = parse(data)

# 1st
print(sum(len(set(g.replace(" ", ""))) for g in groups))

# 2nd
print(sum(answered_all(g) for g in groups))