class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five= 0
        ten = 0
        
        for cost in bills:
            if cost == 5:
                five+=1
            elif cost == 10:
                five, ten = five-1, ten+1
            elif ten>0:
                five, ten = five-1, ten-1
            else:
                five -= 3
                
            if five <0:
                return False
        return True