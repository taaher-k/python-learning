""""




#3.2==1

for x in range (0,51):
      if x % 3==0 and x % 5==0:
            print("Accord info matrix")
      elif x % 5==0:
            print("info matrix")

      elif x % 3==0 :
            print("Accord")

      else:
            print(x)
    

            


#3.2==2

 
 # Read input from user


num = int(input("Enter a number: "))

print(f"Divisors of {num} are:")


# Loop through all numbers from 1 to num


for i in range(1, num + 1):
    if num % i == 0:
        print(i)


#3.2.3



mul = int(input("Enter the Number for tables"))


tabels =''   

for t in range(1,12 +1):
        tabels = mul*t
        print(f'{mul} x {t} = {tabels}')


for y in range(1, 1000 +1):
      mul = y
      tabels =''   
      for t in range(1,12 +1):
         tabels = mul*t
         print(f'{mul} x {t} = {tabels}')


#3.2.4

mulnum = int(input("Enter a number greater than 1000: "))

sepnum = mulnum  # This line is redundant unless you're planning to use sepnum separately

print(mulnum)



print("Value is", mulnum, sep=": ")
# Output: Value is: 1234
"""


mulnum = int(input("Enter a number greater than 1000: "))

print("Digits separated by '.':", end=' ')
print(*str(mulnum), sep='.')



j = 12365486359535
print(*str(j), sep='.')


j = 12365486359535

print(*str(j))


j = 1234
o = [*str(j)]
print(o) 



f = []

for q in range(1, 31):
    if q % 2 != 0:
        f.append(q)
        print(list(reversed(f)))


f = [q for q in range(1, 31) if q % 2 != 0]
print(list(reversed(f)))

labels =  [f"Odd-{q}" for q in range(1, 11) if q % 2 != 0]
# Output: ['Odd-1', 'Odd-3', 'Odd-5', 'Odd-7', 'Odd-9']
print(labels)


num = int(input("Enter a number: "))

# Separate and display each digit
for digit in str(num):
    print(digit)

for num in range(29, 0, -2):
    print(num)


odd_numbers = [num for num in range(29, 0, -2)]
print(odd_numbers)


for num in range(29, 0, -1):
    if num%2!=0:
     print(num)