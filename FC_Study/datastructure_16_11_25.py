class Node:
    def __init__(self, data=None):
        self.next = None
        self.data = data

    def __str__(self):
        return self.data


class MyStack:

    def __init__(self, name=None):
        self.name = name
        self.head = None

    def __str__(self):
        return self.name

    def is_empty(self):
        return True if self.head is None else False

    def pop(self):
        if self.is_empty():
            raise IndexError('OUT OF INDEX')
        else:
            result = self.head.data
            self.head = self.head.next
            return result

    def push(self, data=None):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def peek(self):
        return self.head.data


class MyQueue:

    def __init__(self, name=None):
        self.name = name
        self.tail = None
        self.head = None

    def enqueue(self, data=None):
        new_node = Node(data=data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):

        if self.is_empty():
            raise IndexError('자료가 더 이상 없습니다.')

        else:
            result = self.head.data
            self.head = self.head.next
            return result

    def is_empty(self):
        return True if self.head is None else False

    def peek(self):
        return self.head.data

