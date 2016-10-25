
def trial_division(n):
    """Return a list of the prime factors for a natural number."""
    if n < 2:
        return []
    prime_factors = []
    for p in prime_sieve(int(n**0.5)):
        if p*p > n: break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1:
        prime_factors.append(n)
    return prime_factors

print trial_division(77)
