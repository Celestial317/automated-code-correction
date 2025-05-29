```python
from collections import deque as Queue
 
def breadth_first_search(startnode, goalnode):
    queue = Queue()
    nodesseen = set()

    # Add the startnode to the queue and mark it as seen
    queue.append(startnode)
    nodesseen.add(startnode)

    # Loop while the queue is not empty (addresses issue 1)
    while queue:
        node = queue.popleft()

        if node is goalnode:
            return True
        else:
            # Iterate through successors and add to queue/nodesseen only if not seen (addresses issue 2)
            for successor_node in node.successors:
                if successor_node not in nodesseen:
                    nodesseen.add(successor_node)  # Mark as seen when added to queue
                    queue.append(successor_node)

    # If the loop finishes, the goalnode was not found (return False is now reachable)
    return False
```