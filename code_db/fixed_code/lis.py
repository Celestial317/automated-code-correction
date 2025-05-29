def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):

        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]

        length = max(prefix_lengths) if prefix_lengths else 0

        new_length = length + 1

        if new_length > longest:
            ends[new_length] = i
            longest = new_length
        elif val < arr[ends[new_length]]:
            ends[new_length] = i

    return longest