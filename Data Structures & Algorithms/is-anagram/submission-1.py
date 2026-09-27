class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for i in s:
            count[i] = 1+count.get(i,0)
        for j in t:
            count[j] = count.get(j,0) - 1
        for c in count.values():
            if c !=0:
                return False
        return True