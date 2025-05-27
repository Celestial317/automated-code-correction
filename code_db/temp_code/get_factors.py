```python
def get_factors(n):
    if n == 1:
        return []

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return [i] + get_factors(n // i)

    # If the loop completes, it means n has no divisors up to its square root,
    # implying n is a prime number greater than 1.
    return [n]
```