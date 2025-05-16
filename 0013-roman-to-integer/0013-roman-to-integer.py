class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,
        'M':1000}

        result = 0

        for i in range(len(s)):
            # 앞 문자가 뒷 문자보다 작으면 빼야함!!!
            if i<len(s) -1 and roman[s[i]] < roman[s[i+1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]

        return result