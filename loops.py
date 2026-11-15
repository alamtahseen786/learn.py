#LOOPS

    # while loop
i=0
while(i<=100):
    print(i)
    i+=1
    
# wap to print content of the list using while loops  
    
l=[1,"tahseen","alam",False,"yes"]
j=0
while(i<len(l)):
    print(l[i])
    i+=1
    
    # for loops
for n in range(4): #range function 0 to n-1 tk print krke deta hai
    print(n)    
    
        # for loop with lists
l1=[1,4,6,657,66]
for h in l:
    print(h)      
    
        # for loop with tuples
t=(2,5,6,7)
for i in t:
    print(i)  
    
    
    # for loop with else
    
l2=[1,2,3,4,5]
for item in l2:
    print(item)
else:
    print("Loop completed successfully")
    
    # break and continue
    
for i in range(100):
    if(i==34):
        break #exit the loop when i=34
    print(i)
    
for i in range(100):
    if(i==34):
        continue #skip this iteration and continue with next iteration
    print(i)
        
        