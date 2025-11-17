#3Printing Floyd’s triangle pattern



n=1

for i in range (1,5):
    for j in range (1,i+1):
        print(n,end=" ")
        n+=1
    print()    



#2

rows = 5
num = 1   # starting number

for i in range(1, rows+1):          # Outer loop → rows
    for j in range(1, i+1):         # Inner loop → columns
        print(num, end=" ")         # Print current number
        num += 1                    # Increment number
    print()                         # Move to next line
