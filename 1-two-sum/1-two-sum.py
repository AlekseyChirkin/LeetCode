class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        
        for i in range(len(nums)):
            hash_table[nums[i]] = i
        
        for j in range(len(nums)):
            checking_num = target - nums[j]
            if checking_num in hash_table and hash_table[checking_num] != j:
                return [j, hash_table[checking_num]]