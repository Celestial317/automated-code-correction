import collections

def topological_ordering(nodes):
    # 1. Calculate Initial In-degrees:
    # Determine the number of incoming edges for every node in the graph.
    in_degrees = {node: 0 for node in nodes}
    for node in nodes:
        for neighbor in node.outgoing_nodes:
            in_degrees[neighbor] += 1

    # 2. Initialize Queue:
    # Create a queue and add all nodes that have an in-degree of 0 to this queue.
    # These are the nodes that can be processed first.
    queue = collections.deque()
    for node in nodes:
        if in_degrees[node] == 0:
            queue.append(node)

    # Initialize the list to store the topologically ordered nodes
    ordered_nodes = []

    # 3. Process Nodes:
    # While the queue is not empty, process nodes.
    while queue:
        # Dequeue a current_node.
        current_node = queue.popleft()
        # Add current_node to your ordered_nodes result list.
        ordered_nodes.append(current_node)

        # For each neighbor that current_node has an outgoing edge to:
        for neighbor in current_node.outgoing_nodes:
            # Decrement the neighbor's in-degree.
            in_degrees[neighbor] -= 1
            # If the neighbor's in-degree becomes 0, enqueue it.
            if in_degrees[neighbor] == 0:
                queue.append(neighbor)

    return ordered_nodes