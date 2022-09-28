class Solution:
    def multiply(self, num1: str, num2: str) -> str:
    
        def str_to_int(num: str) -> int:
            multiplier = 1
            digit = 0

            for i in range(len(num) - 1, -1, -1):
                digit += (ord(num[i]) - 48) * multiplier
                multiplier *= 10
            return digit
    
        x = str_to_int(num1)
        y = str_to_int(num2)
        
        return str(x * y)
