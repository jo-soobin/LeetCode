class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # taget이 nums의 요소 일부를 더한 것과 같아지면 -> 해당 요소의 nums 인덱스 번호를 리스트 형태로 반환한다
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target == (nums[i]+nums[j]):
                    return [i,j]