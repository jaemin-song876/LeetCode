class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, "M"), (900,"CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5,"V"), (4,"IV"), (1, "I")
        ] #bigger value first

        result =[]
        for values, symbol in values:
            while num >= values:
                result.append(symbol)
                num -= values
        return ''.join(result)
"""
''.join(['L', 'V', 'I', 'I', 'I'])  
→ "LVIII" 하려고 ''.join(result) 하는 것임
빈 문자열''을 기준으로 리스트 안에 있는 문자열을 전부 하나로 이어붙이라는 뜻
"""
