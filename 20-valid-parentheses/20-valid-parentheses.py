class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        dict = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        
        stack = []
        
        for i in range(len(s)):
            if s[i] in dict.values():
                stack.append(s[i])
            elif s[i] in dict.keys():
                if stack == [] or dict[s[i]] != stack.pop():
                    return False
        if stack: return False
                
        return True
    