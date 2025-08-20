from LearningPython.OopsDemo import Calculator  # This line is added to import class calculator


class ChildImpl(Calculator):  # This class inherate methods and variables from Calculator class
    num2 = 200

    def _init_(self, a, b):
        Calculator.__init__(self, a, b)

    def get_completed_data(self):
        return self.num2 + self.num + self.Summation()


'''obj = ChildImpl(2, 3)  # If you create an object for current class need to verify which parameters
# are required from the constructor of parent class '''
obj = ChildImpl(12, 10)  # You need to add the constructor of the parent class into current class
print(obj.get_completed_data())
