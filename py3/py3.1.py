"""


#3.1 ===1




# Input marks
English = int(input("Marks in English: "))
Tamil = int(input("Marks in Tamil: "))
Maths = int(input("Marks in Maths: "))
Science = int(input("Marks in Science: "))
Social = int(input("Marks in Social: "))

# Calculate total and average
TotalMarks = English + Tamil + Maths + Science + Social
TotalAverage = TotalMarks / 5

# Check percentage using match-case

def check_percentage(x):
    match x:
        case x if x >= 75:
            print("Distinction.")
        case x if x >= 60:
            print("First Class.")
        case x if x >= 50:
            print("Second Class.")
        case x if x < 50:
            print("Fail.")
        case _:
            print("Invalid entry.")

# Output
print(f"\nTotal Marks: {TotalMarks}")
print(f"Percentage: {TotalAverage:.2f}")
check_percentage(TotalAverage)


print("________________________________________________________________________________________")




#3.1===2



EB_Amount = int(input("Enter the EB Bill Amount:  "))

EB_Bill = ""


def Check_EB_Bill_Amount(x):
    match x:
        case x if x <= 100:
            print(f"Free.")


        case x if x > 100 and x <= 200:
            EB_Bill= EB_Amount * 0.80
            print(f"EB Bill:  {EB_Bill}" )


        case x if x > 200 and x <= 300:
            EB_Bill= EB_Amount * 1
            print(f"EB Bill:  {EB_Bill}" )

        case x if x > 300 and x <= 400:
            EB_Bill= EB_Amount * 1.20
            print(f"EB Bill:  {EB_Bill}" )

        case x if x > 400:
            EB_Bill= EB_Amount * 2
            print(f"EB Bill:  {EB_Bill}" )

        case _:
            print(f"Please enter the valid amount" )

Check_EB_Bill_Amount(EB_Amount)


#3.1====3



print("_____________________________________________________________________________________________________")


div24 = int(input("enter the number:  "))


print("divisible by 2 but not by 4." if div24 % 2==0 and div24 % 4!=0 else "Does not meet the condition.")

print("_____________________________________________________________________________________________________")

#3.1 = = = 4

numpn = int(input("enter the number:  "))


print("negative" if numpn < 0  else "positive.")

print("_____________________________________________________________________________________________________")

"""
#3.1 = == 5
# Input: three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Nested if logic
if a > b:
    if a > c:
        print("The largest number is:", a)
    else:
        print("The largest number is:", c)
else:
    if b > c:
        print("The largest number is:", b)
    else:
        print("The largest number is:", c)


print("________________________________________________________________________________________________")


