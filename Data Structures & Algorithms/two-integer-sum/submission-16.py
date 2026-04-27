class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in dct:
                return [dct[diff], index]
            dct[number] = index 