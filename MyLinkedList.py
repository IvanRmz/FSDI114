class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DLNode:
    def __init__(self, data):
      self.prev = None
      super().__init__(data)

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data, prev_node=None, position=None):
        
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return True

        if prev_node:
            temp = prev_node.next
            prev_node.next = new_node
            new_node.next = temp
            return True

        if position:
            last  = self.find_index(index=position)
            if last == self.head:
                last.next = self.head
                self.head = last
                return True
            return self.add(data, prev_node=last)
        
        last = self.find_index()
        last.next = new_node
        return True

    def find_index(self, index=None):
        last = self.head
        counter = 0
        while last.next:
            last = last.next
            if counter == index:
                break
            counter += 1
        return last

    def removeNode(self, data=None, position=None, prev_node=None):
        
        if not self.head or (not data and not position and not prev_node):
            return False
        
        last = self.head

        if prev_node:
            temp = prev_node.next
            next_node = temp.next
            prev_node = next_node
            return True

        if data:
            if last.data == data:   
                last = last.next
                return True
            
            while last.next and last.next.data != data:
                last = last.next
            if last.next and last.next.data == data:
                last.next = last.next.next
                return True
            else:
                return False
        
        if position:
            counter = 0
            while last.next and counter < position-1:
                last = last.next
                counter+=1
            
            if last.next and counter == position-1:
                last.next = last.next.next
                return True
            
        return False


    def printLinkedList(self):
        print("List")
        list = ''
        temp = self.head
        while temp.next:
            list += f'{temp.data} -> '
            temp = temp.next
        list += f'{temp.data}'
        print(list)


class DLList:

    def __init__(self):
      self.head = None  
      self.tail = None

    def add(self, data):
        new_node = DLNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return True
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        return True

    def insert_after(self, prev_node, data):
        new_node = DLNode(data)
        temp = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if temp:
            new_node.next = temp
            temp.prev = new_node
        if not temp:
            self.tail = new_node
        return True

    def remove(self, data):
        if not self.head:
            return False
        node = self.head

        while node.next and node.data != data:
            node = node.next
        
        if node.data == data:
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node
            if next_node:
                next_node.prev = prev_node
            if not next_node:
                self.tail = prev_node
            return True

        return False
        


    def printDLL(self):
        print("DLL")
        list = ''
        temp = self.head
        while temp.next:
            list += f'{temp.data} <-> '
            temp = temp.next
        list += f'{temp.data}'
        print(list)