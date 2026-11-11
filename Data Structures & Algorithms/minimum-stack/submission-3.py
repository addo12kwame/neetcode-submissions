class MinStack:

    def __init__(self):
        self.stack = []
        self.min = [9999999999]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min.append(min(val, self.min[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()
        

    def top(self) -> int:
        # print("top", self.stack[-1])
        return self.stack[-1]
        

    def getMin(self) -> int:
        mins = self.min[-1]
        return mins
        
