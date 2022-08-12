class MyStack:

    def __init__(self):
        self.lst = [] 

    def push(self, x: int) -> None:
        self.lst.append(x)

    def pop(self) -> int:
        return self.lst.pop(-1)
        
    def top(self) -> int:
        return self.lst[-1]

    def empty(self) -> bool:
        if len(self.lst) == 0:
            return True
        else:
            return False
