```python
def detect_cycle(node):
    # 1. Handle empty list: If the list is empty, there's no cycle.
    if node is None:
        return False

    hare = tortoise = node
 
    while True:
        # Advance tortoise one step
        tortoise = tortoise.successor

        # 2. Robust Hare Movement:
        # Before advancing hare two steps, ensure that hare and hare.successor are not None.
        # If hare is None, it means hare moved past the end of the list in the previous iteration.
        # If hare.successor is None, it means hare is at the last node, and cannot move two steps.
        # In either case, the end of the list has been reached, so there's no cycle.
        if hare is None or hare.successor is None:
            return False

        # Advance hare two steps
        hare = hare.successor.successor

        # 3. Order of operations: Check for meeting after both have moved.
        if hare is tortoise:
            return True
```