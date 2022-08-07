class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        dec = False
        if x < 0:
            return dec
        else:
            original=x
            reverse=0
            while x:
                remainder=x%10
                x=x//10
                reverse=reverse*10+remainder

            if reverse == original:            
                dec=True
            else:
                dec=False
        
        return dec