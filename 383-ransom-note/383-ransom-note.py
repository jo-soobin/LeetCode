class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ranlist = list(ransomNote)
        maglist = list(magazine)
        answer = True
        
        for i in ranlist:
            if i not in maglist:
                answer = False
                break
            
            else:
                cha = maglist.index(i)
                maglist.pop(cha)
                
        return answer