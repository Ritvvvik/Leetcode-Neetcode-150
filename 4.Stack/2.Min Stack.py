#Design problem to build a stack from scratch
class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)  #push into 1st stack
        val = min(val,self.minstack[-1] if self.minstack else val) #updating value for 2nd stack
        self.minstack.append(val) #push to second stack

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]