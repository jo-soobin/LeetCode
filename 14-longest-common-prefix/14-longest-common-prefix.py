class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lststr = [list(Str) for Str in strs]
        minstrlength = min([len(lst) for lst in lststr])
        
        answer = 0
        for position in range(minstrlength):
            samecount = 0
            for lst in lststr:
                if lststr[0][position] == lst[position]:
                    samecount +=1
                    
            if samecount == len(lststr):
                answer +=1
            else:
                break
                
        return ''.join(lststr[0][:answer])
    
        '''prefix=[]
        num = len(strs)
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix) '''