class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # res = 0
        # for i in range(len(nums)):
        #     if nums[i] < target:
        #         res = i + 1
        # return res
        
        high = len(nums) - 1
        low = 0
        
        while low <= high:
            mid = (high + low) // 2
            
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return low