```python
def find_in_sorted(arr, x):
    def binsearch(start, end):
        # Base case: if the search range is empty
        if start >= end: # Changed from start == end to start >= end to handle cases where start becomes greater than end
            return -1
        
        mid = start + (end - start) // 2
        
        if x < arr[mid]:
            # If x is less than the middle element, search in the left half
            return binsearch(start, mid)
        elif x > arr[mid]:
            # If x is greater than the middle element, search in the right half
            # The search should continue *after* mid to avoid infinite recursion
            return binsearch(mid + 1, end) 
        else:
            # If x is equal to the middle element, we found it
            return mid

    # The initial call to binsearch should cover the entire array
    # The 'end' parameter in binsearch represents an exclusive upper bound,
    # so len(arr) is correct for the initial call.
    return binsearch(0, len(arr))
```