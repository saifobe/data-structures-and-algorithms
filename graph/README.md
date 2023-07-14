# Challenge Title
Implement a Graph class

## Challenge
Implement a Graph class without using an existing graph library.

## Code 
```python
class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        v = Vertex(value)
        self._adjacency_list[v] = []
        return v

    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self._adjacency_list:
            raise KeyError('Start Vertex not in Graph')
        if end_vertex not in self._adjacency_list:
            raise KeyError('End Vertex not in Graph')

        edge = Edge(end_vertex, weight)
        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append(edge)

    def get_nodes(self):
        return self._adjacency_list.keys()

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]

    def size(self):
        return len(self._adjacency_list)

```

## Approach & Efficiency
- add_node: O(1)
- add_edge: O(1)
- get_nodes: O(1)
- get_neighbors: O(1)
- size: O(1)

## Solution
path: [graph](./graph.py) \
      [node](./node.py) \
      [tests](./tests/test_graph.py) 
