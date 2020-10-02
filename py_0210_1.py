'''
Write a function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)
'''

def insert_end(a):
    return a[-2:]*4

print(insert_end('Python'))
print(insert_end('Exercises'))