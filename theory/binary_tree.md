# Trees

In graph theory, a **tree** is an undirected graph *G=(V,E)* that is connected and contains no cycles (See `graphs.md` for an explanation of what this means).

It can be shown that all the following definitions for a tree are equivalent:
* *G* is connected and contains no cycles ("acyclic").
* *G* is acyclic, but any edge *e=(u,v)* that is added to G forms a simple cycle.
* *G* is connected, but would become disconnected if any edge *e=(u,v)* is removed from it.
* Any two vertices in V are connected by a unique simple path.

Properties of a tree include:
* *|E| = |V| - 1*
* Every tree has at least two leaves, that is, two distinct vertices *u, v* with *d(u) = d(v) = 1*


# Rooted trees
Since any pair of vertices in a tree is connected by a unique simple path, another way to look at a tree is to distinguish one of the vertices (the "root") from the others.
By doing this we form a "rooted tree", or an hierarchy of nodes that starts at the root node. We then use the following terminology for a rooted tree with root *r*:
* For any node *x*, we call any node *y* in the unique path from *r* to *x* an **ancestor** of *x*.
* If *y* is an ancestor of *x*, we say that *x* is a **descendant** of *y*.
* The **subtree rooted at _x_** is the tree induced by descendants of *x*, that is rooted at *x*.
* If *(y,x)* is the last edge in the path from *r* to *x*, we say that *y* is the **parent** of *x*.
* If *y* is the parent of *x*, we say that *x* is the **child** of *y*.
* A node with no children is called a **leaf**.
* The length of the unique path from *r* to *x* is called the **depth** of x.
* All the nodes with the same **depth** form a **level** of the tree.
* The **height** of a tree is the number of edges in the longest downward path from the root to a leaf.


# Binary trees
Binary trees are a special case of rooted trees, where every node has only two optional children. We then use the following terminology:
* The children of a node are referred to as the **left child** and **right child** of their parent.
* Their respected subtrees are the **left subtree** and **right subtree**.
* We call a binary tree a **complete binary tree** if all its levels, except possibly the last one, are filled from left to right.


# Implementation of binary trees
Usually binary trees are implemented by keeping a reference from a parent node to both its (optional) children.
```
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right
```

However, a complete binary tree, like a heap (see `heap.md`), can also be implemented on top of an array, with the elements in indexes _2*i_ and _2*i+1_ being the left and right children of the *i*-th element.


# Search trees
Search trees are binary trees with the following properties:
* If *u* is the left child of *v*, then `u.val < v.val`
* If *u* is the right child of *v*, then `u.val > v.val`

Therefore, if search trees are balanced, that is, `Height(tree) = O(log n)`, with *n* being the number of nodes in the tree, then finding an element in the tree would take only `O(log n)` time.


# Techniques
## Pre-order, in-order and post-order scans
Scan the tree recursively, with the current node being processed:
* before the left and right subtrees (in *pre-order*).
* after the left subtree, but before the right subtree (in *in-order*).
* after the left and right subtrees (in *post-order*).

## Level-order traversal
A BFS scan starting at the root. Therefore, in every stage, only the nodes in the next level of the tree are scanned.