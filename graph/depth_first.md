# Depth first search

## Challenge
<!-- Description of the challenge -->
Write a depth first traversal method which takes a graph as its unique input. Return a collection of nodes in the order they were visited. Display the collection.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![graph-depth-first](./Depth%20first.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Time: O(n+m)
- Space: O(n)

## Solution

<!-- Show how to run your code, and examples of it in action -->
```
graph = Graph()
node1 = graph.add_node('A')
node2 = graph.add_node('B')
node3 = graph.add_node('C')
node4 = graph.add_node('D')

graph.add_edge(node1, node2)
graph.add_edge(node1, node3)
graph.add_edge(node2, node4)

print(graph.depth_first(node1))
```

## [code](./graph.py)
## [test](./tests/test_graph.py)
