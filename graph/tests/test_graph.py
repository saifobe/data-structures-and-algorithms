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