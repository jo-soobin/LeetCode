class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        reverse = s[::-1]
        return s == reverse
        '''
        i, j = 0, len(s)-1
        Answer = True
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                Answer = False
               
        return Answer
        #s에 포함된 모든 글자만 남긴다(글자 빼고 다 삭제)
        #모든 문자를 소문자/대문자로 바꾼다
        #문자열을 뒤집어서 새로운 변수에 할당
        # 문자열 뒤집기 전후 같은 지 확인 후 return
        ''' 
        