class Solution:
    def climbStairs(self, n: int) -> int:
        last = 1
        last_bf = 0
        for i in range(n):
            no_of_ways = last + last_bf
            last_bf = last
            last = no_of_ways
        return no_of_ways