class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #1. 띄어쓰기 단위로 단어들을 모두 list로 만든다
        #2. 문자가 아닌 특수문자 삭제
        #3. 단어를 count
        #4. banned 에 해당되는 단어 삭제
        #5. 가장 높은 count를 return
        
        paragraph = paragraph.replace(',', ' ')
        paragraph = paragraph.replace('  ', ' ')

        words = paragraph.lower().split(' ')

        wordList = []
        for s in words:
            wordList.append(''.join(filter(str.isalnum, s)))
            
        for ban in banned:
            while ban in wordList:
                wordList.pop(wordList.index(ban))

        return max(wordList,key=wordList.count)