#3

#1


def fibonacci_upto(limit):
    a, b = 0, 1
    fib_list = []
    while a <= limit:
        fib_list.append(a)
        a, b = b, a + b   # update values
    
    p = len(fib_list)-1

    if fib_list[p]==limit:
            return "its a fibonacci"
    else:
            return "not a fibonacci"


num = int(input("enter any number to check its fibonacci or not"))
print(fibonacci_upto(num))



#2
def fibonacci_upto(limit):
    a, b = 0, 1
    fib_list = []
    while a <= limit:
        fib_list.append(a)
        a, b = b, a + b   # update values
    
    if limit in fib_list:   # check membership in the whole list
        return "its a fibonacci"
    else:
        return "not a fibonacci"

num = int(input("enter any number to check its fibonacci or not: "))
print(fibonacci_upto(num))



