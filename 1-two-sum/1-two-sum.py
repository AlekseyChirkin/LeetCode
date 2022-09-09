class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in nums:
            for n2 in range(nums.index(n) + 1, len(nums)):
                if (n + nums[n2]) == target:
                    return [nums.index(n), n2]