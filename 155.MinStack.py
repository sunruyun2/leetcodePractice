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
