from abc import ABC, abstractmethod
from typing import Optional

import pytest

from data_structures.binary_tree.binary_tree import BinTreeNode
from tests.binary_tree.construct import construct


class Solution(ABC):
    """
        - Title: Binary Tree Maximum Path Sum
        - Available at: https://leetcode.com/problems/binary-tree-maximum-path-sum/?envType=study-plan-v2&envId=top-interview-150
        - Why was this chosen:
            This problem requires to separate the recursion to multiple (3) functions.
    """

    @abstractmethod
    def maxPathSum(self, root: BinTreeNode) -> int:
        pass


class MultipleRecursionsSolution(Solution):
    """
    Approach:
        implement the following methods using each other:
            maxPathStartingAtRoot
            maxPathThroughRoot
            maxPathWithoutRoot

        In order to prevent multiple computations on the same subtree, use memoization.
        Then, return the maximum between all three method calls on the given root.

    Complexity:
        Time Complexity: O(n) (due to memoization)
        Space Complexity: O(n)
    """
    def maxPathStartingAtRoot(self, root: Optional[BinTreeNode], d1) -> float:
        if root in d1:
            return d1[root]
        if not root:
            d1[root] = float("-inf")
            return d1[root]

        d1[root] = float(root.val) + max(
            max(0.0, self.maxPathStartingAtRoot(root.left, d1)),
            max(0.0, self.maxPathStartingAtRoot(root.right, d1))
        )
        return d1[root]

    def maxPathThroughRoot(self, root: Optional[BinTreeNode], d1) -> float:
        if not root:
            return float("-inf")

        return (root.val + self.maxPathStartingAtRoot(root.left, d1) +
                self.maxPathStartingAtRoot(root.right, d1))

    def maxPathWithoutRoot(self, root: Optional[BinTreeNode], d1, d2) -> float:
        if root in d2:
            return d2[root]
        if not root:
            return float("-inf")

        m = max(
            self.maxPathStartingAtRoot(root.left, d1),
            self.maxPathThroughRoot(root.left, d1),
            self.maxPathWithoutRoot(root.left, d1, d2),
            self.maxPathStartingAtRoot(root.right, d1),
            self.maxPathThroughRoot(root.right, d1),
            self.maxPathWithoutRoot(root.right, d1, d2)
        )
        d2[root] = m
        return d2[root]

    def maxPathSum(self, root: BinTreeNode) -> int:
        d1 = {}
        d2 = {}
        return int(max(
            self.maxPathStartingAtRoot(root, d1),
            self.maxPathThroughRoot(root, d1),
            self.maxPathWithoutRoot(root, d1, d2),
        ))


class MultipleValuesRecursionSolution(Solution):
    """
    Approach:
        Same as before, except we only use one recursion, that returns 3 values:
            maxPathStartingAtRoot
            maxPathThroughRoot
            maxPathWithoutRoot

    Complexity:
        Time Complexity: O(n)
        Space Complexity: O(h)
    """
    def _maxPathSum(self, root: Optional[BinTreeNode]) -> (float, float, float):
        if not root:
            return float("-inf"), float("-inf"), float("-inf")

        startingAtLeft, throughLeft, withoutLeft = self._maxPathSum(root.left)
        startingAtRight, throughRight, withoutRight = self._maxPathSum(root.right)

        startingAtRoot = root.val + max(0.0, startingAtLeft, startingAtRight)
        throughRoot = root.val + startingAtLeft + startingAtRight
        withoutRoot = max(startingAtLeft, throughLeft, withoutLeft,
                          startingAtRight, throughRight, withoutRight)
        return startingAtRoot, throughRoot, withoutRoot

    def maxPathSum(self, root: BinTreeNode) -> int:
        startingAtRoot, throughRoot, withoutRoot = self._maxPathSum(root)
        return int(max(startingAtRoot, throughRoot, withoutRoot))


@pytest.mark.parametrize("solution", [MultipleRecursionsSolution(), MultipleValuesRecursionSolution()])
def test_small_tree(solution: Solution):
    root = construct([1, 2, 3])
    assert solution.maxPathSum(root) == 6


@pytest.mark.parametrize("solution", [MultipleRecursionsSolution(), MultipleValuesRecursionSolution()])
def test_large_tree(solution: Solution):
    root = construct([-10,9,20,None,None,15,7])
    assert solution.maxPathSum(root) == 42

