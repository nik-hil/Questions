# Python interview Questions

1. Difference between list and tuple
1. How to create immutable object? `__slots__`
1. What are various magic methods?
1. Which objects we can use as keys in dict
1. which method are required to implement hash? `__hash__ & __eq__ or __cmp__`
1. implement ordered dict
1. `with` context manager with example other than file access
1. GIL
1. Python thread lock example
1. Python producer consumer example
1. Python fibonacci series
1. Python yield keyword. How to stop iteration in generator with yield
1. Difference between generator and list comprehension
1. Design pattern in Python? Singleton, Observer, Strategy, iterator, Factory, Decorator
1. Decorator example. Difference with closure? `too_big and italic from stackoverflow`
1. How to call parent method in child? Pass the instance of parent to child explicitly.
```
    a = A()
    b = B() # B is child of A
    b.solve(a)
```


1. Composition vs inheritance? Which is preferred?  Composition
1. Python inheritance order resolution? multiple inheritance
1. Python difference between old class & new class
1. Python reference by object
1. Python weak reference
1. Python `type` and `metaclass` example
1. Python sort a list or string
1. Python example of lambda function
1. Python sort list of dict by a key
1. Python exception resolution
1. Python accept input from command line? sys.argv
1. Python getattr vs getattribute
1. Python @property & @attr.setter
1. list slicing. arr[-1:-3:1] vs arr[-1:-3:-1]
1. Python treading pipe, queue
1. Python LRU & LFU cache
1. Python private/ protected variable. Access __variable of class.
1. Python keywords

# Django
1. How to modify view to log the request details? decorator
1. Django request response cycle
1. Django middleware classes
1. Django router
1. Django models, forms, validation, Response object, urls file content


# Algorithms & Problem solving (interviewbit.com & GeeksforGeeks.org)
1. Knapsack
1. [tapping rain Water / Horizontal stripes on the wall](https://github.com/nik-hil/Questions/blob/master/problems/tapping_rain_water.py)
1. [coin exchange problem](https://github.com/nik-hil/Questions/blob/master/problems/Coin_denomination.py) 
1. sort the array with 0, 1 & 2
1. sort the array with 0 and 1
1. find the best day to buy and sell stock given in an array
1. [In an sorted array find the frequency of duplicated elements](https://github.com/nik-hil/Questions/blob/master/problems/Coin_denomination.py)
1. Remove duplicate in an list
1. Modify tree with sum of child's value
1. Left view, right view, down view of the tree
1. stack from list
1. Reverse a stack without using extra space
1. Check palindrome represented as linked list? Use traversing to find len. 
Use recursion to reach middle of list. Add pts to check palindrome after returning
from recursion.
1. Shuffle the card deck
1. topological sort
1. Matrix chain multiplication
1. Quick sort and merge sort algorithm
1. Check if a binary tree is subtree of another binary tree | Set 1 - GeeksforGeeks
1. Median in a stream of integers (running integers) 
1. Find avg of last five minutes in a stream of integers
1. Permutation of string
1. word ladder
1. [Max area of 1's island in matrix of 0 & 1](https://www.youtube.com/watch?v=W8VuDt0eb5c)
1. Given matrix of 0 & 1 and 0 is before 1. Find the count of 0 or 1 in O(n). 
Iterate through first row. Find 1's location. Go to next row at same index. Find 
1's location and so on.
1. Calculate a^b using binary search
1. Clone linked list with random pointers
1. Given timing for booking of meeting room. Find min meeting rooms.
1. Sq root via binary search
1. Find a + b + c = 0/d in an array
1. inorder/ preorder/ post order traversal with & without recursion
1. Distance between two string 
1. Sum of two number in BST
1. Spiral view of a tree
1. [Write a function to find the longest common prefix string amongst an array of strings.](https://leetcode.com/problems/longest-common-prefix/)

# System Design (educative.io & youtube)
1. Design hotel booking System
1. Design Cricinfo. Use cdn to dump all updates
1. How to add track objects to remove from cache in Redis. Each object has a time limit.
Use a queue with expiry timestamp and value. Lowest expiry time at head of queue.
Highest expiry time at tail of queue. Check head of queue for expired element.
Insert with logN complexity
1. twitter/ Whatsapp/ FB messenger/ Uber design
1. RabitMQ usage
1. Design nginx web proxy. Use trie
1. Reddit design
1. Design cache
