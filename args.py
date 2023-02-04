
#python #args #tutorial

# *args =   parameter that will pack all arguments into a tuple
#                 useful so that a function can accept a varying amount of arguments

#def add(*args):
def add(*steepen):
    sum = 0
    steepen = list(steepen)
    for i in steepen:
        sum += i
    return sum

print(add(1,2,3,4,5,6,7,8))
