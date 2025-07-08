# def sum(x,y):
#     result=x+y
#     print(f"The sum of {x} and {y} is: {result}")
    
# def sum(x,y,z):
#     result=x+y+z
#     print(f"The sum of {x}, {y}, and {z} is: {result}")
    
# sum(5, 10)  # This will call the first sum function
# sum(5, 10, 15)  # This will call the second sum function with three parameters

from multipledispatch import dispatch
@dispatch(int, int)
def sum(x, y):
    result = x + y
    print(f"The sum of {x} and {y} is: {result}")
@dispatch(int, int, int)
def sum(x, y, z):
    result = x + y + z
    print(f"The sum of {x}, {y}, and {z} is: {result}")

sum(5, 10)  # This will call the first sum function
sum(5, 10, 15)  # This will call the second sum function with three parameters