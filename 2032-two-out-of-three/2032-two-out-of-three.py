class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # Step1: num1, num2, num3에서 중복을 제거한다.
        # python list delete duplicate
        # Step2: num1+num2+num3 를 합쳐서 하나의 list로 만든다.
        # python concatenate lists to one list
        # Step3: 하나의 list가 된 데이터에서 count를 하여,
        # 2개 이상인 숫자들만 list 형태로 return 한다.
        # python counter in list Collections.Counter
    
        #set() 은 집합을 나타냄 -> 중복 제거
        lst = list(set(nums1))+list(set(nums2))+list(set(nums3))
        
        count = collections.Counter(lst)
        
        answer=[]
        for key, value in count.items():
            if value>=2:
                answer.append(key)
        return answer