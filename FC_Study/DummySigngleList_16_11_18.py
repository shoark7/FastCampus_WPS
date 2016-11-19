class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return self.value


class LinkedList:
    def __init__(self):
        self.head = Node()

        self.before = self.head
        self.current = self.head
        self.tail = self.head
        self.num_of_data = 0

    def __str__(self):
        return_list = []
        for i in range(self.num_of_data):
            return_list += self.search(i)
        return return_list


    def first(self):
        self.current = self.head.next
        self.before = self.head


    def add_new_entry(self, value=None):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.num_of_data += 1


    def next(self):
        self.current = self.current.next
        self.before = self.before.next
        return self.current.value


    def search(self, index):
        # 범위를 넘겼다면,
        if not isinstance(index, int):
            raise TypeError("Index must be an integer.")
        elif index > self.num_of_data:
            raise IndexError("Out of index..")
        elif index < 0:
            raise ValueError("INDEX must be over or equals to 0.")

        self.first()

        for _ in range(index):
            self.current = self.current.next
            self.before = self.before.next
        return self.current.value


