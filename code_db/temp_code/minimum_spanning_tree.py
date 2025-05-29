def minimum_spanning_tree(weight_by_edge):
    group_by_node = {} # Maps each node to the set it belongs to
    mst_edges = set()

    # Sort edges by weight in ascending order
    for edge in sorted(weight_by_edge, key=weight_by_edge.__getitem__):
        u, v = edge

        # Get the sets for nodes u and v. If a node hasn't been seen, create a new set for it.
        set_of_u = group_by_node.setdefault(u, {u})
        set_of_v = group_by_node.setdefault(v, {v})

        # If u and v are not already in the same component (i.e., their sets are different objects)
        if set_of_u is not set_of_v:
            mst_edges.add(edge) # Add the edge to the MST

            # Merge the component of v into the component of u
            set_of_u.update(set_of_v)

            # Update all nodes that were in v's component to now point to the merged set (set_of_u)
            # Iterate through the elements that were originally in set_of_v
            for node in set_of_v:
                group_by_node[node] = set_of_u # Re-assign the reference to the unified set

    return mst_edges