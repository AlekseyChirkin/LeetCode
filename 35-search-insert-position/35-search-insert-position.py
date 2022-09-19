class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] < target:
                res = i + 1
        return res
        
#         low = 0
#         high = len(nums) - 1
#         res = -1
                
#         if target <= nums[0]:
#             res = 0
#         if target > nums[high]:
#             res = high + 1
            
#         while low <= high:
#             mid = low + (high - low) // 2
            
#             if nums[mid] == target:
#                 res = mid
#                 break

#             if nums[mid] < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
        
#         return res
        