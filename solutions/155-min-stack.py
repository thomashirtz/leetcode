class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append([x, x])
        else:
            minimum = min(x, self.getMin())
            self.stack.append([x, minimum])

    def pop(self):
        return self.stack.pop()[0]

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]