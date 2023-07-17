import pytest
from graph.graph import Graph, Edge

def test_add_vertex():
    graph = Graph()
    expected = 'saif'
    actual = graph.add_vertex('saif').value
    assert actual == expected

def test_add_edge():
    graph = Graph()
    start = graph.add_vertex('start')
    end = graph.add_vertex('end')
    graph.add_edge(start, end)
    expected = 'end'
    actual = graph.get_neighbors(start)[0].vertex.value
    assert actual == expected

def test_get_vertices():
    graph = Graph()
    start = graph.add_vertex('start')
    end = graph.add_vertex('end')
    expected = 2
    actual = len(graph.get_vertices())
    assert actual == expected

def test_get_neighbors():
    graph = Graph()
    start = graph.add_vertex('start')
    end = graph.add_vertex('end')
    graph.add_edge(start, end)
    expected = 'end'
    actual = graph.get_neighbors(start)[0].vertex.value
    assert actual == expected

def test_size():
    graph = Graph()
    node1 = graph.add_vertex('saif')
    node2 = graph.add_vertex('mohammed')
    node3 = graph.add_vertex('obeidat')
    expected = 3
    actual = graph.size()
    assert actual == expected

def test_size_empty():
    graph = Graph()
    expected = None
    actual = graph.size()
    assert actual == expected

def test_empty_graph():
    graph = Graph()
    expected = 'start'
    actual = graph.add_vertex('start').value
    assert actual == expected

def test_one_node_one_edge():
    graph = Graph()
    start = graph.add_vertex('start')
    end = graph.add_vertex('end')
    graph.add_edge(start, end)
    expected = 'end'
    actual = graph.get_neighbors(start)[0].vertex.value
    assert actual == expected

def test_breadth_first():
    graph = Graph()
    start = graph.add_vertex('start')
    end = graph.add_vertex('end')
    graph.add_edge(start, end)
    expected = ['start', 'end']
    actual = graph.graph_breadth_first(start)
    assert actual == expected

def test_breadth_first_seven_edges():
    graph = Graph()
    start = graph.add_vertex('start')
    node1 = graph.add_vertex('node1')
    node2 = graph.add_vertex('node2')
    node3 = graph.add_vertex('node3')
    node4 = graph.add_vertex('node4')
    node5 = graph.add_vertex('node5')
    end = graph.add_vertex('end')
    graph.add_edge(start, node1)
    graph.add_edge(start, node2)
    graph.add_edge(start, node3)
    graph.add_edge(node1, node4)
    graph.add_edge(node2, node5)
    graph.add_edge(node3, end)
    graph.add_edge(node4, end)
    graph.add_edge(node5, end)
    expected = ['start', 'node1', 'node2', 'node3', 'node4', 'node5', 'end']
    actual = graph.graph_breadth_first(start)
    assert actual == expected

def test_breadth_empty_edge():
    graph = Graph()
    start = graph.add_vertex('start')
    expected = ['start']
    actual = graph.graph_breadth_first(start)
    assert actual == expected



    


