class Stack:
    """
    Stack implementation as a list.
    """

    def __init__(self):
        """
        Creates new stack
        """

        self.__item = []

    def is_empty(self):
        """
        Check if the stack is empty.
        :return: bool
        """

        return not bool(self.__item)

    def push(self, item):
        """
        Adds new items to the stack
        :param item: item to add to the stack
        :return: Nothing
        """
        self.__item.append(item)

    def pop(self):
        """
        Removes the top item from the stack
        :return: the item that has been removed
        """
        return self.__item.pop()

    def peek(self):
        """
        Returns the top item from the stack
        :return: Nothing
        """
        return self.__item[-1]

    def size(self):
        """
        Get the number of items in the stack
        :return: the number of items in the stack
        """
        return len(self.__item)