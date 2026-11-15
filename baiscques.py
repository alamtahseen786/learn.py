# ques-wap to display a user entered name followed by good afternoon using input()function

name=input('enter the name: ')
print("good afternoon",name)

# ques-wap tp fill in a letter template given below with name and date
letter='''dear <|Name|>,
         you are selected!
         <|date|>
         '''
print(letter.replace("<|Name|>","harry").replace("<|date|>","20/06/2024"))

# ques-wap to detect double spaces in a string

a="harry is a good  boy"
print(a.find("  ")) #finds the index of double space

# escape sequence
print("harry is a good boy\n he is a good\n\t student")

# spam comment
p1="make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"

message=input("enter the message: ")
if(p1 in message or p2 in message or p3 in message or p4 in message):
    print("spam")
    
else:
    print("not spam")  
    
#username contain less than 10 character or not

username=input("enter the username: ")
if(len(username)<10):
    print("username contain less than 10 character")
    
elif(len(username)>10):
    print("username contain more than 10 character")    
    
else:
   print("username contain 10 character");    
         
            
