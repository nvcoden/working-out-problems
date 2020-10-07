'''Create a function that takes a string and returns true or false depending on whether or not the formula is correct.'''

######UNFINISHED

def formula(string):
    if string != '': 
        return eval(string[0:string.index('=')])==eval(string[string.index('=')+1:])
    else: 
        return 0
    



print(formula("6 * 4 = 24"))
print(formula("18 / 17 = 2"))
print(formula(""))