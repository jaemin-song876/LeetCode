class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs= {')':'(', '}':'{', ']':'['}
        brackets = []

        for char in s:
            if char not in pairs: #여는 괄호면
                brackets.append(char) #stack에 넣기
            elif not brackets or brackets[-1] != pairs[char]:
                #스택이 비었거나, 짝이 안 맞으면
                #brackets[-1],즉 스택에서 가장 최근에 쌓은 괄호가 pairs[char]이랑 다를때
                return False
            else:
                brackets.pop()#짝이 맞으면 꺼내기

        return len(brackets) == 0 #마지막에 스택이 비었는지 확인
