# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# any code should be wrapped in method only
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    print("Hello")


@pytest.mark.smoke
@pytest.mark.xfail
def test_secondProgram():
    print("Good Morning")
