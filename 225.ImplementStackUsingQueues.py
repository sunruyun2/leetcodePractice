class MyStack:

    def __init__(self):
        self.list = []

    def push(self, x: int) -> None:
        self.list.append(x)

    def pop(self) -> int:
        return self.list.pop()

    def top(self) -> int:
        return self.list[-1]

    def empty(self) -> bool:
        return len(self.list) == 0