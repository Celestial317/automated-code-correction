
from heapq import *

def shortest_path_length(length_by_edge, startnode, goalnode):
    # 2. Introduce a distances dictionary to store the shortest distance found so far
    # Initialize startnode's distance to 0, others implicitly float('inf')
    distances = {startnode: 0}
    
    # unvisited_nodes acts as the priority queue (min-heap)
    # storing (distance, node) pairs. Initialize with the startnode.
    unvisited_nodes = []
    heappush(unvisited_nodes, (0, startnode))
    
    while unvisited_nodes: # Continue as long as there are nodes to process
        current_dist, node = heappop(unvisited_nodes)

        # 3. Refactor the main while loop:
        # Crucial check: If we've already found a shorter path to 'node' than 'current_dist',
        # this entry from the heap is outdated/stale. Discard it.
        if current_dist > distances.get(node, float('inf')):
            continue

        # If the current node is the goal node, we have found the shortest path.
        if node is goalnode:
            return current_dist

        # Explore neighbors (successors) of the current node
        for nextnode in node.successors:
            # Calculate the distance to the nextnode through the current node
            edge_length = length_by_edge[node, nextnode]
            new_dist = current_dist + edge_length

            # If a shorter path to nextnode is found than what was previously recorded
            if new_dist < distances.get(nextnode, float('inf')):
                distances[nextnode] = new_dist # Update the shortest distance to nextnode
                heappush(unvisited_nodes, (new_dist, nextnode)) # Add/update in the priority queue

    # If the loop finishes and the goal node was not reached, it means it's unreachable.
    return float('inf')

"""
Shortest Path

dijkstra

Implements Dijkstra's algorithm for finding a shortest path between two nodes in a directed graph.

Input:
   length_by_edge: A dict with every directed graph edge's length keyed by its corresponding ordered pair of nodes
   startnode: A node
   goalnode: A node

Precondition:
    all(length > 0 for length in length_by_edge.values())

Output:
    The length of the shortest path from startnode to goalnode in the input graph
"""
