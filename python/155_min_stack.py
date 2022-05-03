# https://leetcode.com/problems/min-stack/


class MinStack:
    def __init__(self):
        self.stack = []
        self.running_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.running_min:
            self.running_min.append(min(self.running_min[-1], val))
        else:
            self.running_min.append(val)

    def pop(self) -> None:
        self.running_min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.running_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
