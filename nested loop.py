
#python #nested #loops

# nested loops =    The "inner loop" will finish all of it's iterations before
#                   finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns): 			# default print statement will print every output in new line
        print(symbol, end="") 			# end="" is used to prevent the output in new line
    print()