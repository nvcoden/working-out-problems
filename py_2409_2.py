'''
Create a function that will build a staircase using the underscore _ and hash # symbols. 
A positive value denotes the staircase's upward direction and downwards for a negative value.
'''
def staricase_maker(n):
    a = ""
    if n>0:
        for i in range(1, n+1):
            a+=('_'*(n-i)+'#'*i)+"\n"
    if n<0:
        n = -n
        for i in range(n):
            a+=('_'*i+'#'*(n-i))+"\n"
    return(a)


n = int(input("Enter the no of stairs\n"))
print(staricase_maker(n))