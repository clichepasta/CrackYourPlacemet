class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        y = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[y] = nums[i]
                y = y + 1

        return y
