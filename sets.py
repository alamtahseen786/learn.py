# SETS

s={1,2,3,4,5,"radhika"}
print(s)
print(type(s))

#methods
s.add(333) #add elemntto the last
print(s)

new_set=s.copy()
print(new_set)

set1={1,2,3,4,5}
set2={4,5,6,7,8}

print(set1.union(set2))#returns a new set with all the elements from both sets

print(set1.difference(set2))#returns a new set with all the elements from set1 that are not in set2

set1.difference_update(set2)#removes all the elements from set1 that are also in set2
print(set1)