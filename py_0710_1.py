'''
Create a function that returns true if a string contains any spaces.
'''
def hasSpaces (string):
    return ' ' in string

print(hasSpaces("hello"))
print(hasSpaces("hello, world"))
print(hasSpaces(" "))
print(hasSpaces(""))
print(hasSpaces(",./!@#"))