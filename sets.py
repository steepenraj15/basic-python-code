
#python #sets #set

#set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#dishes.update(utensils)
#dinner_table = utensils.union(dishes)

print(dishes.difference(utensils))
print(utensils.intersection(dishes))

for x in utensils:
    print(x)

'''
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is unordered, unchangeable*, and unindexed.
'''