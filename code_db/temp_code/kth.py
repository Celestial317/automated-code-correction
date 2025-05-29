import random

def kth(arr, k):
    # The precondition 0 <= k < len(arr) ensures arr is not empty on the initial call.
    # In recursive calls, if k is adjusted correctly, arr should also not become empty
    # unless k is effectively out of bounds for the sub-array, which would be a bug.

    # Select a random pivot to mitigate worst-case O(N^2) time complexity
    # and prevent RecursionError for large, sorted/reverse-sorted inputs.
    pivot = random.choice(arr)
    
    # Partition elements into 'below' (strictly less than pivot)
    # and 'above' (strictly greater than pivot).
    # Elements equal to the pivot are implicitly handled by not being in 'below' or 'above'.
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]
    
    # num_less: count of elements strictly less than the pivot.
    num_less = len(below)
    
    # num_lessoreq: count of elements less than or equal to the pivot.
    # This represents the size of the 'below' partition plus the 'equal to pivot' partition.
    # It can be calculated by subtracting the count of elements strictly greater than pivot
    # from the total number of elements.
    num_lessoreq = len(arr) - len(above) 
    
    if k < num_less:
        # If k falls within the range of elements strictly less than the pivot,
        # recurse on the 'below' partition with the same k.
        return kth(below, k)
    elif k >= num_lessoreq:
        # If k falls within the range of elements strictly greater than the pivot,
        # recurse on the 'above' partition.
        # The k value must be adjusted: subtract the count of elements that are
        # less than or equal to the pivot (num_lessoreq), as these are now 'skipped'.
        return kth(above, k - num_lessoreq)
    else:
        # If k is not in 'below' and not in 'above', it means the kth element
        # is one of the elements equal to the pivot. Since all such elements
        # are identical, the pivot itself is the answer.
        return pivot