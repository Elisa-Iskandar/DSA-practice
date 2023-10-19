class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        result = ''
        current_node = self.head
        while current_node:
            result += str(current_node.value)
            if current_node.next:
                result += '->'
            current_node = current_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.append(value)
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def insert(self, index, value):
        if index < 0 or index >= (self.length):
            return "index out of range"        
        elif self.length == 0 or index == 0:
            self.prepend(value)
        else:
            new_node = Node(value)
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
        self.length += 1
        return "Inserted"

    def traverse(self):
        current_node = self.head
        for i in range(self.length):
            print(current_node.value)
            current_node = current_node.next
            
    def search(self, key):
        current_node = self.head
        index = 0
        for i in range(self.length):
            if current_node.value == key:
                return "Found at index "+index
            current_node = current_node.next
            index += 1
        return "Not found"

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        else:
            current_node = self.head
            for i in range(index):
                current_node = current_node.next
            return current_node

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return "value set"
        return "value not set"
    
    def pop_first(self):
        popped = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped.next = None
        self.length -= 1
        return popped
    
    def pop(self):
        popped = self.tail
        temp = self.head
        if self.length == 0 or self.length == 1:
            self.pop_first()
        else:
            for i in range(self.length-2):
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.length -= 1
        return popped
    
    def remove(self, index):
        if index == 0:
            return self.pop_first() #pop first already minuses the length
        elif index < 0 or index > self.length-1:
            return "index out of range"
        else:
            previous_node = self.get(index-1)
            removed_node = previous_node.next
            previous_node.next = removed_node.next
            removed_node.next = None
            self.length -= 1
            return removed_node
        
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
                
#testing my methods :D
my_linked_list = LinkedList()
my_linked_list.append(20)
my_linked_list.append(30)
my_linked_list.append(40)
print(my_linked_list.length)
print(my_linked_list.__str__())
print("---------")
my_linked_list.prepend(10)
print(my_linked_list.length)
print(my_linked_list.__str__())
print("---------")
print(my_linked_list.insert(2,25)) 
print(my_linked_list.length)
print(my_linked_list.__str__())
print("---------")
print(my_linked_list.remove(2))
print(my_linked_list.length)
print(my_linked_list.__str__())
print("---------")
print(my_linked_list.search(20))
print("---------")
print(my_linked_list.get(0))
print("---------")
print(my_linked_list.set_value(0,15))
print(my_linked_list.__str__())
print("---------")
print(my_linked_list.pop_first())
print(my_linked_list.__str__())
print(my_linked_list.length)
print("---------")
print(my_linked_list.pop()) 
print(my_linked_list.__str__())
print(my_linked_list.length)

