# There are 5 datatype python provides: Numeric(int, long, float, complex),
# String, List, Tuple, Dictionary

Str = "Hello World"
print(Str)

# Declaring multiple variable type and values in 1 line
b, c, d, e = 12, False, 34.5, "content"
print(c)
print(d)
# Python does not allow concat a String with an integer or double using +
# print(e + (b + d))

# Concat with + simbol is only allowed for String data type
print(e+" some text"+" more text")
# to concat different data types we open and close brackets{} for each data type and use
# function format (arg0, arg1)
print("{} {}".format(e, b+d))
# To know any data type use the function type
print(type(b))
print(type(b), type(c), type(d), type(e))


