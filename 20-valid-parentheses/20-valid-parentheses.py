class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        brackets = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []
        for ch in s:
            if ch in brackets.values():
                stack.append(ch)
            elif ch in brackets.keys():
                if stack == [] or brackets[ch] != stack.pop():
                    return False
        
        if len(stack): return False
                    
        return True