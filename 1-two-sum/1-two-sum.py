class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
               
        # Two-pointer 풀이방법
        nums_sorted = sorted(nums)
        i, j = 0 , len(nums)-1
        while i<j:
            left = nums_sorted[i]
            right = nums_sorted[j]
            diff = left+right-target
            
            if diff <0:
                i+=1
            elif diff>0:
                j-=1
            else:
                break
        
        if left != right:
            return nums.index(left), nums.index(right)
        else:
            return [i for i, num in enumerate(nums) if num==left]

        '''
        # hash table 풀이방법
        hashtable = dict()
        for i, value in enumerate(nums): #(0,2),(1,7),(2,11),(3,15)
            hashtable[value] = i #hashtable[2] = 0, hashtable[7] = 1, hashtable[11] = 2, hashtable[15] = 3
            
        pairs = [target-num for num in nums] #pairs = [7,2,-2,-6]
        
        for i, pair in enumerate(pairs): #(0,7),(1,2),(2,-2),(3,-6)
            if pair in hashtable and i != hashtable[pair]: # 7,2,-2,-6 in hashtable and                                                                                          0,1,2,3 != hashtable[7.2.-2.-6]
                return [i, hashtable[pair]]
        '''
        
        '''
        # enumerate 풀이방법
        pairs = [target - num for num in nums] # nums = [2,7,11,15] -> pairs = [7,2,-2,-6]
        
        for i , pair in enumerate(pairs): #pairs의 각각의 key와 value -> (0,7),(1,2),(2,-2),(3,-6)
            
            if pair in nums and i != nums.index(pair): #pair가 nums의 요소이고, key값이 nums에서 pair의 인덱스값과                                                                      다르면
                return [i, nums.index(pair)]
        '''

        
        '''
        2중 for문 풀이
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target == (nums[i]+nums[j]):
                    return [i,j]
        '''