VERSION = "1.0"
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
if _name_ == "_main_":
    print("Calculator v" + VERSION)
    print("2 + 3 =", add(2,3))
    print("4 x 5 =", multiply(4, 5))