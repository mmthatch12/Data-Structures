from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If inserting we must already have a tree/root
        # if value is less than root value/self.value go left,

        # make a new tree/node if empty, otherwise keep going(recursion)
        if value >= self.value and self.right is None:
            self.right = BinarySearchTree(value)
        elif value >= self.value and self.right is not None:
            self.right.insert(value)
        elif value < self.value and self.left is None:
            self.left = BinarySearchTree(value)
        elif value < self.value and self.left is not None:
            self.left.insert(value)
        
    
        
        # if >= go right, make a new tree/node if empty otherwise keep going 

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if target == self.value, return it
        # otherwise go left or right based on smaller or bigger
        if target is self.value:
            return True
        elif target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        elif target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

        

    # Return the maximum value found in the tree
    def get_max(self):
        # always go right, if right exists, go right
        # otherwise return self.value
        if self.right is not None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # recursively
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

        #iteratively
        # stack = Stack()
        # stack.push(self)
        # while len(stack) >0:
        #     current_node = stack.pop()
        #     if current_node.right:
        #         stack.push(current_node.right)
        #     if current_node.left:
        #         stack.push(current_node.left)
        #     cb(current_node.value)

                

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # make a stack
        
        # add root to stack
        # while stack not empty then:
        # pop it out (DO THE THING!!! IE PRINT)
        # check left if exists add to stack, 
        # check right if exists add to stack
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Make a queue
        # put root in the queue
        # while queue is not empty
            # always pop out the thing at the top of the while loop
            # pop out front of que
            # (DO THE THING!!)
            # If left:
                # add left to back of queue
            # if right:
                # add right to back of queue
        pass


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
