class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []

        res = nums
        res.extend(nums)
        
        return res