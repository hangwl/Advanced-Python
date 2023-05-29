# type hinting is a formal solution to statically indicate the type of a value with your Python code

def greet(name: str) -> str:
    return "Hello, " + name

print(greet("Bob"))