'''
NT : I was taking some time off coding for some days, and it was refreshing....back to it then.



Given two numbers, return true if the sum of both numbers is less than 100. Otherwise return false.
'''
def lessThan100(a,b):
    return True if a+b<=100 else False

print(lessThan100(22, 15)) # true
print(lessThan100(83, 34)) # false
print(lessThan100(3, 77)) # true