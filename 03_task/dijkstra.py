# Updated implementation from LMS
def dijkstra_path(graph, from_node) -> dict[(float, list[str])]:
    nodes = graph.nodes()
    # distance is represented by distance and path
    distances = {vertex: (float('infinity'), []) for vertex in nodes}
    distances[from_node] = (0, [from_node])
    unvisited = list(nodes)

    while unvisited:
        # Find the vertex with min distance to `from_node`
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex][0])

        cur_distance, cur_path = distances[current_vertex]
        if cur_distance == float('infinity'):
            break

        for neighbor in graph[current_vertex]:
            weight = graph[current_vertex][neighbor]["weight"]
            distance = cur_distance + weight

            # If new distance is shorter than update shortest path
            if distance < distances[neighbor][0]:
                distances[neighbor] = (distance, cur_path+[neighbor])
        # remove current vertex from unvisited nodes
        unvisited.remove(current_vertex)

    return distances
