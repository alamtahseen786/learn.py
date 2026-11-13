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
         
            
