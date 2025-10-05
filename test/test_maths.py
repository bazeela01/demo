
import pytest
import src.math as t  

@pytest.mark.parametrize("x,y" , [(8,1),(78,16)])
def test_addition(x,y):
    res = t.add(x,y)
    assert res == x+y       