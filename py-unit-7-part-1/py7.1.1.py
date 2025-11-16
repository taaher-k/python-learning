#1. Check if given number is Niven number or not.



def is_niven(n):

        digit_sum = sum(int(d) for d in str(n))
        if n % digit_sum == 0:   # divisible check
         return True
        else:
         return False

print(is_niven(18))  # True
print(is_niven(15))  # False


#2




def niven(number):
        c = 0
        
        for i in str(number):

            c+=(int(i))

        if number %  c == 0:
                return "its a niven number: "
        else:
                return "its not a niven number"  

number = int(input("enter the number to check its an niven number: "))
print(niven(number))






#these are three formates to convert a string list into a int of sum



numbers = ["10", "20", "30", "40"]
total = sum(map(int, numbers))
print(total)   # 100


#2
numbers = ["10", "20", "30", "40"]
total = sum([int(x) for x in numbers])
print(total)   # 100

#3

numbers = ["10", "20", "30", "40"]
total = 0
for x in numbers:
    total += int(x)
print(total)   # 100


