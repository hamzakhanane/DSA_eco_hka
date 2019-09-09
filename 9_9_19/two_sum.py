# Runtime O(n)
# Memory O(n)

def twoSum(nums, target):
        dict = {}
        i = 0
        while i < len(nums):
            diff = target - nums[i]
            if diff in dict:
                return [dict[diff], i]
            else:
                dict[nums[i]] = i
            i += 1