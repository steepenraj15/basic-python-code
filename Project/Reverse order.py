def reverse_string(s):
    if len(s) == 0:
        return
    else:
        reverse_string(s[1:])
        print(s[0])

s = input("Enter a string: ")
reverse_string(s)
