class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_from_center(left, right) -> str:

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""

        for i in range(len(s)):
            #odd
            pal1 = expand_from_center(i,i)

            #even
            pal2 = expand_from_center(i, i+1)

            longer_pal = pal1 if len(pal1) > len(pal2) else pal2

            if len(longer_pal) > len(longest):
                longest = longer_pal
                
        return longest

