```python
def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        # Find the length of the longest increasing subsequence that `val` can extend.
        # `j` represents a length, and `arr[ends[j]]` is the smallest ending element for an LIS of length `j`.
        # We are looking for LIS of length `j` where its ending element is less than `val`.
        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        # `length` is the maximum length of such a subsequence.
        # If no such subsequence exists, `length` is 0.
        length = max(prefix_lengths) if prefix_lengths else 0

        # `new_length` is the potential length if `val` extends an LIS of `length`.
        new_length = length + 1

        # Update `ends` and `longest` based on `new_length`:
        # Condition 1: If `new_length` is greater than the current `longest`,
        # it means `val` forms a new longest increasing subsequence.
        if new_length > longest:
            ends[new_length] = i
            longest = new_length
        # Condition 2: Otherwise (`new_length <= longest`), if `val` provides a smaller
        # ending element for a subsequence of length `new_length` than what is currently stored.
        # This optimizes future extensions by keeping the smallest possible end for each length.
        # `ends[new_length]` is guaranteed to exist here because `new_length <= longest`.
        elif val < arr[ends[new_length]]:
            ends[new_length] = i

    return longest


"""
Longest Increasing Subsequence
longest-increasing-subsequence


Input:
    arr: A sequence of ints

Precondition:
    The ints in arr are unique

Output:
    The length of the longest monotonically increasing subsequence of arr

Example:
    >>> lis([4, 1, 5, 3, 7, 6, 2])
    3
"""
```