from collections import deque

class MyQueue(object):

    def __init__(self):
        self.q = deque()
        

    def push(self, x):
        return self.q.append(x)

        

    def pop(self):
        return self.q.popleft()

        

    def peek(self):
        return self.q[0]
        

    def empty(self):
        return len(self.q) == 0
        


obj = MyQueue()
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()