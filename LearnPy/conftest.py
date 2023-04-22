import pytest

@pytest.fixture(scope='function', autouse=True) 
def tc_setup(browser):

    if browser == "chrome":
        print("Launch chrome")
    elif browser == "ff":
        print("Launch firefox")
    else:
        print("Provide valid browser")

    print("Login")
    print("Browse products")
    yield 
    print("Logoff")
    print("Close browser")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope='function', autouse=True)
def browser(request):
    return  request.config.getoption('--browser')