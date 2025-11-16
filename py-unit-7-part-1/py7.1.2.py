
#2. From given list, display only prime numbers.


#1


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # check divisors up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Example list
numbers = [10, 15, 17, 23, 28, 31, 40, 41]

# Filter primes
prime_numbers = [n for n in numbers if is_prime(n)]

print("Prime numbers from the list:", prime_numbers)


