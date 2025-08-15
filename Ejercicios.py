

a = 4
b, c, d = 2.3, "John", True

print(a)
print("{}{}{}{}{}{}".format("printed values : ", b, " ", c, " ", d))

values = []

values.insert(0, "Apple")
values.insert(1, "Orange")
values.append("Grapes")
values.append("another")
del values[3]

print(values[-1])
print(values)
print(values[0:2])

list2 = ["Text", 3, False, 6.5]

print(list2)
print(type(list2[0]))
print(type(list2[1]))
print(type(list2[2]))
print(type(list2[3]))

for i in list2:
    print(i)

for j in range(2,5):
    print(j)

matrix = [[3, 2, 7], [2, 6, 8]]

for i in matrix:
    print(i)

for i in range(0,2):# Columns
    for j in range(0,3): # Rows
        print(matrix[i][j], end=" ")
    print()

matrix2 = [["blue", "red", "green", "white"], ["solid", "light", "dark", "soft"]]

for i in range(0,2):
    print("{}{}".format("Column ", i))
    for j in range(0,4):
        print("{}{}{}{}{}{}".format("[", i, "][", j, "] = ", matrix2[i][j]))

# Dictionary
myDic = {1: "Name", 2: "Last Name", "Color": "Red"}

print(myDic[1])
print(myDic[2])
print(myDic["Color"])

i = 5
while i > 1:
    print(i)
    i = i - 1

for i in range(1,51):
    if i % 2 == 0:
        print(" {}, {}".format(i, "is multiple of 2"))
    else:
        print(" {}, {}".format(i, "is not multiple of 2"))





