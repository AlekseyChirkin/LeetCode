class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        sorted_s = [''] * len(s)
        
        for index, char in enumerate(s):
            sorted_s[indices[index]] = char
            
        return ''.join(sorted_s)