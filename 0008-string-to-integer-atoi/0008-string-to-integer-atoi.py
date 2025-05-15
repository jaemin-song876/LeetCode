class Solution:
    def myAtoi(self, s: str) -> int:

        #step1: remove whitespace
        i = 0
        n = len(s)
        num = 0

        while i<n and s[i]==' ':
            i += 1

        #step2: check signedness
        sign = 1
        if i < n and s[i] =='-':
            sign = -1
            i +=1
        elif i<n and s[i] =='+':
            i+=1

        #step3: extract num
        while i < n and s[i].isdigit():
            digit = int(s[i])
            num = num*10 + digit
            i += 1
        result = sign * num

        #step4: limit 32bit
        int_min = -2**31
        int_max = 2**31 -1

        if result < int_min:
            return int_min
        elif result > int_max:
            return int_max
        else:
            return result