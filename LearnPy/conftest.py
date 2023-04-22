import pytest

@pytest.fixture(autouse=True) 
def tc_setup():
    print("Launch browser")
    print("Login")
    print("Browse products")
    yield 
    print("Logoff")
    print("Close browser")

