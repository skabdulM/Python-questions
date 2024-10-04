
class MyStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        return self.stack.append(x)
        

    def pop(self):
        return self.stack.pop()
        

    def top(self):
        return self.stack[-1]
        

    def empty(self):
        return not self.stack

obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

