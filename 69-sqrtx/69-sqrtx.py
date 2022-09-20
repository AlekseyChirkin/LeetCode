class Solution:
    def mySqrt(self, x: int) -> int:
        multi = 0
        res = 0
        
        if x == 0:
            return 0
        
        while (res < x):
            multi += 1
            res = multi * multi
        else:
            if res == x:
                return multi
            else:
                return multi - 1

        return multi