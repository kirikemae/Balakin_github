class Stack:
    class Node:
        def __init__(self, value, nextNode):
            self.value = value
            self.nextNode = nextNode

    def __init__(self):
        self.top = None
        self._size = 0

    def isEmpty(self):
        return self.top is None

    def push(self, value):
        self._size += 1
        self.top = Stack.Node(value, self.top)

    def pop(self):
        if self.isEmpty():
            raise Exception
        val = self.top.value
        self.top = self.top.nextNode
        self._size -= 1
        return val

    def peek(self):
        return self.top.value

    def size(self):
        return self._size
