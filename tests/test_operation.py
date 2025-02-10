from src.math_operation import add,sub

def test_add():
    assert add(3,5)==8
    assert add(-5,3)==-2

def test_sub():
    assert sub(3,1)==2
    assert sub(-5,2)==-7
