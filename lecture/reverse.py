class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def push(self, item):
        new_node = Node(item)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.size +=1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

list1 = LinkedList()
list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.push(5)
list1.printLL()
list1.reverse()
list1.printLL()



# def reverse(link):
#     v1 = link.head
#     v2 = link.head.next

#     link.tail = v1

#     while v2.next is not None:
#         temp = v2.next
#         v2.next = v1
#         v1 = v2
#         v2 = temp

#     link.head = v2

#     return link

# l2 = reverse(list1)
# cur = l2.head
# while cur.next is not None:
#     print(cur.value)

    
