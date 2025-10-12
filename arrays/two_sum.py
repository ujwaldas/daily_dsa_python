# LeetCode Problem: Two Sum
# Author: Rancid_engineer

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []

if __name__ == "__main__":
    print(two_sum([2,8,11,15], 9))
