
def find_first_in_sorted(arr, x):
    # Handle empty array case first
    if not arr:
        return -1

    lo = 0
    hi = len(arr)  # hi is exclusive, points one past the last element
    ans = -1       # Stores the lowest index found so far

    while lo < hi:  # Loop while search space is valid (lo < hi)
        mid = (lo + hi) // 2

        if arr[mid] == x:
            ans = mid      # Found a potential first occurrence, store it
            hi = mid       # Try to find an even earlier occurrence in the left half (mid is now exclusive upper bound)
        elif arr[mid] < x:
            lo = mid + 1   # x is in the right half
        else:  # arr[mid] > x
            hi = mid       # x is in the left half (mid is now exclusive upper bound)

    return ans
