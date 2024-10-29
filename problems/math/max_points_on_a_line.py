from abc import ABC, abstractmethod
from typing import List


class Solution(ABC):
    """
        - Title: Max Points on a Line
        - Available at: https://leetcode.com/problems/max-points-on-a-line/
        - Why was this chosen:
            A hard problem with some math in it.
    """

    @abstractmethod
    def maxPoints(self, points: List[List[int]]) -> int:
        pass


class HashSolution(Solution):
    """
    Approach:
        -Store a distinct set of points for by the x component, supporting lines parallel to the y-axis.
        -Store set of points in a hash by the slope and the intercept of the line that they form.
    Complexity:
        Time Complexity: O(n^2)
        Space Complexity: O(n^2)
    """

    def maxPoints(self, points: List[List[int]]) -> int:
        bySlope = {}
        byX = {}

        for [x, y] in points:
            if x not in byX:
                byX[x] = set()
            byX[x].add((x, y))

        for [x1, y1] in points:
            for [x2, y2] in points:
                if x1 == x2:
                    continue
                m = (y1 - y2)/(x1 - x2)
                b = y1 - m*x1
                if (m, b) not in bySlope:
                    bySlope[(m, b)] = set()
                bySlope[(m, b)].add((x1, y1))
                bySlope[(m, b)].add((x2, y2))

        if len(bySlope) == 0:
            bySlope[(0, 0)] = set() # To prevent max() arg is an empty sequence
        return max(
            max([len(points) for points in bySlope.values()]),
            max([len(points) for points in byX.values()])
        )


def testFirstExample():
    assert HashSolution().maxPoints([[1, 1], [2, 2], [3, 3]]) == 3


def testSecondExample():
    assert HashSolution().maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
