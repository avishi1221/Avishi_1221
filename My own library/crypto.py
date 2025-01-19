def mod_exp(base, exp, mod):
    """Computes (base^exp) % mod efficiently using modular exponentiation."""
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def gcd(a, b):
    """Finds the greatest common divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

