class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        digits = []
        temp = x
        
        while temp > 0:
            digits.append(temp % 10)
            temp = temp // 10
        
        reversed_x = 0

        for d in digits:
            reversed_x = reversed_x * 10 + d

        return reversed_x == x