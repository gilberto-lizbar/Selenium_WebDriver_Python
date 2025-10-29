# For loop is used to iterate a list of elements

list1 = [45, 23, 65, 11, 98]

# below code iterate a single list
for i in list1:
    print(i)
print("***********Get number divisible by 2****************")
# Get number divisible by 2
for i in list1:
    if i % 2 == 0:
        print(" {}, {}".format(i, "is multiple of 2"))
    else:
        print(" {}, {}".format(i, "is not multiple of 2"))

#  To iterate from one number to another number
print("***************************")
for j in range(1, 6):  # range(i, j) -> i to j-1
    print(j)
# By default, each iteration increase the count to 1,
# but you can chance the increment adding 1 more argument to range
# In below example loop start at 1 and increment 2 every iteration
# result will be 1, 3, 5
print("***************************")
for j in range(1, 6, 2):  # range(i, j) -> i to j-1
    print(j)
# If only 1 argument is entered on range it will iterate from 0 to argument
# increasing to one the variable for each iteration
print("***************************")
for i in range (10):
    print(i)

# Sum natural number from 1 to 6
sum1 = 0
for j in range(1, 6):  # range(i, j) -> i to j-1
    sum1 = sum1 + j

print(sum1)
print("****************************")
rows = 3
columns = 2
mylist = [[0 for x in range(columns)] for x in range(rows)]
for i in range(rows):
    for j in range(columns):
        mylist[i][j] = '%s,%s' % (i, j)
print(mylist)

# Considering 2-D array having 3 rows and 3 columns
n = 3
m = 3
arr = [[3, 2, 7], [2, 6, 8], [5, 1, 9]]

# Iterating over all 1-D arrays in 2-D array
for i in range(0, n):

    # Printing all elements in ith 1-D array
    for j in range(0, m):
        # Printing jth element of ith row
        print(arr[i][j], end=" ")
    print()


array2 =[[3, 34, 54],[78 ,39 , 22],[99, 55, 77]]

for i in range(0,2):# Columns
    for j in range(0,3): # Rows
        print(array2[i][j], end=" ")
    print()


print("**************************************+")



