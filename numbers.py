def even(list):
    evennymberlist = [i for i in list if i%2 ==0 ]
    return evennymberlist


def its_prime(n):
    if n <= 1:
        return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True


def prime(list):
    primenymberlist = [i for i in list if its_prime(i) ]
    return primenymberlist