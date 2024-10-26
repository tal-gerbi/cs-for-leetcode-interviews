from abc import ABC, abstractmethod
from heapq import heappop, heappush


class Solution(ABC):
    """
        - Title: Find Median from Data Stream
        - Available at: https://leetcode.com/problems/find-median-from-data-stream/
        - Why was this chosen:
            Demonstrates how we can use a max heap and a min heap together.
    """
    @abstractmethod
    def addNum(self, num: int) -> None:
        pass

    @abstractmethod
    def findMedian(self) -> float:
        pass


class MinHeapMaxHeapSolution(Solution):
    """
    Approach:
        Maintain a min heap for the lower half of the numbers, and a max heap for the higher half.

    Complexity:
        Time Complexity: O(log n) for addNum, O(1) for findMedian
        Space Complexity: O(n)
    """
    def __init__(self):
        self.lowNumbers = []
        self.highNumbers = []

    def addNum(self, num: int) -> None:
        # Add to highers. If there's an imbalance, pop from highers into lowers.
        heappush(self.highNumbers, num)
        if len(self.highNumbers) >= len(self.lowNumbers) + 2:
            lowestHigh = heappop(self.highNumbers)
            heappush(self.lowNumbers, -lowestHigh)
            return

        # If the lowest high is less then the highest low, swap them
        if len(self.highNumbers) == 0 or len(self.lowNumbers) == 0:
            return
        if -self.lowNumbers[0] > self.highNumbers[0]:
            lowestHigh = heappop(self.highNumbers)
            highestLow = heappop(self.lowNumbers)
            heappush(self.lowNumbers, -lowestHigh)
            heappush(self.highNumbers, -highestLow)

    def findMedian(self) -> float:
        if len(self.lowNumbers) == len(self.highNumbers):
            return (self.highNumbers[0] + (-self.lowNumbers[0])) / 2
        return self.highNumbers[0]


def testExample():
    medianFinder = MinHeapMaxHeapSolution()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    assert medianFinder.findMedian() == 1.5
    medianFinder.addNum(3)
    assert medianFinder.findMedian() == 2
