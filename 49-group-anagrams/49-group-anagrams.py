class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 같은 anagrams에 해당하는 단어들은 정렬했을 경우 모두 똑같음
        Sorted = [ ''.join(sorted(str)) for str in strs]
        Sorted_unique = list(set(Sorted))
        # Sorted_unique 개수만큼 List가 존재함
        # List 만들어주기
        Answer = []
        for i in range(len(Sorted_unique)):
            Answer.append( [] )
        # sorted에 해당되는 Sorted_unqiue index를 찾아서,
        # 원본 (str[i])을 Answer의 리스트에 넣어줌
        for i in range(len(Sorted)):
            Answer[Sorted_unique.index(Sorted[i])].append( strs[i] )
        return Answer