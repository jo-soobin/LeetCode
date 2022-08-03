class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        answer = ""
        #palindrome_list = [a for a in words if a == a[::-1]]
        lst=[]
        for a in words:
            if a == a[::-1]:
                lst.append(a)
                
        if len(lst) != 0:
            answer = lst[0]
            
        return answer