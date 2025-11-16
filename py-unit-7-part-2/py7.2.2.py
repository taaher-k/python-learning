#2. Program to print hollow rectangle or square star patterns


#1 mid

rows = 5
cols = 7

for i in range(rows):
    for j in range(cols):
        # Print * for first/last row OR first/last column
        #if i == 0 or i == rows-1 or j == 0 or j == cols-1:
        if i==0 or i == rows-1 or j ==0 or j == cols -1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#2 is basic

for i in range (1,6):
    for j in range (1,6):
        print("*" if i==1 or i == 5 or j ==1 or j == 5 else " ",end=" " )
    print()    
