from abc import ABC, abstractmethod
from typing import Dict, Optional

from data_structures.binary_tree.binary_tree import BinTreeNode
from tests.binary_tree.construct import construct


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(ABC):
    """
        - Title: Populating Next Right Pointers in Each Node II
        - Available at: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
        - Why was this chosen:
            A variation of the pre-order traversal, where the right subtree is processed first
    """

    @abstractmethod
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        pass


class ModifiedPreOrderTraversalSolution(Solution):
    """
    Approach:
        1. Scan in the modified pre-order traversal (right subtree first)
        2. Keep a mapping from heights to the next right nodes

    Complexity:
        Time Complexity: O(n)
        Space Complexity: O(h)
    """
    def _connect(self, root: Optional[Node], height: int, next_nodes: Dict[int, Node]):
        if root is None:
            return

        if height in next_nodes:
            root.next = next_nodes[height]
        next_nodes[height] = root

        self._connect(root.right, height + 1, next_nodes)
        self._connect(root.left, height + 1, next_nodes)

    def connect(self, root: Optional[Node]) -> Optional[Node]:
        self._connect(root, 0, {})
        return root


def convert(node: Optional[BinTreeNode]) -> Optional[Node]:
    if not node:
        return None
    return Node(node.val, convert(node.left), convert(node.right), None)


def test_three_leveled_tree():
    root = convert(construct([1, 2, 3, 4, 5, None, 7]))
    root = ModifiedPreOrderTraversalSolution().connect(root)
    assert root.left.next == root.right
    assert root.left.left.next == root.left.right
    assert root.left.right.next == root.right.right
    assert root.next is None
    assert root.right.next is None
    assert root.right.right.next is None


def test_empty_tree():
    root = convert(construct([]))
    root = ModifiedPreOrderTraversalSolution().connect(root)
    assert root is None
