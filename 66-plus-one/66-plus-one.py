class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        strings = ''.join(map(str, digits))
        
        #minNum = min(digits)
        result = int(strings)+1
        
        lst = map(int, str(result))
        return lst