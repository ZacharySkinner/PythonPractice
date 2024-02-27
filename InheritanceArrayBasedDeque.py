#Deque: Inheriting from Arraybased Stack and Queue
from ArrayBasedStack import*
from ArrayBasedQueue import*
class Deque(Stack,Queue):
    def add_first(self,x):
        self.enqueue(x)
    def add_last(self,x):
        self.push(x)
    def delete_first(self):
        return self.dequeue
    def delete_last(self):
        return self.Pop()
    def last(self):
        return self.top()





