class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # words = s.strip().split(' ')
        # return len(words[-1])
        
        count = 0

        for ch in range(len(s) - 1, -1, -1):
            if s[ch] != ' ':
                count += 1 
            elif count != 0:
                break
                
        return count