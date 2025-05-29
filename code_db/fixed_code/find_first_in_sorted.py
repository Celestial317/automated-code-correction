```python
def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    while lo < hi: # Fix: Change loop condition from 'lo <= hi' to 'lo < hi'
        mid = (lo + hi) // 2

        # If x is found at mid, and it's either the first element
        # or the element before it is different from x, then mid is the first occurrence.
        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        # If x is less than or equal to arr[mid], it means x could be at mid
        # or in the left half. We narrow the search space to [lo, mid).
        elif x <= arr[mid]:
            hi = mid

        # If x is greater than arr[mid], x must be in the right half.
        # We narrow the search space to [mid + 1, hi).
        else:
            lo = mid + 1

    return -1
```