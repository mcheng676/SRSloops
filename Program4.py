'''
***PROGRAM 4***
The program below is supposed to prompt the user to enter an integer, and then print all the factorial numbers up to that number factorial. However, if you run the program as written, there is a bug (run the code as written to see what the bug is). Fix the code so that it runs the way it should.

(Note: if you're familiar with the math module, you may use that, but it's highly unnecessary with what's already provided below.)

An example of what should appear when this code runs:

How many numbers?  5
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
'''
num = int(input("How many numbers? "))
factorial = 1
for i in range(num):
    factorial *= i
    print(str(i) + '! =', factorial)
