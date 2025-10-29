# Lists in Python allows multiple datatypes

values = [23, 94, "Gilberto", False, True, 89.4]
print(values)

print(values[0])  # 23
print(values[4])  # True
print(values[-1])  # It references to last index
print(values[2])  # Gilberto
print(values[1:4])  # 94, Gilberto, False, True

# To insert values to the list need to indicate index and value to insert
values.insert(3, "Lizarraga")
print(values)

# To add values to the end of list you can use append() method
values.append("End")

# To delete an item from list use keyword del and enter index of item to delete
del values[0]

# To replace value only need to indicate to your list index
# and new value you want to enter
values[4] = True
print(values)



