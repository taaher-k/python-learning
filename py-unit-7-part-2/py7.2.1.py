#1. Zeros/ ones Pattern Programs



#1

def zero_one_pattern(rows):
    for i in range(1, rows+1):
        pattern = ""
        for j in range(1, i+1):
            if j % 2 == 1:   # odd position → 1
                pattern += "1"
            else:            # even position → 0
                pattern += " 0 "
        print(pattern)

# Example: 5 rows
zero_one_pattern(5)


#2


for i in range (1,6):
    for j in range(1,i+1):
        print("1" if j % 2 !=0 else "0",end=" ")

    print()
