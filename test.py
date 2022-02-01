"""
var_int=11
var_str = 'gaurav'
var_str1 = 'gandal'
var_float = 10.33
var_complex = 2j

print(var_int)
print(var_float)
print(var_str)
print(var_complex)

print(type(var_str))
print(type(var_float))
print(type(var_str))
print(type(var_complex))





class demo:
    def firstFunction(self):
        print("Testing Method in firstFunction")

obj = demo()
obj.firstFunction()
print(type(obj))

print(dir(obj))

print(dir(var_str))

print(var_str.title())
print(var_str + var_str1)

print(hex(id(var_str)))
print(hex(id(var_str1)))
print(hex(id(var_str+var_str1)))
"""

var_list = ['Gaurav', 171 , 9.43]
print(var_list[0])
deleted_item = var_list.remove(171)
print(var_list)

var_tuple=('gaurav',)
print(type(var_tuple))