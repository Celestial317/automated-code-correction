def next_permutation(perm):
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            for j in range(len(perm) - 1, i, -1):
                # Fix 1: Changed comparison to find an element perm[j] GREATER than perm[i]
                if perm[j] > perm[i]:
                    next_perm = list(perm)
                    next_perm[i], next_perm[j] = next_perm[j], next_perm[i]
                    # Fix 2: Converted the reversed iterator to a list for slice assignment
                    next_perm[i + 1:] = list(reversed(next_perm[i + 1:]))
                    return next_perm