def reverse_linked_list(node):
    prevnode = None
    while node:
        nextnode = node.successor
        node.successor = prevnode
        prevnode = node # Update prevnode to the current node, as it's now the head of the reversed part
        node = nextnode
    return prevnode