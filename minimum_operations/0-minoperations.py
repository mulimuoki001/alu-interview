#!/usr/bin/python3
def minOperations(n):
    if n == 1:
        return 0

    operations = 0
    factors = []
    i = 2

    # Find the prime factors of n
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    # Calculate the sum of prime factors
    for factor in factors:
        operations += factor

    return operations


# Example usage
n = 9
result = minOperations(n)
print("Number of operations:", result)
