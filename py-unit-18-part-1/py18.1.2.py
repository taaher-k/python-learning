#2. Write a Python program using the threading module to create two threads.
#One thread increments a counter, and the other thread prints the counter value.
#Use a lock to synchronize access to the counter.
#Output:
#Counter value: 1
#Counter value: 2
#Counter value: 3


import threading
import time

# Shared counter
counter = 0
# Lock to synchronize access
lock = threading.Lock()

# Thread function to increment the counter
def increment_counter():
    global counter
    for _ in range(3):  # increment 3 times
        with lock:  # acquire lock before modifying
            counter += 1
        time.sleep(0.1)  # small delay to simulate work

# Thread function to print the counter value
def print_counter():
    global counter
    for _ in range(3):  # print 3 times
        with lock:  # acquire lock before reading
            print(f"Counter value: {counter}")
        time.sleep(0.1)  # small delay to simulate work

# --- Main Program ---
t1 = threading.Thread(target=increment_counter)
t2 = threading.Thread(target=print_counter)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("\nBoth threads finished execution.")
