import sys
ele = 10
try:
    print(ele/0)
except Exception as e:
    print("String value encountered"+str(sys.exc_info()))
    print("String value encountered"+str(e.__class__))



