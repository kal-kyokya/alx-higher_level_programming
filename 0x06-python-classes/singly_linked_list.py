#!/usr/bin/python3
"""No modules, therefore, no module descriptions."""


class Node:
    """Enables manipulation of a node.

    Attributes:
        data: Value stored in the node.
        next_node: Pointer to the next_node.
    """
    def __init__(self, user_data, next_node=None):
        """Constructs and initializes the 'Node' object.

        Args:
            user_data: Value passed in by user.
            next_node: Pointer to the subsequent node.
        """
        self.__data = user_data
        self.__next_node = next_node

    @property
    def data(self):
        """The def below is the GETTER METHOD for the data of our Node object.

        The SETTER METHOD comes right after.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """The def below is the GETTER METHOD for next_node of our Node object.

        The SETTER METHOD comes right after.
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if (value is not None or (not isinstance(value, Node))):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Enables creation of a linked list.

    Attributes:
        head: Pointer to the beginning of the linked list.
    """
    def __init__(self):
        """Enables construction and initialization for class' instance"""
        self.__head = None

    def sorted_insert(self, value):
        """Method use to add a Node instance to the Linked list.

        Arg:
            value: Integer value stored inside the node.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new

    def __str__(self):
        """Generates the output of this class' objects
        for any call converting it to string such as 'print(objt)'

        Arg:
            None.

        Return:
            The replacement of the object's name.
        """
        values = []
        current = self.__head
        while current is not None:
            value.append(str(current.data))
            current = current.next_node
        return ("\n".join(values))
