from graph.node import Node

class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_vertex(self, value):
        vertex = Node(value)
        self._adjacency_list[vertex] = []
        return vertex
    
    def add_edge(self, start_vertex, end_vertex, weight=0):
        if start_vertex not in self._adjacency_list.keys():
            raise KeyError('Start Vertex not in Graph')
        if end_vertex not in self._adjacency_list.keys():
            raise KeyError('End Vertex not in Graph')
        
        edge1 = Edge(end_vertex, weight)
        self._adjacency_list[start_vertex].append(edge1)

        edge2 = Edge(start_vertex, weight)
        self._adjacency_list[end_vertex].append(edge2)


    def get_vertices(self):
        return self._adjacency_list.keys()
    
    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]
    
    def size(self):
        if len(self._adjacency_list.keys()) == 0:
            return None
        return len(self._adjacency_list.keys())
    
if __name__ == "__main__":
    graph = Graph()
    start = graph.add_vertex('start')
    end = graph.add_vertex('end')
    graph.add_edge(start, end)
    print(graph.get_neighbors(start)[0].vertex.value)