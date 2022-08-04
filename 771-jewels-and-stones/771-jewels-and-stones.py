class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        jewelsList=list(jewels)
        stoneList=list(stones)        
        result=0
        counts = collections.Counter(stoneList)
        for key, value in counts.items():
            if key in jewelsList:
                result+= value
        
        return result
        
        ''' #풀이법2
        jewelsList=list(jewels)
        stoneList=list(stones)
        
        count=0
        for stone in stoneList:
            if stone in jewelsList:
                count+=1
        
        return count'''