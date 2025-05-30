def detect_cycle(node):
    """
    Linked List Cycle Detection
    tortoise-hare

    Implements the tortoise-and-hare method of cycle detection.

    Input:
        node: The head node of a linked list

    Output:
        Whether the linked list is cyclic
    """
    if node is None or node.successor is None:
        return False

    tortoise = node.successor
    hare = node.successor.successor

    # Loop continues as long as hare and hare.successor are valid (not None).
    # This prevents AttributeError when hare reaches the end of a non-cyclic list.
    while hare is not None and hare.successor is not None:
        if hare is tortoise:
            return True
        tortoise = tortoise.successor
        hare = hare.successor.successor

    return False