class Calculator:
# Classes are user defined blueprint prototype
# sum, multiplication, addition, constant
# class, contains, methods, class variables, instance variables, constructor etc
# self keyword is mandatory for calling variables names into methods

    num = 100 # class variable
    # default constructor in other languages we use the name of the class to create
    # class constructor in python we use _init_
    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when is created")


    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber # method returns the sum of 2 numbers

# Instance variable obj
#obj = Calculator() # Create an object to access to class Calculator
obj = Calculator(2,3) #
obj.getData() # Use the object to access to class Methods
obj.num # Access to class variables throught the object
print(obj.num)