from collections import deque
from typing import List, Optional

from data_structures.binary_tree.binary_tree import BinTreeNode


def assertTreeIsSameAsArray(tree: Optional[BinTreeNode], arr: List[Optional[int]]):
    if tree is None:
        assert arr == [], f"tree is empty but {arr} is not"
        return

    current_level = deque()
    current_level.appendleft(tree)
    has_next_level = True
    i = 0
    while has_next_level:
        next_level = deque()
        empty_next_level = True
        while current_level:
            node = current_level.pop()
            assert i < len(arr), "not enough elements in array"
            if node:
                assert node.val == arr[i], f"expected {arr[i]}, but got {node.val}"
            else:
                assert arr[i] is None, f"expected None, but got {arr[i]}"

            i += 1
            if node:
                if node.left or node.right:
                    empty_next_level = False
                next_level.appendleft(node.left)
                next_level.appendleft(node.right)
        if empty_next_level:
            has_next_level = False
        current_level = next_level
    assert i == len(arr), "too many elements in array"
