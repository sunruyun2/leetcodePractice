# 1. intuition - use another variable to store the min value
# not very efficient cause we have to recalculate min if we did the pop
from cmath import inf

class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.min = inf

    def push(self, val:int):
        self.stack.append(val)
        if self.min > val:
            self.min = val

    def pop(self):
        self.stack.pop()
        if not self.stack:
            self.min = inf
        else:
            self.min = min (self.stack)

    def top(self):
        return self.stack[-1]

    def getMin(self)->int:
        return self.min


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_1 = obj.top()
obj.pop()
print(param_1)

# 2.use min stack
class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.minStack = [] 

    def push(self, val:int):
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self)->int:
        return self.minStack[-1]



