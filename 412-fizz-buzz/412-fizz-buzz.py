class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        lst = []
        for i in range(1,n+1):
            if i%15 == 0:
                lst.append('FizzBuzz')
            elif i%5 == 0:
                lst.append('Buzz')
            elif i%3 == 0:
                lst.append('Fizz')
            else:
                lst.append(f'{i}')
        return lst
            