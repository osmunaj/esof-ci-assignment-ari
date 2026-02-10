
def add(a,b):
    return a + b

def test_add():
    assert add(2,3) == 5
    assert add('space', 'ship') == 'spaceship'

def subtract(a,b):
    return a - b # this used to be + to make the test fail. so the large update is just changing it to -

# uncomment the following test in step 5 <- you need this part so the test actually works
def test_subtract():
    assert subtract(2, 3) == -1
