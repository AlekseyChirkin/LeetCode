class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # res = 0
        # for i in range(len(nums)):
        #     if nums[i] < target:
        #         res = i + 1
        # return res
        l , r = 0, len(nums)-1
        while l <= r:
            mid=(l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return l