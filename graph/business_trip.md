# Business Trip Function

## Challenge
<!-- Description of the challenge -->
Write a function that takes in a graph and an array of city names and Return: the cost of the trip (if it’s possible) or null (if not)

## Whiteboard Process
<!-- Embedded whiteboard image -->
![graph-business-trip](./Business%20Trip.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- Time: O(n*m)
- Space: O(1)

## Solution
<!-- Show how to run your code, and examples of it in action -->
```
graph = Graph()
node1 = graph.add_node('A')
node2 = graph.add_node('B')

graph.add_edge(node1, node2, 150)

print(graph.business_trip(['A', 'B']))
```

## [code](./graph_business_trip.py)
## [test](./tests/test_graph.py)

