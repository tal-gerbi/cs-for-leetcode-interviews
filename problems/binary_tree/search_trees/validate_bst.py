from abc import ABC, abstractmethod
from typing import Optional

from data_structures.binary_tree.binary_tree import BinTreeNode
from tests.binary_tree.construct import construct


class Solution(ABC):
    """
        - Title: Validate Binary Search Tree
        - Available at: https://leetcode.com/problems/validate-binary-search-tree/
        - Why was this chosen:
            Demonstrates nicely what a binary search tree is.
    """

    @abstractmethod
    def isValidBST(self, root: Optional[BinTreeNode]) -> bool:
        pass


class MaxMinSolution(Solution):
    """
    Approach:
        Calculate recursively the minimum, the maximum and whether the search tree is valid.

    Complexity:
        Time Complexity: O(n)
        Space Complexity: O(h)
    """

    def _minMaxValid(self, root: Optional[BinTreeNode]) -> (float, float, bool):
        if root is None:
            return float("inf"), float("-inf"), True

        minLeft, maxLeft, validLeft = self._minMaxValid(root.left)
        if not validLeft:
            return float("inf"), float("-inf"), False
        if root.val <= maxLeft:
            return float("inf"), float("-inf"), False

        minRight, maxRight, validRight = self._minMaxValid(root.right)
        if not validRight:
            return float("inf"), float("-inf"), False
        if root.val >= minRight:
            return float("inf"), float("-inf"), False

        return min(minLeft, minRight, root.val), max(maxLeft, maxRight, root.val), True

    def isValidBST(self, root: Optional[BinTreeNode]) -> bool:
        _, _, valid = self._minMaxValid(root)
        return valid


def test_small_tree():
    root = construct([2, 1, 3])
    assert MaxMinSolution().isValidBST(root)


def test_large_tree():
    root = construct([5, 1, 4, None, None, 3, 6])
    assert not MaxMinSolution().isValidBST(root)
