'''
Write a function that takes an integer i and returns a string 
with the integer backwards followed by the original integer.
'''

def ReverseAndNot(num):
    
    num = str(num)
    return (num[::-1]+num)


print(ReverseAndNot(123))# "321123"
print(ReverseAndNot(152)) # "251152"
print(ReverseAndNot(123456789))# "987654321123456789"