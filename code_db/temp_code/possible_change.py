```python
# Python 3
def possible_change(coins, total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    # Fix: Add a base case to handle an empty 'coins' list
    # If there are no coins left and the total is still greater than zero,
    # there are no possible ways to make change.
    if not coins:
        return 0

    first, *rest = coins
    return possible_change(coins, total - first) + possible_change(rest, total)
```