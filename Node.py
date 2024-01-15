"""
Binary Tree Node
----------

This class represents an individual Node in a Binary Tree. 

Each Node consists of the following properties:
    - left_child: Pointer to the left child of the Node
    - right_child: Pointer to the right child of the Node
    - parent: Pointer to the parent of the Node
    - weight: The weight of the Node
    - imbalance: The imbalance of the Node (absolute difference between the weight of the left and right subtree)

The class also supports the following functions:
    - add_left_child(Node): Adds the given Node as the left child
    - add_right_child(Node): Adds the given Node as the right child
    - is_external(): Returns True if the Node is a leaf node
    - update_weight(int): Updates the weight of the Node
    - get_left_child(): Returns the left child of the Node
    - get_right_child(): Returns the right child of the Node
    - get_imbalance(): Returns the imbalance of the Node

Your task is to complete the following functions which are marked by the TODO comment.
Note that your Node should automatically update the imbalance as nodes are added and weights are updated!
You are free to add properties and functions to the class as long as the given signatures remain identical
"""





from logging import root


class Node():
    # These are the defined properties as described above
    left_child: 'Node'
    right_child: 'Node'
    parent: 'Node'
    weight: int
    imbalance: int

    def __init__(self, weight: int) -> None:
        """
        The constructor for the Node class.
        :param weight: The weight of the node.
        """
        self.weight = weight
        self.imbalance = 0
        self.parent = None
        self.left_child = None
        self.right_child = None

        self.total_weight = weight

        # TODO Initialize the properties of the node

    def add_left_child(self, node: 'Node') -> None:
        """
        Adds the given node as the left child of the current node.
        Should do nothing if the the current node already has a left child.
        The given node is guaranteed to be new and not a child of any other node.
        :param node: The node to add as the left child.
        """
        if self.left_child is None and node is not None:
            node.parent = self
            self.left_child = node
            self.update_total_weight(self.left_child.total_weight)
            self.update_method()
            
        else:
            return 


        # TODO Add the given node as the left child of the current node

    def add_right_child(self, node: 'Node') -> None:
        """
        Adds the given node as the right child of the current node.
        Should do nothing if the the current node already has a right child.
        The given node is guaranteed to be new and not a child of any other node.
        :param node: The node to add as the right child.
        """
        if self.right_child is None and node is not None:
            self.right_child = node
            node.parent = self
            self.update_total_weight(self.right_child.total_weight)
            self.update_method()
            

        else:
            return

        # TODO Add the given node as the right child of the current node

    def is_external(self) -> bool:
        """
        Returns True if the node is a leaf node.
        :return: True if the node is a leaf node.
        """

        return self.left_child is None and self.right_child is None

    def update_weight(self, weight: int) -> None:
        """
        Updates the weight of the current node.
        :param weight: The new weight of the node.
        """
        self.update_total_weight(weight-self.weight)
        self.weight = weight
        self.update_method()
        

    def update_total_weight(self,total_weight):
        root=self
        while root is not None:
            root.total_weight+=total_weight
            root=root.parent


    def get_left_child(self) -> 'Node':
        """
        Returns the left child of the current node.
        :return: The left child of the current node.
        """

        return self.left_child

    def get_right_child(self) -> 'Node':
        """
        Returns the right child of the current node.
        :return: The right child of the current node.
        """

        return self.right_child

    def update_method(self):
        root = self
        while root is not None:
            left= root.left_child.total_weight if root.left_child is not None else 0
            right= root.right_child.total_weight if root.right_child is not None else 0
            root.imbalance=abs(left-right)

            root = root.parent


    def get_imbalance(self) -> int:
        """
        Returns the imbalance of the current node.
        :return: The imbalance of the current node.
        """
        return self.imbalance