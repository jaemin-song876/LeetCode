class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right=0, len(s) -1
        #문자 양끝에서 포인터 시작 
        while left<right:
            # 왼쪽 문자 스킵
            while left< right and not s[left].isalnum():
                left += 1
            #오른쪽 문자 스킵
            while left<right and not s[right].isalnum():
                right -=1
            # 소문자로 바꿔서 비교
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        return True