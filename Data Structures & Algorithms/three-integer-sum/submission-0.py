class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res = []
        for i in range(n-2):
            if(nums[i]>0):
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                sum = nums[l] + nums[i] + nums[r]
                if sum >0:
                    r -=1
                elif sum<0:
                    l +=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l +=1
                    while r<n-1 and nums[r] == nums[r-1]:
                        r -=1
                    l,r = l+1,r-1
        return res
                    

