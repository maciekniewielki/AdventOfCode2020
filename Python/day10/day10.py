def get_differences(adapters):
    diffs = {n:0 for n in range(1,4)}
    for prev, curr in zip(adapters, adapters[1:]):
        diffs[curr - prev] += 1
    return diffs

def count_total_ways_to_reach(total_ways_partial, adapters, to_reach):
    from_index = max(0, indexes[to_reach]-3)
    to_index = indexes[to_reach]
    before = [x for x in adapters[from_index:to_index] if to_reach - x <= 3]   
    if not before:
        return 1
    return sum(total_ways_partial[x] for x in before)

# IO
data = [int(line.rstrip()) for line in open("input.txt").readlines()]
adapters = data[:] + [max(data)+3] + [0]
sorted_ad = list(sorted(adapters))
indexes = {a:sorted_ad.index(a) for a in sorted_ad}

#1st
diffs = get_differences(sorted_ad)
print(diffs[1]*diffs[3])

# 2nd
total_ways = {}
for adapter in sorted_ad:
    total_ways[adapter] = count_total_ways_to_reach(total_ways, sorted_ad, adapter)
print(total_ways[sorted_ad[-1]])