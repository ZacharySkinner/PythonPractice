#Queu: ArrayBased
#from ArraryBasedStack import*
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,x):
        self.items.append(x)
    def dequeue(self):
        return self.items.pop(0)
    def first(self):
        return(self.items[0])
    def isEmpty(self):
        return self.size()==0
    def size(self):
        return len(self.items)
    
    

