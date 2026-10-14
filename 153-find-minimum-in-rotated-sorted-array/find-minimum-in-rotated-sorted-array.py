class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]
        l = 0
        r = len(nums) - 1
        res = nums[l]
        while True:
            if nums[l] > nums[r]:
                l += 1
            else:
                res = nums[l]
                break
        return res