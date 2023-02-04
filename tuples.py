#python #tuples #tutorial


# tuple =   collection which is ordered and unchangeable
#                used to group together related data

student = ("Bro",21,"male")

print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")
    
'''
A tuple is created by placing all the items (elements) inside parentheses () , separated by commas. The parentheses are optional, however, it is a good practice to use them. A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).
'''