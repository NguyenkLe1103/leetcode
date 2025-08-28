class Solution:
    def isPalindrome(self, x: int) -> bool:
        org = x
        rev = 0
        if (x < 0):
            return False
        else:
            while x > 0:
                digit = x % 10
                rev = rev * 10 + digit
                x //= 10 
            return org == rev
        
        