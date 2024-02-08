class MinStack:

    def __init__(self):
        self.top_value = -1
        self.initial = 1000
        self.stack = [(-1, -1)] * self.initial
        self.min_map = {}

    def push(self, val: int) -> None:
        self.top_value += 1
        if self.top_value == 0:
            self.stack[self.top_value] = val, val
        else:
            if self.top_value == self.initial:
                ext_stack = [(-1, -1)] * 1000
                self.initial += 1000
                self.stack.extend(ext_stack)
                min_value = min(self.stack[self.top_value - 1][1], val)
                self.stack[self.top_value] = val, min_value
            else:
                min_value = min(self.stack[self.top_value - 1][1], val)
                self.stack[self.top_value] = val, min_value

    def pop(self) -> None:
        if self.top_value != -1:
            self.top_value -= 1

    def top(self) -> int:
        if self.top_value != -1:
            return self.stack[self.top_value][0]

    def getMin(self) -> int:
        if self.top_value != -1:
            return self.stack[self.top_value][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()