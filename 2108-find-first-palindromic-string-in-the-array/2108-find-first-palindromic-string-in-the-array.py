class Solution:
    def checkPalindrome(self, s: str) -> bool:

        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        reverse = s[::-1]
        
        return s == reverse
    
    def firstPalindrome(self, words: List[str]) -> str:
        
        for s in words:
            if self.checkPalindrome(s):
                return s
            
        return ''
    
        '''
        answer = ""
       
        lst=[]  #palindrome_list = [a for a in words if a == a[::-1]]
        for a in words:
            if a == a[::-1]:
                lst.append(a)
                
        if len(lst) != 0:
            answer = lst[0]
            
        return answer
        '''