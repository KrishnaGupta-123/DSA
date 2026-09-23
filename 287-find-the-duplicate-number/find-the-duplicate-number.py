class Solution:
    def BS(self, nums: list[int], i:int, j:int, target:int) -> int:
        if i>j:
            return -1
        m = (i+j) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self.BS(nums,m+1,j,target)
        else:
            return self.BS(nums,i,m-1,target)


    def findDuplicate(self, nums: list[int]) -> int:
        nums.sort()
        m = len(nums)
        for i in range(m-1):
            idx = self.BS(nums,i + 1,m - 1,nums[i])
            if idx != -1:
                return nums[idx]
                