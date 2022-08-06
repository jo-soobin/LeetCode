class Solution:
    def firstUniqChar(self, s: str) -> int:
        answer = -1
        cnt_dict = Counter(list(s))
        i = 0
        
        for word in s:
            if cnt_dict[word] == 1:
                answer = i
                break
            i = i + 1
                
        return answer