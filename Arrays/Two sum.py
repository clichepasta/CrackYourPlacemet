class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numDict = {}

        for i, num in enumerate(nums):

            if target - num in numDict and numDict[target - num] != i:
                return [numDict[target - num], i]

            numDict[num] = i