class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #1. 띄어쓰기 단위로 단어들을 모두 list로 만든다
        #2. 문자가 아닌 특수문자 삭제
        #3. 단어를 count
        #4. banned 에 해당되는 단어 삭제
        #5. 가장 높은 count를 return
        paragraph = paragraph.replace(',', ' ')
        paragraph = paragraph.replace('  ', ' ')
        # 띄어쓰기를 기준으로 List로 변환
        words = paragraph.lower().split(' ')
        # 문자열이 아닌것들 모두 삭제
        wordList = []
        for s in words:
            wordList.append(''.join(filter(str.isalnum, s)))
        # ban에 포함되어있는 단어들 모두 pop 하여 삭제
        for ban in banned:
            while ban in wordList:
                wordList.pop(wordList.index(ban))
        # 가장 많이 count 된 문자열 return
        return max(wordList,key=wordList.count)