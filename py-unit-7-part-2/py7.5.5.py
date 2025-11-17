#5. Pyramid shape pattern



rows = 5

for i in range(1, rows+1):                 # Outer loop → controls rows
    # Print spaces before stars
    for j in range(rows-i):
        print(" ", end=" ")
    
    # Print stars
    for k in range(2*i-1):
        print("*", end=" ")
    
    print()                                # Move to next line




#2


for i in range(1,10):
    for j in range (i,10):
        print(" ",end=" ")
    for k in range(1,i+1):
        print (" * ",end=" " )
    print()       


    