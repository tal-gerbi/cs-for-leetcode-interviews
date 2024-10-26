from typing import List, Optional


class MinHeap:
    def __init__(self, arr: List[int] | None = None):
        if arr is None:
            self.arr: List[Optional[int]] = []
        else:
            self.arr: List[Optional[int]] = arr
            self.size = self.capacity = len(self.arr)
            self._heapify(arr)

    def _heapify(self, arr: List[int]):
        for i in range(self.size//2-1, -1, -1):
            self._heapifyDown(arr, i)

    def _heapifyDown(self, arr: List[Optional[int]], i: int):
        bestChild = True
        while bestChild:
            left = 2 * i + 1
            right = 2 * i + 2
            bestChild = None
            if left < self.size and arr[left] < arr[i]:
                bestChild = left
            if right < self.size and arr[right] < arr[i]:
                if not bestChild or arr[right] < arr[left]:
                    bestChild = right
            if bestChild:
                arr[i], arr[bestChild] = arr[bestChild], arr[i]
                i = bestChild

    @staticmethod
    def _heapifyUp(arr: List[Optional[int]], i: int):
        while i >= 0:
            parent = i // 2
            if arr[parent] <= arr[i]:
                return
            arr[parent], arr[i] = arr[i], arr[parent]
            i = parent

    def push(self, n: int):
        if self.size == self.capacity:
            elementsToAdd = 1 if self.capacity == 0 else self.capacity
            self.arr = self.arr + [None] * elementsToAdd
            self.capacity = len(self.arr)

        self.size += 1
        self.arr[self.size-1] = n
        self._heapifyUp(self.arr, self.size-1)

    def peek(self) -> int:
        return self.arr[0]

    def pop(self) -> int:
        minElement = self.arr[0]
        self.arr[0] = self.arr[self.size-1]
        self.arr[self.size-1] = None
        self.size -= 1
        self._heapifyDown(self.arr, 0)
        return minElement

    def __len__(self) -> int:
        return self.size

