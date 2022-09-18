class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # if target in nums:
        #     return nums.index(target)
        # else:
            res = 0
            for i in range(len(nums)):
                if nums[i] < target:
                    res = i + 1
            return res
                