MY_BAG = "shiny gold"

def parse_line(l):
    bag, content = l.split("contain")
    bag = " ".join(bag.strip().split(" ")[:-1])
    content = content.strip()[:-1].split(", ")
    if (len(content) == 1 and len(content[0].split(" ")) == 3):
        return (bag, None)
    else:
        return (bag, [parse_content(c) for c in content])

def parse_content(c):
    try:
        amount, name1, name2, _ = c.split(" ")
        amount = int(amount)
        name = name1 + " " + name2
        return (name, amount)
    except:
        return None

def bag_contains_my_bag(bags, name):
    content = bags[name]
    if content != None:
        return any((cont[0] == MY_BAG or bag_contains_my_bag(bags, cont[0])) for cont in content)
    else:
        return False

def count_all_inside(bags, name):
    s = 0
    if bags[name] is None:
        return 0
    for content in bags[name]:
        how_many = content[1]
        s += how_many
        s += how_many * count_all_inside(bags, content[0])
    return s

# IO
data = [line.rstrip() for line in open("input.txt").readlines()]
bags = {}
for d in data:
    bag, content = parse_line(d)
    bags[bag] = content


# 1st
print(sum(bag_contains_my_bag(bags, b) for b in bags if b != MY_BAG))

# 2nd
print(count_all_inside(bags, MY_BAG))