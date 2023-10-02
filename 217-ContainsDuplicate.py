class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            else:
                d[i]+=1
        for j in list(d.keys()):
            if d[j]>=1:
                return True
            else:
                continue
        return False
    
'''
Better Approach

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
'''