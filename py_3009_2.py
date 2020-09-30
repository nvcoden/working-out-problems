'''
Steve has a string of lowercase characters in range ascii[["a".."z"]]. 
He wants to reduce the string to its shortest length by doing a series of operations. 
In each operation, he selects a pair of adjacent lowercase letters that match, and he deletes them. 
For instance, the string aab could be shortened to b in one operation.

Steve’s task is to delete as many characters as possible using this method and print the resulting string. 
If the final string is empty, return Empty String.
'''
import sys
from io import StringIO
sys.stdin = StringIO('''cccxllyyyy''')
def super_reduced_string(a):
    b = set(a) 
    for i in b:
        a = a.replace(i*2, '')
    if a=='':
        return 'Empty String'
    else:
        return a

string = input()
print(super_reduced_string(string))