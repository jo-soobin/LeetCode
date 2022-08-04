class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        First = [i for i, digit in enumerate(digits) if digit != 0]
        Second = list(range(0, len(digits)))
        Last = [i for i, digit in enumerate(digits) if digit %2 == 0]
        Answer = set()
        for i in First:
            for j in Second:
                for k in Last:
                    if i != j and i != k and j != k:
                        Answer.add(digits[i]*100 + digits[j]*10 + digits[k])
        Answer = list(Answer)
        Answer.sort()
        return Answer