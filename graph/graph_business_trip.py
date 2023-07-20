from graph.graph import Graph

def business_trip(graph:Graph,arr):
    """
    function that takes in a graph and an array of city names
    and Return: the cost of the trip (if it’s possible) or null (if not)
    """
    cost = 0
    for i in range(len(arr)-1):
        current_city = graph.get_vertex(arr[i])
        next_city = graph.get_vertex(arr[i+1])
        if not current_city or not next_city:
            return None
        for edge in graph.get_neighbors(current_city):
            if edge.vertex == next_city:
                cost += edge.weight
    return cost


if __name__ == "__main__":
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
    print(business_trip(graph,['Metroville', 'Pandora'])) # 
    print(business_trip(graph,['Arendelle', 'Monstroplolis', 'Naboo']))
    print(business_trip(graph,['Naboo', 'Pandora']))
    print(business_trip(graph,['Narnia', 'Arendelle', 'Naboo']))
    print(business_trip(graph,['Narnia', 'Naboo']))
    print(business_trip(graph,['Narnia', 'Metroville', 'Naboo']))
    print(business_trip(graph,['Narnia', 'Arendelle', 'Metroville', 'Naboo']))