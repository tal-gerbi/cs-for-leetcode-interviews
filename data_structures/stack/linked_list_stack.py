from data_structures.linked_list.linked_list import LinkedListNode


class LinkedListStack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return not self.head

    def peek(self):
        if self.isEmpty():
            raise Exception("stack is empty")
        return self.head.val

    def pop(self):
        if self.isEmpty():
            raise Exception("stack is empty")
        val = self.head.val
        self.head = self.head.next
        return val

    def push(self, val: int):
        new_node = LinkedListNode(val)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def __repr__(self):
        return repr(self.head)


def test_stack():
    s = LinkedListStack()
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
