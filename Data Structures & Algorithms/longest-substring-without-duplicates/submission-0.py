class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        maximum = 0
        for right, char in enumerate(s):
            if char in seen and seen[char] >=left:
                left = seen[char] + 1
            seen[char] = right
            maximum = max(maximum,right-left+1)
        return maximum