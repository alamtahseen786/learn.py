'''
ques 7
  *
 ***
*****  
'''
n=int(input("enter a number: "))
for i in range(1,n+1):
    print(" "*(n-i),end="") #blank space print karne ke liye
    print("*"*(2*i-1),end="") #(2*i-1)= odd series ke liye
    print("") # new line lane ke liye
    
'''ques 8
n=3
*
**
***
'''
n=int(input("enter a number: "))
for i in range(1,n+1):
    print((n-i)*" ") #blank space print karne ke liye
    print("*"*i,end="")  
    print("")
    

'''ques 9
n=3
***
* *
***
'''
n=int(input("enter a number: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n)
    else:
        print("*"+" "*(n-2)+"*")
print("")            
