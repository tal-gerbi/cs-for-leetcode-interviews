from abc import ABC, abstractmethod
from heapq import heappop, heappush
from typing import List


class Solution(ABC):
    """
        - Title: IPO
        - Available at: https://leetcode.com/problems/ipo/
        - Why was this chosen:
            A hard problem involving a heap
    """

    @abstractmethod
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pass


class MaxHeapSolution(Solution):
    """
    Approach:
        - Maintain a max heap of profits at any given point, with all the projects whose capital is lower or equals to the capital we have.
        - Greedily choose the project with the maximum profit in the heap.

    Complexity:
        Time Complexity: O(n*log n + k)
        Space Complexity: O(n)
    """

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(capital)
        capital_then_profit = sorted((c, p) for (c, p) in zip(capital, profits))
        profits_heap = []

        i = 0
        while k > 0:
            while i < n and capital_then_profit[i][0] <= w:
                heappush(profits_heap, -capital_then_profit[i][1])
                i += 1
            if len(profits_heap) == 0:
                break

            best_profit = heappop(profits_heap)
            w += -best_profit
            k -= 1
        return w


def testFirstExample():
    assert MaxHeapSolution().findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]) == 4


def testSecondExample():
    assert MaxHeapSolution().findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]) == 6
