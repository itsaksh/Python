def is_prime(number):
    """Return True if number is prime, else False."""
    if number < 2:                      # 0, 1 and negatives are never prime
        return False
    # check divisors 2 .. floor(sqrt(n)) INCLUSIVE
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False                # first factor found -> stop at once
    return True
 
 
def generate_primes(start, end):
    """Return all primes in the inclusive range [start, end]."""
    primes = []
    for number in range(start, end + 1):     # +1 makes 'end' inclusive
        if is_prime(number):
            primes.append(number)
    return primes
 
 
print("generate_primes(1, 30)  :", generate_primes(1, 30))
print("generate_primes(2, 2)   :", generate_primes(2, 2))
print("generate_primes(14, 16) :", generate_primes(14, 16))
# additional edge cases
print("generate_primes(23, 29) :", generate_primes(23, 29))
print("generate_primes(-5, 1)  :", generate_primes(-5, 1))
print("generate_primes(49, 49) :", generate_primes(49, 49))
