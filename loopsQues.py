# LOOPS

# Q1-wap to print table of a given number using for loop
n=int(input("enter a number: "))

for i in range(1,11):
    print(f"{n} X {i}={n*i}")
    
#Q2-wap to greet all the person names stored in listen ,starts with S
l=["harry","soham","sachin","rahul"]

for name in l:
    if(name.startswith("s")):
        print(f"hello {name}")

#Q3-attempt 1 using while loop
n=int(input("enter a number: "))
i=1
while(i<11):
    print(f"{n} X {i}={n*i}")
    i+=1 
    
#Q4-wap to find whether a number is prime or not
n=int(input("enter a number: "))

for i in range(1,n):
    if(n%1)==0:
        print(f"{n} is a prime number")
    break    
else:
    print(f"{n} is not  a prime number")
    
#Q5-wap to find the sum of first n natural numbers using while loop
n=int(input("enter a number: "))
i=1
sum=0
while(i<=n):
    sum+=1
    i+=1
    
print(sum)    

#Q6-wap to find the factorial of a given number using for loop
n=int(input("enter a number: "))
fact = 1
for i in range(1,n+1): #kyuki range jata hai n-1 tk to apn ko n tk leke jana haiato n+1 likhenge
    fact=fact*i
    
print(f"factorial of {n} is {fact}")    