# basic idea of decorators

def mydecorator(function):
    
    def wrapper(*args, **kwargs):
        return_value = function(*args, **kwargs)
        print("I am decorating your function!")
        return return_value
    
    return wrapper

@mydecorator # @ adds functionality to mydecorator
def hello(person):
    return f"Hello {person}!"

print(hello("Mike"))