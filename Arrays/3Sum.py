class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == [] or nums == [0]:
            return []
        x = len(nums)
        nums.sort()
        ans = []
        for i in range(0, x):
            left = i + 1
            right = x - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1

                else:
                    right += 1

        return ans
