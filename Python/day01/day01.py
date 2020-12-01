def solve_for_two(nums, target):
    complements = set()
    for num in nums:
        complement = target - num
        if num in complements:
            return num * complement
        complements.add(complement)
    # should not happen
    return 0

def solve_for_three(nums, target):
    for i, num in enumerate(nums):
        subproduct = solve_for_two(nums[i+1:], target - num)
        if subproduct != 0:
            return subproduct * num
    # should not happen
    return 0

# IO
nums = list(map(int, open("input.txt").readlines()))

# 1st
print(solve_for_two(nums, 2020))

# 2nd
print(solve_for_three(nums, 2020))