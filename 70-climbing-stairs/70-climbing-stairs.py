class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2: return n

        st1 = 1
        st2 = 1
        
        
        k = 0
        
        while (k <= (n-2)):
            sum_ = st1 + st2
            st1 = st2
            st2 = sum_
            k += 1
        
        return st2