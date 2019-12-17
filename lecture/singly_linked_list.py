class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    #create new node to increment
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def printMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head.next
        if self.head is not None:
            while (fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                # print('fast_ptr', fast_ptr.data)
                slow_ptr = slow_ptr.next
                # print('slow_ptr', slow_ptr.data)
            print('thd middle element is: ', slow_ptr.data)
        print('slow_ptr', slow_ptr.data)
        
list1 = LinkedList() 
list1.push(11)
list1.push(10)
list1.push(9)
list1.push(8)
list1.push(7)
list1.push(6)
list1.push(5) 
list1.push(4) 
list1.push(2) 
list1.push(3) 
list1.push(1) 
list1.printMiddle()

