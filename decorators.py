"""
- This file is to practice and document my learning/understanding of decorators/closures.
"""


"""
# Standard Function: do something when called
"""

def break_():
    print("")


"""
# First-Class Functions: assign a function to a variable
"""

def outer_function():
    def inner_function():
        print("We assigned a function to a variable!")
    return inner_function

first_class = outer_function()
first_class()

break_()


"""
# Closure: assign function to a variable which retains information
"""

def outer_function(msg):
    def inner_function(msg2):
        print(f"{msg} {msg2}.")
    return inner_function

test_func = outer_function("test")
thanks_func = outer_function("thank")

test_func("function")
thanks_func("you")

break_()


"""
# Decorator: contribute further functionality to a function
"""

# Define a function to be wrapped
def plus(x, y):
    return x+y

# Define a function to be wrapped
def minus(x, y):
    return x-y

# The wrapping function
def logger(func):
    def log_func(*args):
        print(f"Running {func.__name__} with arguments {args}: ", end="")
        print(func(*args))
    return log_func

# Assign loggers to the function wrapped by LOGGER
addition_logger = logger(plus)
subtraction_logger = logger(minus)

# Call assigned functions, and note newfound capability!
addition_logger(3, 9)
subtraction_logger(9, 6)

break_()


"""
# Fancy Decorator Syntax!
"""

@logger
def scream(msg):
    return msg.upper().replace(".", "!")

scream("such fancy decorations...")

break_()

"""
# More fancy pants magic, but using a wrapper-class instead of a function!
"""

class decorator_class(object):
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        print(f"I'm a little class decorator, joined today by {self.function.__name__} and their homies {args}.")
        print(self.function(*args, **kwargs))
        return self.function(*args, **kwargs)

@decorator_class
def whisper(msg):
    return msg.lower().replace("!", ".")

whisper("I HOPE THEY DON'T HEAR US!!")

break_()

"""
# Last but not least, going to be doing some class concatenation
"""

from functools import wraps, update_wrapper
import functools

def logger_wrapped(func):
    
    @wraps(func)
    def log_func(*args):
        print(f"Running {func.__name__} with arguments {args}: ", end="")
        print(func(*args))
    
    return log_func

class decorator_class_wrapped(object):
    def __init__(self, func):
        self.function = func
        update_wrapper(self, self.function)

    def __call__(self, *args, **kwargs):
        print(f"I'm a little class decorator, joined today by {self.function.__name__} and their homies {args}.")
        #print(self.function(*args, **kwargs))
        return self.function(*args, **kwargs)

@logger_wrapped
@decorator_class_wrapped
def finale(n):
    return("BANZAI" + "!"*n)

finale(4)