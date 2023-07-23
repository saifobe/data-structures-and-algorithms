import pytest
from graph.graph import Graph, Edge
from graph.graph_business_trip import business_trip

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

def test_business_trip():
    graph = Graph()
    pandora = graph.add_vertex('Pandora')
    arendelle = graph.add_vertex('Arendelle')
    metroville = graph.add_vertex('Metroville')
    monstroplolis = graph.add_vertex('Monstroplolis')
    naboo = graph.add_vertex('Naboo')
    narnia = graph.add_vertex('Narnia')
    graph.add_edge(pandora,arendelle,150)
    graph.add_edge(arendelle,metroville,99)
    graph.add_edge(arendelle,monstroplolis,42)
    graph.add_edge(metroville,monstroplolis,105)
    graph.add_edge(metroville,naboo,26)
    graph.add_edge(metroville,narnia,37)
    graph.add_edge(monstroplolis,naboo,73)
    graph.add_edge(narnia,naboo,250)
    expected = 0
    actual = business_trip(graph,['Metroville', 'Pandora'])
    assert actual == expected

def test_business_trip_two_cities():
    graph = Graph()
    pandora = graph.add_vertex('Pandora')
    arendelle = graph.add_vertex('Arendelle')
    metroville = graph.add_vertex('Metroville')
    monstroplolis = graph.add_vertex('Monstroplolis')
    naboo = graph.add_vertex('Naboo')
    narnia = graph.add_vertex('Narnia')
    graph.add_edge(pandora,arendelle,150)
    graph.add_edge(arendelle,metroville,99)
    graph.add_edge(arendelle,monstroplolis,42)
    graph.add_edge(metroville,monstroplolis,105)
    graph.add_edge(metroville,naboo,26)
    graph.add_edge(metroville,narnia,37)
    graph.add_edge(monstroplolis,naboo,73)
    graph.add_edge(narnia,naboo,250)
    expected = 115
    actual = business_trip(graph,['Arendelle', 'Monstroplolis', 'Naboo'])
    assert actual == expected

def test_business_trip_not_in_graph():
    graph = Graph()
    pandora = graph.add_vertex('Pandora')
    arendelle = graph.add_vertex('Arendelle')
    expected = None
    actual = business_trip(graph,['saif', 'obeidat'])
    assert actual == expected

def test_business_trip_empty_graph():
    graph = Graph()
    expected = None
    actual = business_trip(graph,['saif', 'obeidat'])
    assert actual == expected
    

def test_depth_first():
    graph = Graph()
    a = graph.add_vertex('a')
    b = graph.add_vertex('b')
    c = graph.add_vertex('c')
    d = graph.add_vertex('d')
    e = graph.add_vertex('e')
    graph.add_edge(a,b)
    graph.add_edge(b,c)
    graph.add_edge(c,e)
    graph.add_edge(e,d)
    expected = ['a', 'b', 'c', 'e', 'd']
    actual = graph.Depth_first(a)
    assert actual == expected

def test_depth_first_two_edges():
    graph = Graph()
    a = graph.add_vertex('a')
    b = graph.add_vertex('b')
    graph.add_edge(a,b)
    expected = ['a', 'b']
    actual = graph.Depth_first(a)
    assert actual == expected

def test_depth_first_one_graph():
    graph = Graph()
    a = graph.add_vertex('a')
    expected = ['a']
    actual = graph.Depth_first(a)
    assert actual == expected





