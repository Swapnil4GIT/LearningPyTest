import pytest 

# @pytest.fixture(params=["a","b"])
# def demo_fixture(request):
#     print(request.param)

@pytest.mark.parametrize("a, b, final", [(2,6,8), (5,8,15), (5,10,15)])
def testLogin(a, b, final):
    assert a+b == final 
    
# def testLogin(demo_fixture):
#     print("Login Successful")

# def testLogoff():
#     print("Logoff Successful")

# def testCalculation():
#     assert 2+2 == 4

