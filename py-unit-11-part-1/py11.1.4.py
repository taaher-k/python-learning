#Create class named Student. Write methods to read marks as input and
#return total as output. Another method to take total and number of subject
#as input and return average.



class Student:
    def __init__(self):
        self.marks = []

    # Method to read marks and return total
    def readMarks(self):
        n = int(input("Enter number of subjects: "))
        total = 0
        for i in range(n):
            mark = float(input(f"Enter mark for subject {i+1}: "))
            self.marks.append(mark)
            total+=mark
        return total

    # Method to calculate average
    def calculateAverage(self, total, num_subjects):
        average = total / num_subjects
        return average


# --- Program Execution ---
s1 = Student()
total_marks = s1.readMarks()
num_subjects = len(s1.marks)
average = s1.calculateAverage(total_marks, num_subjects)

print("Total Marks:", total_marks)
print("Average Marks:", average)

#2



class Student:
    def __init__(self):
        self.marks = []
        n = int(input("Enter number of subjects: "))
        
        total = 0
        for i in range(n):
            mark = float(input(f"Enter mark for subject {i+1}: "))
            self.marks.append(mark)
            total += mark
        
        self.total = total
        self.average = total / n

        # Display results immediately
        print("Total Marks:", self.total)
        print("Average Marks:", self.average)


# --- Program Execution ---
s1 = Student()








#3




"""


class Student:
    def __init__(self):
        self.marks = []

    # Method to read marks and return total
    def readMarks(self):
        n = int(input("Enter number of subjects: "))
        for i in range(n):
            mark = float(input(f"Enter mark for subject {i+1}: "))
            self.marks.append(mark)
        total = sum(self.marks)
        return total

    # Method to calculate average
    def calculateAverage(self, total, num_subjects):
        average = total / num_subjects
        return average


# --- Program Execution ---
s1 = Student()
total_marks = s1.readMarks()
num_subjects = len(s1.marks)
average = s1.calculateAverage(total_marks, num_subjects)

print("Total Marks:", total_marks)
print("Average Marks:", average)

"""