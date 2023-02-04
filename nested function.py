
#python #nested #functions

# nested functions calls =  function calls inside other function calls
#                           innermost function calls are resolved first
#                           returned value is used as argument for the next outer function


# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num) 				-0565.5 turn into 565.5 by abs 
# num = round(num) 				 565.5 turn into 565 by round
# print(num)

print(round(abs(float(input("Enter the value: ")))))

'''
output:
Enter the value: -0565.5
566
'''