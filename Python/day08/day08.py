def run(data):
    acc = 0
    p = 0
    executed = set()
    while True:
        if p >= len(data) or p < 0:
            return (True, acc)
        if p in executed:
            return (False, acc)
        executed.add(p)
        
        op, arg = data[p].split(" ")
        if op == "nop":
            p += 1
        elif op == "acc":
            acc += int(arg)
            p += 1
        elif op == "jmp":
            p += int(arg)

# IO
data = [line.rstrip() for line in open("input.txt").readlines()]

#1st
_, acc = run(data)
print(acc)

# 2nd
for i in range(len(data)):
    d = data[:]
    if "jmp" in d[i]:
        d[i] = d[i].replace("jmp", "nop")
    elif "nop" in d[i]:
        d[i] = d[i].replace("nop", "jmp")
    halted, acc = run(d)
    if halted:
        print(acc)
        break