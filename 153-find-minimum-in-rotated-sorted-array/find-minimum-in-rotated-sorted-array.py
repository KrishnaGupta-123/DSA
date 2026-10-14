class Solution:
    def findMin(self, nums: list[int]) -> int:
        if nums[-1] > nums[0]:
            return nums[0]
        l = 0
        r = len(nums) - 1
        res = nums[l]
        while True:
            if l == r:
                res = nums[l]
                break
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return res