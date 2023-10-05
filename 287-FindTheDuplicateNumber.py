class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for j in list(d.keys()):
            if d[j] > 1:
                return j


"""
Better Approach

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = set()
        for i in nums:
            if i in d:
                return i
            d.add(i)
"""
