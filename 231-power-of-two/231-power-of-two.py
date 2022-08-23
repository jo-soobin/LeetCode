class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        answer = False
        lst = []
        
        for i in range(50):
            lst.append(pow(2,i))
        
        if n in lst:
            return True
        return False