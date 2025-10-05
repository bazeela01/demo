
import pytest
import src.math as t  

@pytest.mark.parametrize("x,y" , [(8,1),(78,16)])
def test_addition(x,y):
    res = t.add(x,y)
    assert res == x+y       


@pytest.mark.parametrize("x,y" , [(87,19),(788,16)])
def test_substraction(x,y):
    res = t.subtract(x,y)
    assert res == x-y  

@pytest.mark.parametrize("x,y" , [(8,2),(78,6)])
def test_multiply(x,y):
    res = t.multiply(x,y)
    assert res == x*y  



# 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git 
