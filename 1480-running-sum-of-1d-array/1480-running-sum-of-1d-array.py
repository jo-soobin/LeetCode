class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        sumList = []
        currentSum = 0
        
        for i in range(len(nums)):
            currentSum += nums[i]
            sumList.append(currentSum)
        return sumList