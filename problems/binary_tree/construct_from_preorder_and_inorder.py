from abc import abstractmethod, ABC
from typing import Dict, List, Optional

import pytest

from data_structures.binary_tree.binary_tree import BinTreeNode
from tests.binary_tree.same import assertTreeIsSameAsArray


class Solution(ABC):
    """
        - Title: Construct Binary Tree from Preorder and Inorder Traversal
        - Available at: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
        - Why was this chosen:
            Just to get the feeling of the meaning of pre-order and in-order traversals.
    """
    @abstractmethod
    def buildTree(self, preOrder: List[int], inOrder: List[int]) -> Optional[BinTreeNode]:
        pass


class NaiveSolution(Solution):
    """
    Approach:
        1. if preOrder == inOrder == [], return None
        2. otherwise:
            2.1. rootVal = preOrder[0]
            2.2. index = inOrder.index(rootVal)
            2.3. then:
                2.3.1. leftPreOrder  == preOrder[1:index+1]
                2.3.2. leftInOrder   == inOrder[0:index]
                2.3.3. rightPreOrder == preOrder[index+1:]
                2.3.4. rightInOrder  == inOrder[index+1:]
                2.3.5. therefore, continue recursively for both subtrees and construct the new tree

    Complexity:
        Time Complexity: O(n^2)
        Space Complexity: O(h)
    """

    def buildTree(self, preOrder: List[int], inOrder: List[int]) -> Optional[BinTreeNode]:
        if not preOrder:
            return None

        rootVal = preOrder[0]
        index = inOrder.index(rootVal)
        return BinTreeNode(
            rootVal,
            self.buildTree(preOrder[1:index+1], inOrder[:index]),
            self.buildTree(preOrder[index+1:], inOrder[index+1:])
        )


class LookupSolution(Solution):
    """
        Approach:
            same as before, except we build a dictionary that looks up indexes of items in inOrder first.

        Complexity:
            Time Complexity: O(n)
            Space Complexity: O(n)
        """

    def _buildTree(self, preOrder: List[int], inOrder: List[int], inOrderLookup: Dict[int, int]) -> Optional[BinTreeNode]:
        if not preOrder:
            return None

        rootVal = preOrder[0]
        index = inOrderLookup[rootVal]
        return BinTreeNode(
            rootVal,
            self.buildTree(preOrder[1:index+1], inOrder[:index]),
            self.buildTree(preOrder[index+1:], inOrder[index+1:])
        )

    def buildTree(self, preOrder: List[int], inOrder: List[int]) -> Optional[BinTreeNode]:
        inOrderLookup = {}
        for i, num in enumerate(inOrder):
            inOrderLookup[num] = i
        return self._buildTree(preOrder, inOrder, inOrderLookup)


@pytest.mark.parametrize("solution", [NaiveSolution(), LookupSolution()])
def testThreeLeveledTree(solution: Solution):
    tree = solution.buildTree(preOrder=[3, 9, 20, 15, 7], inOrder=[9, 3, 15, 20, 7])
    assertTreeIsSameAsArray(tree, [3, 9, 20, None, None, 15, 7])


@pytest.mark.parametrize("solution", [NaiveSolution(), LookupSolution()])
def testTreeWithJustRoot(solution: Solution):
    tree = solution.buildTree(preOrder=[1], inOrder=[1])
    assertTreeIsSameAsArray(tree, [1])


@pytest.mark.parametrize("solution", [NaiveSolution(), LookupSolution()])
def testEmptyTree(solution: Solution):
    tree = solution.buildTree(preOrder=[], inOrder=[])
    assertTreeIsSameAsArray(tree, [])
