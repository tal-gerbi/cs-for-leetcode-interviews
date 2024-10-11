from typing import Optional


class LinkedListNode:
    def __init__(self, val: int, next: Optional['LinkedListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        if self.next:
            return f"[{self.val} {self.next}]"
        return f"[{self.val}]"
