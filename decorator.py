def gaurav(func):
    def do_nothing(a,b):
        print("---------------")
        func(a,b)
        print("--------------------------------")
    return do_nothing

def decorator2(func):
    def decorator_2(a,b):
        print("HELLO")
        func(a,b)
    return decorator_2


@gaurav
def abc(name,lname):
    print(name,lname)
    
abc("Gaurav","Gandal")


@decorator2
@gaurav

def demo(x,y):
    print(x+y)
demo(10,20)


