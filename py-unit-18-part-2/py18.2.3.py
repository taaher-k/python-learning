#3. Implement a Python script that uses both fork() and os.spawnv() to create new processes.
#Compare the behavior and output of the two methods.
#Output:
#Parent Process
#Child Process (fork)
#Child Process (spawnv)

"""
import os
import sys

def main():
    print("Parent Process")

    # --- Using fork() ---
    pid = os.fork()   # creates a child process
    if pid == 0:
        # Child process (fork)
        print("Child Process (fork)")
        sys.exit(0)
    else:
        # Parent waits for fork child
        os.wait()

    # --- Using spawnv() ---
    # os.spawnv(mode, path, args)
    # mode = os.P_WAIT → parent waits until child finishes
    # path = sys.executable → Python interpreter
    # args = [program name, script, arguments]
    os.spawnv(os.P_WAIT, sys.executable, [sys.executable, "-c", "print('Child Process (spawnv)')"])

if __name__ == "__main__":
    main()

    

import multiprocessing

def child_process():
    print("Child Process (multiprocessing)")

if __name__ == "__main__":
    print("Parent Process")
    p = multiprocessing.Process(target=child_process)
    p.start()
    p.join()

    


import os
import sys

def main():
    print("Parent Process")

    # Using spawnv to run a child process
    os.spawnv(
        os.P_WAIT, 
        sys.executable, 
        [sys.executable, "-c", "print('Child Process (spawnv)')"]
    )

if __name__ == "__main__":
    main()


    

import os
import sys
import multiprocessing

def fork_like_child():
    print("Child Process (fork)")

def main():
    print("Parent Process")

    # Simulate fork using multiprocessing (works on Windows)
    p = multiprocessing.Process(target=fork_like_child)
    p.start()
    p.join()

    # Use spawnv to launch a new Python process
    os.spawnv(
        os.P_WAIT,
        sys.executable,
        [sys.executable, "-c", "print('Child Process (spawnv)')"]
    )

if __name__ == "__main__":
    main()







"""



import os
import sys
import multiprocessing

def fork_like_child():
    print("Child Process (fork)")

def main():
    print("Parent Process")

    # Simulate fork using multiprocessing
    p = multiprocessing.Process(target=fork_like_child)
    p.start()
    p.join()

    # Use spawnv with properly escaped quotes
    os.spawnv(
        os.P_WAIT,
        sys.executable,
        [sys.executable, "-c", "print(\"'Child Process (spawnv)'\")"]
    )

if __name__ == "__main__":
    main()

