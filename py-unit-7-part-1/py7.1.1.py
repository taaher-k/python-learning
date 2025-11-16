#1. Check if given number is Niven number or not.



def is_niven(n):
    
    digit_sum = sum(int(d) for d in str(n))
    if n % digit_sum == 0:   # divisible check
        return True
    else:
        return False

print(is_niven(18))  # True
print(is_niven(15))  # False

