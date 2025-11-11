#Write a Python program using a generator function to generate Fibonacci
#numbers up to a given number n




#1
"""
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
"""



def generater_fun_fibo(x):
    a,b = 0,1
    while a <= x:
        yield a
        a,b = b,a+b


limit = 100
print(f"im printing fibona sec to the given limit:{limit}")
for num in generater_fun_fibo(limit):

    print(num,end=" ")


