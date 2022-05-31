class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros = zeros + 1
            elif nums[i] == 1:
                ones = ones + 1

        for i in range(len(nums)):
            if zeros > 0:
                nums[i] = 0
                zeros = zeros - 1
            elif ones > 0:
                nums[i] = 1
                ones = ones - 1
            else:
                nums[i] = 2

        return nums