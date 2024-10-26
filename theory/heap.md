# Heaps

A *min heap* is a special case of a complete binary tree, where for every *parent* and *child*, it holds that:
`parent.val <= child.val`

A *max heap* is a special case of a complete binary tree, where for every *parent* and *child*, it holds that:
`child.val >= child.val`

(See `binary_tree.md` for an explanation of what this means).

Heaps provide the following operations:
- They can be be built from an array in *O(n)*.
- new elements can be added in *O(log n)*.
- The minimum / maximum can be removed in *O(log n)*.


# Implementation of a min heap
Since a heap is a complete binary tree, it is usually implemented on top of an array.
In this array, *arr*, the left and right children of _arr[i]_ are _arr[2*i+1]_ and _arr[2*i+2]_ (If they are present in the array).

## Building a heap in O(n) time
In order to build a min heap from an array in time O(n), the following algorithm is used:
```python
from typing import List, Optional


def __init__(self, arr: List[int]):
    self.capacity = self.size = len(arr)
    self.heapify(arr)

def heapify(self, arr: List[int]):
    for i in range(self.size//2-1, -1, -1):
        self.heapifyDown(arr, i)
        
def heapifyDown(self, arr: List[Optional[int]], i: int):
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
```

If h is the height of the tree, then,
```math
\displaylines{
    1 + ... + 2^{h-1} \le n \\
    2^{h} - 1 \le n \\
    2^{h} \le n+1 \\
    2^{h+1} \le 2*n + 2 \\
    2^{h+1} - 1 \le 2*n + 1
}
```
Now, since the amount of swaps between level k-1 to level k is at most `2^k-1` (The number of elements in the first k-1 layers), we get a total number of swaps of
```math
\begin{aligned}
(2^{1}-1) + (2^{2}-1) + ... + (2^{h}-1) \le
2^{1} + 2^{2} + ... + 2^{h} =
2^{h+1} - 1 \le
2*n + 1
\end{aligned}
```
Therefore, the time complexity of *heapify* is *O(n)*.


## Remove the minimum element
We swap the root element with the last element in the heap, and heapify the new root down the tree:
```python
def pop(self) -> int:
    minElement = self.arr[0]
    self.arr[0] = self.arr[self.size-1]
    self.arr[self.size-1] = None
    self.size -= 1
    self.heapifyDown(self.arr, 0)
    return minElement
```

## Adding a new element
We double the array if needed, put the new element at the end, and heapify the new element up the tree:
```python
from typing import List, Optional


def heapifyUp(self, arr: List[Optional[int]], i: int):
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
```
