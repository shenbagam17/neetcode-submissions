class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]: 
        n = len(nums)
        prefix = [0]*n
        prefix[0] = 1
        res = [0]*n
        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]
        suffix = 1
        for i in range(n-1,-1,-1):
            res[i] = suffix*prefix[i]
            suffix = suffix * nums[i]
        return res