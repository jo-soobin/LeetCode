class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sumList = []
        Max=-1

        for i in range(len(accounts)):         
            sumA = 0
            for j in range(len(accounts[i])):
                sumA += accounts[i][j]
                if Max < sumA:
                    Max = sumA
        return Max