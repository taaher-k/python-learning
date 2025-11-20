#1
# 
# 
# 4. Read user inputs and create 2 separate tuples. Display only the common
#values.



user_input1 = input("enter any numbers: ")

tuple1 = tuple(user_input1.split())


user_input2 = input("enter any numbers: ")

tuple2 = tuple(user_input2.split())


comman_valuse =[x for x in set(tuple1) if x in set(tuple2)]



print(comman_valuse)
print(user_input1.split())






# Program to read user inputs, create 2 tuples, and display common values

# Step 1: Read first tuple input
tuple1_input = input("Enter elements for first tuple (separated by spaces): ")
tuple1 = tuple(tuple1_input.split())

# Step 2: Read second tuple input
tuple2_input = input("Enter elements for second tuple (separated by spaces): ")
tuple2 = tuple(tuple2_input.split())

# Step 3: Find common values
common_values = tuple(set(tuple1) & set(tuple2))   # intersection of sets

# Step 4: Display results
print("First Tuple:", tuple1)
print("Second Tuple:", tuple2)
print("Common Values:", common_values)
