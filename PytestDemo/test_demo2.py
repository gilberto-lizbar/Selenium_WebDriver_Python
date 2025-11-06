import pytest


def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because string not match"


@pytest.mark.smoke
def test_secondGreetCreditCard():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition do not match"


