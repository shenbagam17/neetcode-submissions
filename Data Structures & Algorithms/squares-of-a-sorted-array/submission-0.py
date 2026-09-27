class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n-1
        res = [0] * n
        for pos in range(n-1,-1,-1):
            ls = nums[l]*nums[l]
            rs = nums[r]*nums[r]
            if ls<rs:
                res[pos] = rs
                r -=1
            else:
                res[pos] = ls
                l +=1
        return res