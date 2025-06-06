class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s=[]
        carry =0
        i=len(a)-1
        j=len(b)-1

        while i>=0 or j>= 0 or carry:
            if i>=0:
                carry += int(a[i]) #a의 i번째수를 정수로 바꾸고 carry에 더하기
                i -= 1

            if j>=0:
                carry += int(b[j])
                j -= 1
            
            s.append(str(carry % 2))

            carry //= 2 #몫만 carry에 다시 저장
        
        return ''.join(reversed(s))
        