class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

class Queue2Stacks:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self,element):
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if len(self.stack2) == 0 :
            return "The Queue it's empty"
        return self.stack2.pop()
