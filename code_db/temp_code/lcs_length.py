```python
def lcs_length(s, t):
    # Initialize dp as a 2D list of zeros with dimensions (len(s) x len(t))
    # dp[i][j] will store the length of the longest common substring ending at s[i] and t[j]
    dp = [[0] * len(t) for _ in range(len(s))]

    # Initialize max_length to track the overall maximum common substring length found
    max_length = 0

    # Iterate through the strings to fill the DP table
    for i in range(len(s)):
        for j in range(len(t)):
            # If characters s[i] and t[j] match
            if s[i] == t[j]:
                # If it's the first character of either string (base case)
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    # Extend the common substring from the previous diagonal element
                    dp[i][j] = dp[i-1][j-1] + 1
                
                # Update the overall maximum length found
                max_length = max(max_length, dp[i][j])
            # If s[i] != t[j], dp[i][j] remains 0 (as initialized),
            # indicating that a common substring cannot extend past this point.

    return max_length
```