
def shortest_paths(source, weight_by_edge):
    # 1. Collect all unique nodes from the edges and the source
    all_nodes = set()
    for u, v in weight_by_edge.keys():
        all_nodes.add(u)
        all_nodes.add(v)
    all_nodes.add(source)

    # 2. Initialize weight_by_node for all collected nodes with infinity
    # and set the source node's weight to 0.
    weight_by_node = {node: float('inf') for node in all_nodes}
    weight_by_node[source] = 0

    # Bellman-Ford algorithm: Iterate |V| - 1 times
    # where |V| is the number of nodes in the graph.
    # This ensures that shortest paths with up to |V|-1 edges are found.
    for _ in range(len(all_nodes) - 1):
        # In each iteration, relax all edges.
        for (u, v), weight in weight_by_edge.items():
            # 3. Correct Bellman-Ford relaxation logic:
            # If a path to 'u' has been found (i.e., its weight is not infinity)
            # and the path through 'u' to 'v' is shorter than the current known path to 'v',
            # update the weight of 'v'.
            if weight_by_node[u] != float('inf'):
                weight_by_node[v] = min(weight_by_node[v], weight_by_node[u] + weight)

    return weight_by_node
