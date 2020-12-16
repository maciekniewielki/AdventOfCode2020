INPUT = "17,1,3,16,19,0"

def solve(data, times):
    last_said_map = {v:k+1 for k, v in enumerate(data)}
    last_last_said_map = {}
    last_said = data[-1]
    i = len(data)
    while i < times:
        i += 1
        if last_said not in last_said_map:
            last_said = 0
            last_said_map[last_said] = i
        elif last_said not in last_last_said_map:
            last_said = 0
            last_last_said_map[last_said] = last_said_map[last_said]
            last_said_map[last_said] = i
        else:
            last_said = last_said_map[last_said] - last_last_said_map[last_said]
            if last_said in last_said_map:
                last_last_said_map[last_said] = last_said_map[last_said]
            last_said_map[last_said] = i
        data.append(last_said)
    return last_said

# IO
data = [int(line) for line in INPUT.split(",")]

# 1st
print(solve(data, 2020))

# 2nd
print(solve(data, 30000000))
