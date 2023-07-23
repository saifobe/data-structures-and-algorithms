from graph.node import Node
from stack_and_queue.queue import Queue
from stack_and_queue.stack import Stack
class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_vertex(self, value):
        """Adds a vertex to the graph and returns it"""
        vertex = Node(value)
        self._adjacency_list[vertex] = []
        return vertex
    
    def add_edge(self, start_vertex, end_vertex, weight=0):
        """Adds an edge between two vertices in the graph"""
        if start_vertex not in self._adjacency_list.keys():
            raise KeyError('Start Vertex not in Graph')
        if end_vertex not in self._adjacency_list.keys():
            raise KeyError('End Vertex not in Graph')
        
        edge1 = Edge(end_vertex, weight)
        self._adjacency_list[start_vertex].append(edge1)

        edge2 = Edge(start_vertex, weight)
        self._adjacency_list[end_vertex].append(edge2)

        weight = 0
        for edge in self._adjacency_list[start_vertex]:
            weight += edge.weight


    def get_vertices(self):
        """Returns all of the vertices in the graph as a collection (set, list, or similar)"""
        return self._adjacency_list.keys()
    
    def get_neighbors(self, vertex):
        """Returns a collection of edges connected to the given vertex"""
        return self._adjacency_list[vertex]
    
    def get_vertex(self, value):
        """Returns the vertex with the given value"""
        for vertex in self._adjacency_list.keys():
            if vertex.value == value:
                return vertex
        return None
    
    def size(self):
        """Returns the total number of vertices in the graph"""
        if len(self._adjacency_list.keys()) == 0:
            return None
        return len(self._adjacency_list.keys())
    
    def graph_breadth_first(self, node):
        """Returns a collection of nodes in the order they were visited"""
        arr = []
        queue = Queue()
        queue.enqueue(node)
        visited = set()
        visited.add(node)
        while not queue.is_empty():
            front = queue.dequeue()
            arr.append(front.value)
            for edge in self._adjacency_list[front]:
                if edge.vertex not in visited:
                    queue.enqueue(edge.vertex)
                    visited.add(edge.vertex)
        return arr

    def Depth_first(self,node:Node):
        """Returns a collection of nodes in the order they were visited"""
        if node is None:
            return []
        else:
            arr = []
            stack = Stack()
            stack.push(node)
            visited = set()
            visited.add(node)
            while not (stack.is_empty()):
                top = stack.pop()
                arr.append(top.value)
                for edge in self._adjacency_list[top]:
                    if edge.vertex not in visited:
                        stack.push(edge.vertex)
                        visited.add(edge.vertex)
            return arr
    
    
if __name__ == "__main__":
    # graph = Graph()
    # start = graph.add_vertex('start')
    # end = graph.add_vertex('end')
    # graph.add_edge(start, end)
    # print(graph.get_neighbors(start)[0].vertex.value)

    g = Graph()
    a = g.add_vertex('a')
    b = g.add_vertex('b')
    c = g.add_vertex('c')
    d = g.add_vertex('d')
    e = g.add_vertex('e')
    f = g.add_vertex('f')
    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(b, d)
    g.add_edge(c, d)
    g.add_edge(c, e)

    print(g.graph_breadth_first(a))
    print(g.Depth_first(a))