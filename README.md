Motivation
==========
I am preparing for a position in one of the big corps (Microsoft, Google, Palo Alto, etc.). Since a small portion of the admission process 
includes "leetcode" interviews, I decided to refresh some of my knowledge from my bachelor's degree in Computer Science that might be relevant.

In order to prevent this process from becoming too theoretical, I simply solved the Leetcode problem set titled "Top Interval 150" 
(https://leetcode.com/studyplan/top-interview-150). Whenever a familiarity with an old-new data structure or technique was required, I looked up the 
theory (online, and, if necessary, in computer science courses and books), summarized it, and then solved the problem.

By the way, the book "Introduction to Algorithms" by Cormen et al. was what I used the most when more advanced theoretical background was required.


The organization of this project
================================
- In the `problems/` directory there are solutions to various problems from the set above. Problems are organized by the underlying data structure 
used to solve them, and then (sometimes) by technique. I solved all 150 problems in the set, but I attach here only the problems among them that 
  provide (in my opinion) some educational value.
- In the `algorithms/` directory there are implementations of some of the more complex algorithms from the Bachelor's degree (most of them are 
graph-related).
- In the `data_structures/` directory there are various implementations of some useful data structures, including: Binary Trees, Binary Heaps, 
  Graphs, Hashmaps, Linked Lists, Queues, Stacks and Tries. Some of them are used by certain solutions to `problems/` or by certain 
  implementations of `algorithms/`.
- In the `tests/` directory there are some utils used for testing solutions of various problems. These utils, too, are categorized by the 
underlying data structure.
- In the `theory/` directory there are summaries of the relevant theory for each data structure.


The inner organization of problem solutions
============================================
Each problem is solved in a single file, which contains the following (in order):
1. Documentation of the problem:
    - The name and description link of the problem
    - Why this problem was included
2. For each solution:
    - A few words about the approach I have chosen
    - Complexity analysis (both in terms of time and space)
    - The actual implementation
3. Tests for each of the solutions (only the examples provided by Leetcode are tested)

P.S.
====
I use `camelCase` (for methods, fields, parameters, and variables) everywhere. I still use `snake_case` for file names and module names.
I know PEP8 says `snake_case` should be used pretty much everywhere for "readability", but it's dumb and wrong.
