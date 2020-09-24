'''
Question 1
Create methods for the Calculator class that can do the following:
1. Add two numbers.
2. Subtract two numbers.
3. Multiply two numbers.
4. Divide two numbers.

Sample Output :-
calculator = Calculator()

calculator.add(10, 5) ➞ 15

calculator.subtract(10, 5) ➞ 5

calculator.multiply(10, 5) ➞ 50

calculator.divide(10, 5) ➞ 2
'''

class Calculator:
    def add(i,j):
        return i+j
    
    def subtract(i,j):
        return i-j

    def multiply(i,j):
        return i*j

    def divide(i,j):
        return i/j

i = int(input("Enter the First no\n"))
j = int(input("Enter the Second no\n"))
print(Calculator.add(i,j))
print(Calculator.subtract(i,j))
print(Calculator.multiply(i,j))
print(Calculator.divide(i,j))


