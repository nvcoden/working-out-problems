'''Given a sorted array of numbers, remove any numbers that are divisible by 13. Return the amended array.
'''

def unlucky_13(arr):
    return list(i for i in arr if i%13!=0)
    
print(unlucky_13([53, 182, 435, 591, 637]))
print(unlucky_13([24, 316, 393, 458, 1279]))
print(unlucky_13([104,351,455,806,871]))