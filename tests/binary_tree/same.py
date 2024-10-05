from collections import deque
from typing import Deque, List, Optional

from data_structures.binary_tree.binary_tree import BinTreeNode


def assertTreeIsSameAsArray(tree: Optional[BinTreeNode], arr: List[Optional[int]]):
    if tree is None:
        assert arr == [], f"tree is empty but {arr} is not"
        return

    currentLevel: Deque[Optional[BinTreeNode]] = deque()
    currentLevel.appendleft(tree)
    hasNextLevel = True
    i = 0
    while hasNextLevel:
        nextLevel: Deque[Optional[BinTreeNode]] = deque()
        emptyNextLevel = True
        while currentLevel:
            node = currentLevel.pop()
            assert i < len(arr), "not enough elements in array"
            if node:
                assert node.val == arr[i], f"expected {arr[i]}, but got {node.val}"
            else:
                assert arr[i] is None, f"expected None, but got {arr[i]}"

            i += 1
            if node:
                if node.left or node.right:
                    emptyNextLevel = False
                nextLevel.appendleft(node.left)
                nextLevel.appendleft(node.right)
        if emptyNextLevel:  # If all the nodes in the next level are None, stop
            hasNextLevel = False
        currentLevel = nextLevel
    assert i == len(arr), "too many elements in array"
