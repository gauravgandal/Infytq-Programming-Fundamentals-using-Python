age = -30
try:
    assert not age < 0
    
    print("Age is"+str(age))
    
except:
    print("Age must be positive")
else:
    print("Your age is"+str(age))
    
finally:
    print("This will be executed always")