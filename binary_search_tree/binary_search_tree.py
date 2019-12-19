# from dll_queue import Queue
# from dll_stack import Stack


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
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
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
