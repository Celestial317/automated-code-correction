
def lcs_length(s, t):
    # 1. DP Table Initialization:
    # dp[i][j] will store the length of the longest common substring
    # ending at s[i-1] and t[j-1].
    # The table is (len(s) + 1) x (len(t) + 1) to handle empty prefixes (base cases).
    m = len(s)
    n = len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize max_len to track the maximum length found anywhere in the DP table.
    max_len = 0

    # 2. Correct Loop Ranges and Indexing:
    # Iterate from 1 up to (and including) m and n.
    # i and j represent the current lengths of prefixes being considered.
    # To access the actual characters, use s[i-1] and t[j-1] because strings are 0-indexed.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 3. Accurate Recurrence Relation:
            # If the characters match, extend the common substring from the previous diagonal cell.
            if s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                # 4. Track Maximum Length:
                # Update max_len if the current dp value is greater.
                max_len = max(max_len, dp[i][j])
            else:
                # If characters do not match, the common substring is broken.
                # Therefore, the length of the common substring ending at these characters is 0.
                dp[i][j] = 0

    # The final answer is the maximum value found anywhere in the dp table.
    return max_len
