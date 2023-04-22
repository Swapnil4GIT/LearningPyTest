import pytest

@pytest.fixture(scope='function', autouse=True) 
def tc_setup():
    print("Launch browser")
    print("Login")
    print("Browse products")
    yield 
    print("Logoff")
    print("Close browser")

