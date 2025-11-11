#Write a Python program using a generator function to generate Fibonacci
#numbers up to a given number n




#1

def fibonacci_up_to(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# Example usage
limit = 100
print(f"Fibonacci numbers up to {limit}:")
for num in fibonacci_up_to(limit):
    print(num, end=" ")
