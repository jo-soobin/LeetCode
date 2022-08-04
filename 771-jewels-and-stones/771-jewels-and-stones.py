class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsList=list(jewels)
        stoneList=list(stones)
        
        count=0
        for stone in stoneList:
            if stone in jewelsList:
                count+=1
        
        return count