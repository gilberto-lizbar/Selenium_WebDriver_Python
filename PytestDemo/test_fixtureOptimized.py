import pytest


@pytest.mark.usefixtures("setup")  # Annotation to apply setup from conftest to all tests
class TestExample:
    # If conftest file is created do not need to declare set up method in this file
    """@pytest.fixture()   # This works as before annotation
    def setup():
        print("I will be executing first")
        yield  # Code behind this line will be executed until are completed
        print("executed last")"""

    def test_fixtureDemo(self):  # Only fixture can be passed as an argument
        print("i will execute steps in fixtureDemo")

    def test_fixtureDemo2(self):  # Only fixture can be passed as an argument
        print("i will execute steps in fixtureDemo2")

    def test_fixtureDemo3(self):  # Only fixture can be passed as an argument
        print("i will execute steps in fixtureDemo3")

    def test_fixtureDemo4(self):  # Only fixture can be passed as an argument
        print("i will execute steps in fixtureDemo4")
