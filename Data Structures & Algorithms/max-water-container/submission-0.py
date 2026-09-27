class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        n = len(heights)
        l = 0
        r = n-1
        while l<r:
            length = r-l
            area = length * min(heights[l],heights[r])
            maximum = max(maximum, area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maximum 