from abc import ABC, abstractmethod
from typing import List, Optional

from data_structures.binary_tree.binary_tree import TreeNode
from tests.binary_tree.construct import construct


class Solution(ABC):
    """
        - Title: Binary Tree Level Order Traversal
        - Available at: https://leetcode.com/problems/binary-tree-level-order-traversal/
        - Why was this chosen:
            In order to be familiar with the concept of level-order traversal
    """

    @abstractmethod
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


class LevelOrderSolution(Solution):
    """
    Approach:
        Move from one level to the next.

    Complexity:
        Time Complexity: O(n)
        Space Complexity: O(n)
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        currentLevel = [root] if root else []
        while currentLevel:
            levels.append([node.val for node in currentLevel])
            nextLevel = []
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
        return levels


def test_tree_with_three_levels():
    root = construct([3, 9, 20, None, None, 15, 7])
    assert LevelOrderSolution().levelOrder(root) == [[3], [9, 20], [15, 7]]


def test_tree_with_single_node():
    root = construct([1])
    assert LevelOrderSolution().levelOrder(root) == [[1]]


def test_empty_tree():
    root = construct([])
    assert LevelOrderSolution().levelOrder(root) == []
