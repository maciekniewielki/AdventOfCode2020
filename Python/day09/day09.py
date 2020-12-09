def exists_sum(nums, target):
    complements = set()
    for num in nums:
        complement = target - num
        if num in complements:
            return True
        complements.add(complement)
    return False

def get_invalid(data):
    for i, num in enumerate(data):
        if i < 25:
            continue
        if not exists_sum(data[i-25:i], num):
            return num
        
def get_contiguous_range(data, num):
    n = len(data)
    for j in range(n):
        for i in range(j):
            if sum(data[i:j]) == num:
                return data[i:j]

# IO
data = [int(line.rstrip()) for line in open("input.txt").readlines()]

#1st
num = get_invalid(data)
print(num)

# 2nd
components = get_contiguous_range(data, num)
print(min(components) + max(components))