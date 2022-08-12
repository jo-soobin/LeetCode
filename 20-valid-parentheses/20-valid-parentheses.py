class Solution:
    def isValid(self, s: str) -> bool:
        inputlst = list(s)
        lst = []
        for i in inputlst:
            if i in ['(','{','[']:
                lst.append(i)
            else:
                if len(lst) ==0:
                    return False
                if lst[len(lst)-1] == '(' and i == ')':
                    lst.pop()
                elif lst[len(lst)-1] == '{' and i =='}':
                    lst.pop()
                elif lst[len(lst)-1] == '[' and i ==']':
                    lst.pop()
                else:
                    return False
            
        if len(lst)>0:
            return False
        return True