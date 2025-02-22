def countPrimes(n: int) -> list:
    # Handle vals less than 2
    if n < 2:
        return []

    # Mark all vals in range, set all numbers as potential primes
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes

    # Iterate from 2 to sqrt(n)
    for idx in range(2, int(n**0.5) + 1):
        if is_prime[idx]:
            # Mark all multiples of idx as non-prime
            for i in range(idx * idx, n, idx):
                is_prime[i] = False

    # Return the list of primes
    primes = [i for i in range(2, n) if is_prime[i]]
    return primes


# Test the function
print(countPrimes(99))  # Output should be [2, 3]
