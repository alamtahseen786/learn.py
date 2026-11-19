# FUNCTIONS-grp of statment to perform a specific task
# def avg():
#     a=int(input("ENTER YOUR NUMBER: "))
#     b=int(input("ENTER YOUR NUMBER: "))
#     c=int(input("ENTER YOUR NUMBER: "))
    
#     average=(a+b+c)/3
#     print("AVERAGE OF THREE NUMBERS IS: ",average)
    
# #Function CALL 
# avg() 


# def greet():
#     name=input("enter the name: ")
    
#     print(f" good morning {name}")
  
# greet()    

#QUES- wap to find gratest of three numbers
a=1
b=2
c=3
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
    
print(f"the gratest of all three numbers is: {greatest(a,b,c)}")  

#QUES-covert celcius to fahrenheit  
    #formula= c/5=(f-32)/9
    
def c_to_f():
    return ((c*9)/5)+32
    
    
c=int(input("ENTER THE TEMPERATURE IN CELCIUS: "))
print(c_to_f)

# QUES-print pattern using function
def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

pattern(5)    
    