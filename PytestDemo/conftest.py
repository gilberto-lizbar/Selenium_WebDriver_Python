import pytest


# conftest will be available for all the tests in folder which names follows name convention
# test_name, instead add the fixture method in the tests file and then call it in method
# Fixture is declared one time in conftest.py, any method which receive as argument the fixture
# will execute fixture as before test method
# example: When run the file test_demo2 if method has the argument the name of method for fixture
# it will execute fixture before run a particular test for example: test_secondGreetCreditCard(setup):


# fixtures are used for setup and tear down method for test case - contest file to generalize
# fixture and make it available to all test cases

# @pytest.fixture works as before annotation so setup method will be executed before any test
@pytest.fixture(scope="class")  # adding scope="class" means setup method will be executed before class
def setup():
    print("I will be executing first")
    yield  # Code behind this line will be executed until tests are completed
    print("executed last")


@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["Gilberto", "Lizarraga", "gilberto.lizbar@gmail.com"]


@pytest.fixture(params=["chrome", "Firefox", "IE"])
def crossBrowser(request):  # Use request when you have fixtures with some params available
    return request.param


@pytest.fixture(params=[("Chrome", "CH"), ("Firefox", "FF"), ("Internet Explorer", "IE")])
def crossBrowser2(request):  # Use request when you have fixtures with some params available
    return request.param
