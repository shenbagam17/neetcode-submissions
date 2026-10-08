class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        current = 1
        maximum = 0
        for n in seen:
            if not n-1 in seen:
                while n+current in seen:
                    current +=1
                maximum = max(maximum,current)
            current = 1
        return maximum