class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(c for c in s if c.isalnum())

        l = 0
        r = len(string) - 1
        while l<r:
            if string[l].lower() != string[r].lower():
                return False
            l += 1
            r -= 1
        return True