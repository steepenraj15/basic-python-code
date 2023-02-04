
#python #index #indexing

# index operator [] = gives access to a sequence’s element (str,list,tuples)

name = "steepen RAJ!"

'''
if(name[0].isupper()):
   name = name.lower()
print(name)  
'''

first_name = name[:7].upper()
last_name = name[8:-1].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)
