numbers = [10, 20, 10, 30, 40, 20, 50, 60, 30, 70]

# Remove duplicates using set and dict()


#unique_numbers = set(numbers)
unique_numbers = list(dict.fromkeys(numbers))



print("Original list:", numbers)
print("List after removing duplicates:", unique_numbers)


print("____________________________________________________________________________");



number = [10, 20, 10, 30, 40, 20, 50, 60, 30, 70]
unique_number = []


for num in numbers:
    if num not in unique_number:
        unique_number.append(num)

print("Original list:", numbers)
print("List after removing duplicates:", unique_number)

print("____________________________________________________________________________________")



report = {"math":89,"psy":91,"che":98};

print("math:",report["math"],"\nche:",report["che"],"\npsy:",report["psy"])



print("____________________________________________________________________________________")



newtuple = (23,9,36,748,57487,4585,4874,)

print(newtuple[:4]);

#print from 23 to 748
print("________________________________________________________________________________________________")



ck_vowel = input("Enter your name: ");

converted_ck_vowel = list(ck_vowel)


vowel = ["a","e","i","o","u"];

print("vowel"if converted_ck_vowel[0].lower() in vowel else"not an vowel");



found = []

for ch in ck_vowel.lower():

    if ch in vowel and ch not in found:
     found.append(ch)

print("Vowels found:", found)

print("______________________________________________________________________________")



ta = int(input("enter any number"));


my_new_list = [12,22,36,9,87,7,]




print("found"if ta in my_new_list  else "not found");
