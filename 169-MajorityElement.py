class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            else:
                d[i] += 1
        x = max(d.values())
        keys = list(d.keys())
        vals = list(d.values())
        pos = vals.index(x)
        return int(keys[pos])


"""
Better Approach

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return nums[n//2]
"""
