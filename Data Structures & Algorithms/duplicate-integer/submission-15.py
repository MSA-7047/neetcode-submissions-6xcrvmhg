class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        setnums = set()
        for i in nums:
            if i in setnums:
                return True
            setnums.add(i)
        return False