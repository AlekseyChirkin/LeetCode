class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numbers_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        arabic_number = 0
        
        for i in range(len(s)-1):
            if roman_numbers_dict[s[i]] < roman_numbers_dict[s[i + 1]]:
                arabic_number -= roman_numbers_dict[s[i]]
            else:
                arabic_number += roman_numbers_dict[s[i]] 

        return arabic_number + roman_numbers_dict[s[-1]]