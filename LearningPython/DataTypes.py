# Python datatypes: Numeric(int, long, float, complex), String, List, Tupple & Dictionary

# *****Lists******

values = [1, 2, "Gilberto", 4, 5]
# List is a datatype that allow multiple values and can be different data types
# declare a list with []

print(values)  # print all list values
print(values[0])  # 1
print(values[3])  # 4
print(values[-1])  # 5 ,last value of list
print(values[1:3])  # 2, "Gilberto"
values.insert(5, "Lizarraga")  # Insert a String value in the given position 5
values.insert(0, "start")
print(values)
values.append("end")  # Add the value "end" to the end of the list
print(values)

values[3] = "GILBERTO"
print(values)
del values[2]
print(values)

# *****Tuples******
# Same as list datatype, but it is immutable declare a tuple with ()
val = (1, 2, "name", 3)
print(val[3])
print(f"text: {val[2]}")
print(f"text: {val}")

#val[3] = "new" #uncomment to check the error for tuples

# *****Dictionaries******

dict1 = {1: "azul", 2: "rojo", "color": 1}

print(dict1[1])
print(dict1["color"])
print(type(dict1))

# declare empty dictionary
dict2 = {}
print(dict2)
# add values to dictionary
dict2[10] = "hello"
dict2["green"] = 5

print(dict2[10])
print(dict2)

