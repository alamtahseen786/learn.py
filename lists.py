# LISTS-mutable data type

friends=["mango",7,False] #can store any data type
print(friends)
print(friends[0])
friends[0]="banana" #can change the value of a list ,mutable
friends.append("tahseen") #add an element to the end of the list
print(friends)

l1=[13,55,67,90,43]
l1.sort() #sorts the list in ascending order
print(l1)
l1.reverse() #reverses the list
print(l1)
l1.insert(3,333.3)#insert 333.3 in index 3
print(l1)
l1.pop(3)#removes the element at index 3
print(l1)