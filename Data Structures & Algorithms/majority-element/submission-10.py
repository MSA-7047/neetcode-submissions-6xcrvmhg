class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxNum = 0
        maxCount = 0
        for i in nums:
            if maxCount == 0:
                maxNum = i
            if i == maxNum:
                maxCount += 1
            else:
                maxCount -= 1
        return maxNum