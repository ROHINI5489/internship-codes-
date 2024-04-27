def my_decorator(func):
    def wrapper():
        print("something is happening befor the function is called")
        func()
        print("something is happening after the function is called")
    return wrapper 
@my_decorator 
def say_hello():
    print("hello!")
    print("something")
say_hello()

