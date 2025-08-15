print("hello")

# here are the comments

a = 3
print(a)

Str = "Text"
print(Str)

# declare multiple variables

a, b, c = 5, 6.5, "moretext"

# concatenate
# print("value "+b) #TypeError: can only concatenate str (not "float") to str
print("value" + c)
print("{} {}".format("values of b ", b))

# know data types of a variable
print(type(c))
print(type(b))
print(type(a))


age = 25
height = 5.9
favorite_color = "blue"

print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Favorite Color:", favorite_color, "| Type:", type(favorite_color))


print("value of a", a, "value of b", b, "value of c", c)


fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Print the first and last elements
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Slicing to print the second and third fruits
print(f"Fruits from index 1 to 2: {fruits[1:3]}")
