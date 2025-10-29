# This datatype work similar than List datatype with the different it is immutable
# once it is declared does not allow to modify, delete or add new items

# it is declared with parenthesis () instead brackets []
values = (22, 45, "Gilberto", True, 12.3)
# values[0] = 33 #Uncomment this line see an error tuple does not support item assigment
#values.insert(1, "87") #Uncomment this line see 'tuple' object has no attribute 'insert'
# del values[0] #Uncomment this line see tuple doesn't support item deletion
print(values)
