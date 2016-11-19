"""
Linked list by Python!!

16/11/18
"""


class Node:
    """
    Item for a linked list of specific index.
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value


class LinkedList:
    def __init__(self):
        """
        We're implementing a dummy single list. So we initialize list with a dummy node.
        """
        self.head = Node()
        self.before = self.head
        self.current = self.head
        self.tail = self.head
        self._num_of_data = 0


    def __str__(self):
        return_list = []
        for i in range(self._num_of_data):
            return_list += str(self.search_entry(i))
        return ', '.join(return_list)


    def __getitem__(self, index):
        return self.search_entry(index)


    def __len__(self):
        return self._num_of_data


    def first(self):
        """
        Reset current and before node for search_entry and delete_entry.
        :return: None
        """
        self.current = self.head.next
        self.before = self.head


    def add_new_entry(self, value=None):
        """
        Add a new entry to the last element of the list.
        :param value: Value of the new node
        :return: None
        """
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self._num_of_data += 1


    def next(self):
        """
        Get the next node's value from current position.
        Move the current cursor to next one.
        :return: Next node's value.
        """
        self.first()
        self.current = self.current.next
        self.before = self.before.next
        return self.current.value


    def search_entry(self, index):
        """
        Search node by index. Like others, first one's index is 0.
        :index: Index you want
        :return: Value of Node of the index
        """
        # 범위를 넘겼다면,
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        elif index > self._num_of_data:
            raise IndexError("Out of index..")
        elif index < 0:
            raise ValueError("INDEX must be over or equals to 0.")

        self.first()

        for _ in range(index):
            self.current = self.current.next
            self.before = self.before.next
        return self.current.value


    def delete_entry(self, index):
        """
        Delete node by index.
        :param index: Node's index you want
        :return: None
        """

        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        elif index >= self._num_of_data:
            raise IndexError("Out of index..")
        elif index < 0:
            raise ValueError("INDEX must be over or equals to 0.")

        self.first()

        for _ in range(index):
            self.current = self.current.next
            self.before = self.before.next

        self.before.next = self.current.next
        del(self.current)
        self.current = self.before.next
        self._num_of_data -= 1


