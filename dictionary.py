# DICTIONARY 
d={}# empty dictionary
result={
    "harry":10,
    "sandy":19,
    "naveen":20,
    "pragati":21
}

print(result)
print(type(result))
# methods
print(result.values())#returns a list of all the values in the dictionary
print(result.items())#returns a list of tuples containing key value pairs
print(result.keys())#returns a list of all the keys in the dictionary

result.update({"sandy":22})#updates the value of the key "sandy" to 22
print(result)