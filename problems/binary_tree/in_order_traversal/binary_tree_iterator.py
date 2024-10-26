from abc import ABC, abstractmethod

from data_structures.binary_tree.binary_tree import TreeNode
from data_structures.stack.linked_list_stack import LinkedListStack
from tests.binary_tree.construct import construct


class Solution(ABC):
    """
        - Title: Binary Search Tree Iterator
        - Available at: https://leetcode.com/problems/binary-search-tree-iterator/
        - Why was this chosen:
            Implementing the in-order traversal iteratively helps to understand it better
    """
    @abstractmethod
    def hasNext(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> int:
        pass


class StackBinaryTreeIterator(Solution):
    """
    Approach:
        1. Keep a stack with (node, recursive), where:
            - recursive = True, if the node should be processed recursively
            - recursive = False, if the node itself should be processed
        2. Since we want the left subtree to be processed first, push the left subtree last
        3. When recursive is False, return the element's value

    Complexity:
        Time Complexity: O(n)
        Space Complexity: O(h)
    """
    def __init__(self, root: TreeNode):
        self.stack = LinkedListStack()
        self.stack.push((root, True))

    def hasNext(self) -> bool:
        return not self.stack.isEmpty()

    def next(self) -> int:
        elem, recursive = self.stack.pop()
        while recursive:
            if elem.right:
                self.stack.push((elem.right, True))
            self.stack.push((elem, False))
            if elem.left:
                self.stack.push((elem.left, True))
            elem, recursive = self.stack.pop()
        return elem.val


def test_example():
    root = construct([7, 3, 15, None, None, 9, 20])
    iterator = StackBinaryTreeIterator(root)
    assert iterator.next() == 3
    assert iterator.next() == 7
    assert iterator.hasNext()
    assert iterator.next() == 9
    assert iterator.hasNext()
    assert iterator.next() == 15
    assert iterator.hasNext()
    assert iterator.next() == 20
    assert not iterator.hasNext()
