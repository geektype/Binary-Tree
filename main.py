class Node:
    """ Class representing a sing node in a binary tree 

    Attributes
    ----------
    value : int
        The integer value of the Node itself
    right_pointer : obj
        An instance of a node object which is to the "right" of the node
    left_pointer : obj
        An instance of a node object which is to the "left" of the node

    
    Methods
    -------
    addLeft(node)
        Adds a node object to the node left pointer.
        return True if successful
    
    addRight(node)
        Adds a node object to the node right pointer.
        return True if successful
    
    rightPointer(node)
        Returns object stored in right pointer attribute
    
    leftPointer(node)
        Returns object stored in left pointer attribute    

    """


    def __init__(self, value = 0, left_pointer=None, right_pointer=None):
        """
        Parameters
        ----------
        value : int
            The integer value of the Node itself
        right_pointer : obj, optional
            An instance of a node object which is to the "right" of the node.
            Default: None
        left_pointer : obj, optional
            An instance of a node object which is to the "left" of the node
            Default: None

        """
        self.left_pointer = left_pointer
        self.right_pointer = right_pointer
        self.value = value
    
    def addLeft(self, node):
        """Adds a node object to the node left pointer. 

        Parameters
        ----------
        node : obj 
            instance of Node() to be stored in the left pointer of current Node
        
        Return
        ------
        True if successful
        """

        self.left_pointer = node
        return True

    def addRight(self, node):
        """Adds a node object to the node right pointer. 

        Parameters
        ----------
        node : obj 
            instance of Node() to be stored in the right pointer of current Node
        
        Return
        ------
        True if successful
        """
        self.right_pointer = node
        return True
    
    def rightPointer(self):
        """Returns object at right pointer

        Parameters
        ----------
        None
        
        Return
        ------
        right_pointer : obj
            value of the instance right pointer
        """
        return self.right_pointer
    
    def leftPointer(self):
        """Returns object at left pointer 

        Parameters
        ----------
        None
        
        Return
        ------
        left_pointer : obj
            value of the instance lefts pointer
        """
        return self.left_pointer
    def nodeValue(self):
        """ Returns value of the node
        Parameters
        ----------
        None
        
        Return
        ------
        value : obj
            value of the node
        """
        return self.value

    def __str__(self):
        return str(self.nodeValue())


class Tree:
    """Class representing a binary tree consisting of nodes

    Attributes
    ----------
    root : obj => Node()
        The root Node of the tree
        Default: None
    size_limit : int
        Number of maximum allowed Nodes in the tree (inclusive)
    size : int
        Current number of nodes in the tree

    Methods
    -------
    add(value)
        Adds a Node with the given value to the tree. Follows the pointers starting from the root node and adds to leaf.
        Returns False if adding a Node will exceed the size limit.

    """

    def __init__(self, size):
        self.root = None
        self.size_limit = size
        self.size = 0
    
    def add(self, value):
        if self.root == None:
            self.root = Node(value)
            return True
        elif self.size + 1 < self.size_limit:
            add_node = Node(value)
            current_node = self.root

            while current_node != None:
                previous_node = current_node


                if value > current_node.nodeValue():
                    current_node = current_node.rightPointer()
                else:
                    current_node = current_node.leftPointer()
            if value > previous_node.nodeValue():
                previous_node.addRight(add_node)
                self.size+=1
            else:
                previous_node.addLeft(add_node)
                self.size+=1
            return True
        else:
            return False
    
tree = Tree(10)
elements = [10,3,8,1,39,8,3,6,3,19,18]
for element in elements:
    if not tree.add(element):
        print("Size limit Exeeded. Did not add", element)

print(tree.root)