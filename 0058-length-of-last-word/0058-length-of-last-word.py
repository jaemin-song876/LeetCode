class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.strip().split()
        #문자열 양쪽 끝의 공백 제거하고, 공백기준으로 단어들을 리스트로 분리

        if not words:
            return 0 #빈 문자열인 경우 0반환
        
        return len(words[-1])