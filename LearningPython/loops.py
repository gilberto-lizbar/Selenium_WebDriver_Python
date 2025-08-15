greeting = "Good Morning"

if greeting == "Morning":
    print(" Condition Matches")
    print("second line")
else:
    print("condition do not match")

print("if else condition is completed")

# *******+for loops*********

# iterate all elments of a list
obj = [2, 3, 4, 5, 6, 7, 8]
for i in obj:
    print(i)
# print only multiples of 2
for i in obj:
    print(i*2)

# iterate in a range of list items
for j in range(1, 6):
    print(j)

sum1 = 0
# iterate in a range
for j in range(1, 6):
    sum1 = sum1 + j
print(sum1)

# iterate in a range and sum a value each iteration
# if the range is equal to (1, 6, 2) it means loop will increase 2 to
# value of k and the result will be 1, 3 and 5
for k in range(1, 6, 2):
    print(k)

# start from 0 to 9
for m in range(10):
    print(m)


# ******************* While loops *************
# Iterate while the condition is true
it = 4
while it > 1:
    print(it)
    it = it - 1
print("while loop execution is done")

it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue  # Stop the current iteration and continue with next one
    if it == 3:
        break
    print(it)

    it = it - 1


