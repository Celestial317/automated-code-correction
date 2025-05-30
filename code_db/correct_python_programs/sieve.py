def sieve(max_val):
    if max_val < 2:
        return []

    # 1. Initialize a boolean list (or array) is_prime of size max + 1, setting all entries to True.
    is_prime = [True] * (max_val + 1)

    # 2. Explicitly mark is_prime[0] and is_prime[1] as False, as 0 and 1 are not prime.
    is_prime[0] = False
    is_prime[1] = False

    # 3. Iterate p from 2 up to the square root of max_val.
    # We iterate up to int(max_val**0.5) + 1 to include the square root itself.
    for p in range(2, int(max_val**0.5) + 1):
        # 4. If is_prime[p] is True (meaning p is a prime number),
        if is_prime[p]:
            # then mark all multiples of p (starting from p*p) as False in the is_prime list.
            # That is, for i from p*p up to max_val with a step of p, set is_prime[i] = False.
            for multiple in range(p * p, max_val + 1, p):
                is_prime[multiple] = False

    # 5. Finally, iterate from 2 up to max_val and collect all numbers i for which is_prime[i] is True
    # into your primes list.
    primes = []
    for i in range(2, max_val + 1):
        if is_prime[i]:
            primes.append(i)

    return primes