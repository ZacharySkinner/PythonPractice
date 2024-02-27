#Stack: ArrayBased
class Stack:
    def __init__(self):
        self.items = []
    def push(self, x):
        self.items.append(x)
    def Pop(self):
        return self.items.pop()
    def top(self):
        return self.items[-1]
    def isEmpty(self):
        return self.size()==0
    def size(self):
        return len(self.items)

        

