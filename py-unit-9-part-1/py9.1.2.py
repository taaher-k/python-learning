#2Write a Python program that creates a new directory named pythonPrograms using the
#mkdir shell command via the subprocess.run() method.



import subprocess

def main():
    try:
        # Run the mkdir shell command
        subprocess.run(["mkdir", "pythonPrograms"], check=True)
        print("Directory 'pythonPrograms' created successfully.")
    except subprocess.CalledProcessError:
        print("Error: Failed to create directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
