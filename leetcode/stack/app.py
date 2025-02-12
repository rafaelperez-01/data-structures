class Stack:

    def __init__(self):
        self.top = []

    def push(self, value):
        self.top.append(value)

    def pop(self):
        if not self.top:
            return -1
        return self.top.pop()

    def peek(self):
        if not self.top:
            return -1
        return self.top[-1]
