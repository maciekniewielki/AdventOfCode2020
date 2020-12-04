import re

def parse(data):
    passes = []
    i = -1
    for n, line in enumerate(data):
        if line == "" or n == 0:
            i += 1
            passes.append(line)
        else:
            passes[i] += " " + line
    return [p.lstrip() for p in passes]

def mappify(passes):
    passes_mapped = []
    for p in passes:
        m = {}
        pairs = p.split(" ")
        for pair in pairs:
            if pair.strip() == "":
                continue
            k,v = pair.split(":")
            m[k] = v
        passes_mapped.append(m)
    return passes_mapped

def validate_loose(p):
    return "byr" in p and "iyr" in p and "eyr" in p and "hgt" in p and "hcl" in p and "ecl" in p and "pid" in p

def validate_strict(p):
    if not validate_loose(p):
        return False
    try:
        if not (1920 <= int(p["byr"]) <= 2002):
            return False
        if not (2010 <= int(p["iyr"]) <= 2020):
            return False
        if not (2020 <= int(p["eyr"]) <= 2030):
            return False
        if not (("cm" in p["hgt"] and 150 <= int(p["hgt"][:-2]) <= 193) or ("in" in p["hgt"] and 59 <= int(p["hgt"][:-2]) <= 76)):
            return False
        if not (re.search(r'^#([0-9a-f]{6})$', p["hcl"])):
            return False
        if not (p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
            return False
        if not (re.search(r'^([0-9]{9})$', p["pid"])):
            return False
    except:
        return False
    return True

# IO
data = [line.rstrip() for line in open("input.txt").readlines()]
passes = mappify(parse(data))

# 1st
print(sum(1 for p in passes if validate_loose(p)))

# 2nd
print(sum(1 for p in passes if validate_strict(p)))