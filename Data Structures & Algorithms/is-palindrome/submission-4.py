class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c for c in s if c.isalnum()]
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True