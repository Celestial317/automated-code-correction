from collections import deque as Queue
 
def breadth_first_search(startnode, goalnode):
    queue = Queue()
    queue.append(startnode)

    nodesseen = set()
    nodesseen.add(startnode)

    # Loop continues as long as the queue is not empty
    while queue:
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            # Iterate through successors, add to nodesseen and queue only if not seen before
            for successor_node in node.successors:
                if successor_node not in nodesseen:
                    nodesseen.add(successor_node)
                    queue.append(successor_node)

    # If the loop finishes and goalnode was not found, return False
    return False