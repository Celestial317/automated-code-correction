
def bitcount(n: int) -> int:
    """
    Counts the number of set bits (1s) in the binary representation of a non-negative integer.

    This function uses Brian Kernighan's algorithm, which is an efficient method
    to count set bits. It works by repeatedly flipping the least significant
    set bit to zero until the number becomes zero.

    Args:
        n: A non-negative integer.

    Returns:
        The count of set bits in the integer.
    """
    count = 0
    while n > 0:
        n &= (n - 1)
        count += 1
    return count
