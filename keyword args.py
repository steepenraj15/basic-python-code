
#python #kwargs #tutorial

# **kwargs =   parameter that will pack all arguments into a dictionary
#                        useful so that a function can accept a varying amount of        
#                        keyword arguments

def hello(**raj):
    print("Hello " + raj['first'] + " " + raj['last'])
    print("Hello",end=" ") 								#  ,end=" "  is used to print the output in single line
    for key,value in raj.items(): 						#			otherwise it print output in seperate separete line
        print(value,end=" ")


hello(title="Mr.",first="Bro",middle="Dude",last="Code")