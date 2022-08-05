class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
        
        # enumerate 풀이방법
        pairs = [target - num for num in nums] # nums = [2,7,11,15] -> pairs = [7,2,-2,-6]
        
        for i , pair in enumerate(pairs): #pairs의 각각의 key와 value -> (0,7),(1,2),(2,-2),(3,-6)
            
            if pair in nums and i != nums.index(pair): #pair가 nums의 요소이고, key값이 nums에서 pair의 인덱스값과                                                                      다르면
                return [i, nums.index(pair)]
        

        
        '''
        2중 for문 풀이
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target == (nums[i]+nums[j]):
                    return [i,j]
        '''