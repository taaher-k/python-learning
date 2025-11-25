#Write a program to print numbers from 1 to 50 using two threads. One thread print all

#prime number , and the other thread print all even numbers.



import threading

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Thread function to print prime numbers
def print_primes():
    print("\nPrime numbers from 1 to 50:")
    for num in range(1, 51):
        if is_prime(num):
            print(num, end=" ")
    print()

# Thread function to print even numbers
def print_evens():
    print("\nEven numbers from 1 to 50:")
    for num in range(1, 51):
        if num % 2 == 0:
            print(num, end=" ")
    print()

# --- Main Program ---
t1 = threading.Thread(target=print_primes)
t2 = threading.Thread(target=print_evens)

# Start both threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("\nBoth threads finished execution.")

