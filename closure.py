def demo(a):
    def test(b):
        print(a+b)
    return test

data = demo(10)

data(2)
data(20)