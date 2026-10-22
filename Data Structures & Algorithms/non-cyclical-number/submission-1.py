class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            n = self.get_value(n)
        return True
    def get_value(self, n):
        total = 0
        while n:
            digit = n%10
            total += digit*digit
            n //=10
        return total