str1 = "Doing exercises for practice"
str2 = "and"
str3 = "learning"

print(str1[1])  # o
print(str1[0:5])  # Doing
# Concatenation
print(str1 + str2 + str3)  # Doing exercises for practiceandlearning
print(f"{str1} {str2} {str3}")  # Doing exercises for practice and learning
print(f"text equals to: {str1} {str2} {str3}")  # text equals to: Doing exercises for practice and learning
print("{} {} {}".format(str1, str2, str3))  # Doing exercises for practice and learning
print("{} {} {} {}".format("first text", str1, str2, str3))  # first text Doing exercises for practice and learning

# Check a String is present in another String
print(str1 in str2)  # False
print("Doing" in str1)  # True
# Split separate Strings
spl1 = "This.string.was.given.for.test_verify_split_is_done another check"
spldot = spl1.split(".")
print(spldot)
print(spldot[0])
splunderscore = spl1.split("_")
print(splunderscore)
print(splunderscore[1])
splblankspaces = spl1.split(" ")
print(splblankspaces)
print(splblankspaces[1])

# remove white spaces from beginning and to the end 'trim'
str10 = " validate strip in python "
print(str10.strip())  # remove blank spaces from beginning and to the end
print(str10.lstrip())  # remove blank spaces to the left
print(str10.rstrip())  # remove blank spaces to the right



