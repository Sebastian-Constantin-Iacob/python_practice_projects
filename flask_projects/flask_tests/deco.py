def my_decorator(func):
    def wrapper(*args):
        print(f"function {func.__name__}, arguments {args}")
        func()
    return wrapper

list = [1, 2, 3, 4, 5, 9]

@my_decorator
def simple_function():
    print("HELLO!")


simple_function(list)
