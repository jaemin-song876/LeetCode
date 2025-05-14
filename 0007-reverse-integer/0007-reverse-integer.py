class Solution:
    def reverse(self, x: int) -> int:

        #step1 remove the sign
        sign = -1 if x<0 else 1
        x = abs(x)

        #step2 reverse the number
        reversed_str = str(x)[::-1]
        reversed_x = int(reversed_str)


        #step4 add sign on the final number
        if reversed_x > 2**31 -1:
            return 0
        
        return sign*reversed_x
        