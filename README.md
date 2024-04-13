Heaps

A heap is a tree-based data structure that follows the properties of a complete binary tree and is either a min Heap or a max Heap.

Properties
Ordering(min-heap or max-heap)
Structural
Array implementation
It is a complete binary tree

Applications of binary trees
Scheduling tasks
Implementing priority queues
Sorting
Finding the smallest or largest element in an array

Adding items to a heap
Create an array to hold the heap items and increase the heap size by 1 to hold the new item
Insert the item at the end of the heap
Find the parent of the new item and compare the new item with the parent
If the inserted node is larger, swap it with its parent(max heap)
Repeat step  3 until the heap order property is restored.

Removing items from a heap
Replace the root node with the last element
Delete the last element from the heap by reducing the heap size by 1
Compare the new root node with the left and right children
If the children are larger, swap the root node with the child  so the child will take its place
Repeat step 3 until the heap order property is restored.



