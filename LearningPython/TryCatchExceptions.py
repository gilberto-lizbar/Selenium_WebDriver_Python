# try, except (catch)
try:
    with open("test2.txt", "r") as reader:
        reader.read()
# Exception with customized message
except:
    print("There is an exception on the file name it does not exists but program"
          " is not stopped because exception is catch")
# Exception base class, 'e' allows you to access information about the exception,
# such as its message or other attributes
try:
    with open("test2.txt", "r") as reader:
        reader.read()
except Exception as e:
    print(e)

# Run finally block in try exception block it will send the msg even if there is no exception
# Finally is always executed
try:
    with open("test.txt", "r") as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("testing finally block is printed even if no exception exist")

# send the exception and stop the program
with open("test2.txt", "r") as reader:
    reader.read()
