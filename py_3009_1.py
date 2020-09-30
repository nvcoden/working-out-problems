'''
A quadratic equation a x² + b x + c = 0 has either 0, 1, or 2 distinct solutions for real values of x. 
Given a, b and c, you should return the number of solutions to the equation.
'''

def solution (a,b,c):
    eqn = b**2-(2*a*c)
    if eqn>0:
        return 2
    elif eqn == 0:
        return 1
    else:
        return 0

a,b,c = map(int, input().split())
print(solution(a,b,c))
