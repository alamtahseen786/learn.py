# RECURSION-it directly use a mathematical formula as a function
'''
factorial(1)=1
factorial(2)=2 X 1 
factorial(3)=3 X 2 X 1
factorial(4)= 4 X 3 X 2 X 1
factorial(5)=5 X 4 X 3 X 2 X 1

FACTORIAL OF N= N X FACTORIAL OF (N-1)'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n*factorial(n-1)

n=int(input("ENTER THE NUMBER: "))
print(f"the factorial  of {n} is:{factorial(n)} ")
