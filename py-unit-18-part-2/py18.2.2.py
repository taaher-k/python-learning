#Write a Python program that demonstrates inter-process communication using pipes. Create

#two processes; one process sends a message through the pipe, and the other process

#receives and prints the message.

#Output:Message sent: Hello from process 1

#Message received: Hello from process 1



import multiprocessing

# Function for process 1: send a message
def sender(conn):
    message = "Hello from process 1"
    print("Message sent:", message)
    conn.send(message)   # send message through pipe
    conn.close()

# Function for process 2: receive a message
def receiver(conn):
    message = conn.recv()   # receive message from pipe
    print("Message received:", message)

if __name__ == "__main__":
    # Create a pipe
    parent_conn, child_conn = multiprocessing.Pipe()

    # Create two processes
    p1 = multiprocessing.Process(target=sender, args=(parent_conn,))
    p2 = multiprocessing.Process(target=receiver, args=(child_conn,))

    # Start processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()


