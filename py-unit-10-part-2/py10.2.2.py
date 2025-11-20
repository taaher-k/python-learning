#1


##each student’s details are stored in a nested dictionary. Example:
#○ priya: {&quot;age&quot;: 20, &quot;dept&quot;: &quot;Computer Science&quot;, &quot;gpa&quot;: 3.9}
#○ sam: {&quot;age&quot;: 22, &quot;dept&quot;: &quot;Mathematics&quot;, &quot;gpa&quot;: 3.8}
#Access the GPA of sam and print it.


# Step 1: Create nested dictionary
students = {
    "priya": {"age": 20, "dept": "Computer Science", "gpa": 3.9},
    "sam": {"age": 22, "dept": "Mathematics", "gpa": 3.8},
    "rahul": {"age": 21, "dept": "Physics", "gpa": 3.7},
    "anita": {"age": 23, "dept": "Chemistry", "gpa": 3.6},
    "vijay": {"age": 20, "dept": "Biology", "gpa": 3.5}
}

# Step 2: Access GPA of sam
print("Sam's GPA:", students["sam"]["gpa"])
