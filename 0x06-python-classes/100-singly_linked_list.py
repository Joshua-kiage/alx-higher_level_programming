#!/usr/bin/python3
"""
This module defines the Node and SinglyLinkedList classes.
"""


class Node:
    """
    Represents a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node): The reference to the next node. Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not a Node or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieves the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data stored in the node.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Retrieves the reference to the next node.

        Returns:
            Node: The reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the reference to the next node.

        Args:
            value (Node): The reference to the next node.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        __head (Node): The head node of the list.
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value of the new Node to be inserted.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the list.

        Returns:
            str: The string representation of the list.
        """
        node = self.__head
        output = ""
        while node is not None:
            output += str(node.data) + "\n"
            node = node.next_node
        return output.rstrip()
