import pytest 

@pytest.fixture
def setUp():
    print("Launch browser")
    print("Login")
    print("Browse products")
    yield
    print("Logoff")
    print("Close browser")

def testAddItemtoCart(setUp):
    print("Add Item Successful")

def testRemoveItemFromCart(setUp):
    print("Remove Item Successful")