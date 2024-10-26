from abc import ABC, abstractmethod
from typing import Optional

from data_structures.binary_tree.binary_tree import TreeNode
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
            A nice use case for when level-order traversal may be relevant
    """

    @abstractmethod
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        pass


class LevelOrderTraversalSolution(Solution):
    """
    Approach:
        Scan in level-order traversal and set the next pointers for each level separately

    Complexity:
        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return None

        currentLevel = [root]
        while currentLevel:
            for i in range(len(currentLevel) - 1):
                currentLevel[i].next = currentLevel[i + 1]

            nextLevel = []
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
        return root


def convert(node: Optional[TreeNode]) -> Optional[Node]:
    if not node:
        return None
    return Node(node.val, convert(node.left), convert(node.right), None)


def test_three_leveled_tree():
    root = convert(construct([1, 2, 3, 4, 5, None, 7]))
    root = LevelOrderTraversalSolution().connect(root)
    assert root.left.next == root.right
    assert root.left.left.next == root.left.right
    assert root.left.right.next == root.right.right
    assert root.next is None
    assert root.right.next is None
    assert root.right.right.next is None


def test_empty_tree():
    root = convert(construct([]))
    root = LevelOrderTraversalSolution().connect(root)
    assert root is None
