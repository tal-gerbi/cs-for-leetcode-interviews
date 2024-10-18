import heapq
from abc import ABC, abstractmethod
from heapq import heappop, heappush
from typing import List


class Solution(ABC):
    """
        - Title: Kth Largest Element in an Array
        - Available at: https://leetcode.com/problems/kth-largest-element-in-an-array
        - Why was this chosen:
            A simple demonstration of the concept of maintaining a heap with exactly k (largest) items.
    """

    @abstractmethod
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pass


class MaintainLargestElementsSolution(Solution):
    """
    Approach:
        Maintain a min heap of the largest k elements, and return its minimum.

    Complexity:
        Time Complexity: O(n*log k)
        Space Complexity: O(k)
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        largeElements = []
        for n in nums:
            if len(largeElements) == 0 or largeElements[0] < n:
                heappush(largeElements, n)
                if len(largeElements) > k:
                    heappop(largeElements)

        return heappop(largeElements)


def testSmallArray():
    nums = [3, 2, 1, 5, 6, 4]
    assert MaintainLargestElementsSolution().findKthLargest(nums, 2) == 5


def testBigArray():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    assert MaintainLargestElementsSolution().findKthLargest(nums, 2) == 5
