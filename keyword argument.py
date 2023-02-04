
#python #keyword #arguments

# keyword arguments =   arguments preceded by an identifier when we pass them to a function. The order of the arguments doesn't matter, unlike positional arguments. Python knows the names of the arguments that a function receive


def hello(first, last, middle):
    print("Hello " + first + " " + middle + " " + last)


hello(last="D",first="Steepen",middle="Raj")
