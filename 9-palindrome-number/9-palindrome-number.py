class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = str(x)
        return i[::-1] == i