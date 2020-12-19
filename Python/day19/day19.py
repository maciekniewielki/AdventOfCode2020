import re


def parse(data):
    rules = {}
    parsing_rules = True
    messages = []
    for line in data:
        if line == "":
            parsing_rules = False
            continue
        if parsing_rules:
            key, rest = line.split(":")
            key = int(key)
            rest = rest.strip()
            if "\"" in line:
                rules[key] = rest[1]
            else:
                groups = rest.split("|")
                sub_rules = []
                for g in groups:
                    nums = [int(num) for num in g.strip().split()]
                    sub_rules.append(nums)
                rules[key] = sub_rules
        else:
            messages.append(line)
    return rules, messages


def solve_1(data):
    rules, messages = parse(data)
    rule_0 = "^" + unwrap_match(rules, 0) + "$"
    matched = [message for message in messages if bool(
        re.match(rule_0, message))]
    return matched


def unwrap_match(rules, which):
    restrictions = rules[which]
    if isinstance(restrictions, str):
        return restrictions

    groups = []
    for r in restrictions:
        restriction = "".join(unwrap_match(rules, i) for i in r)
        groups.append(restriction)
    if len(groups) == 1:
        return "(" + groups[0] + ")"
    return connect_or(groups)


def connect_or(groups):
    return "(("+")|(".join(restriction for restriction in groups) + "))"


def solve_2(data):
    rules, messages = parse(data)
    max_length = max(len(m) for m in messages)
    additional_rules_8 = gen_8_rules(max_length)
    additional_rules_11 = gen_11_rules(max_length)

    rules[0] = [[max(additional_rules_8), max(additional_rules_11)]]
    rules = {**rules, **additional_rules_8, **additional_rules_11}

    rule_0 = "^" + unwrap_match(rules, 0) + "$"
    matched = [message for message in messages if bool(
        re.match(rule_0, message))]
    return matched


def gen_8_rules(max_length):
    base_8 = 8000
    rule_chain = {}
    prev_key = 8
    for x in range(max_length):
        key = base_8 + x
        rule_chain[key] = [[42], [42, prev_key]]
        prev_key = key
    return rule_chain


def gen_11_rules(max_length):
    base_11 = 11000
    rule_chain = {}
    prev_key = 11
    for x in range(max_length):
        key = base_11 + x
        rule_chain[key] = [[42, 31], [42, prev_key, 31]]
        prev_key = key
    return rule_chain


# IO
data = [line.rstrip() for line in open("input.txt").readlines()]

# 1st
print(len(solve_1(data)))

# 2nd
print(len(solve_2(data)))
