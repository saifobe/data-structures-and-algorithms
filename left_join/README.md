# class 32 - Tree intersection

join two hash tables together and return the result as a list of lists

## Whiteboard Process
<!-- Embedded whiteboard image -->
![whiteboard](./Left%20Join.jpg)

## Approach & Efficiency

time: O(n) because we loop throw the first hash table once
space: O(n) because we created hashtable which will store the first hash table values, and we have values values which can be the min(n, m) so in worse case it will be O(n)

## Solution

[Tree Intersection](./left_join.py) \
[test](./tests/test_left_join.py)