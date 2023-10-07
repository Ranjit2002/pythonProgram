def greet(fn):
    def mfx():
        print("Hey user!")
        fn()
        print("Thanks for using this function")

    return mfx


@greet
def hello():
    print("Hello World")


# hello()  # First write @greet at the top of a function then only the function will decorate
# greet(hello)()   # We can call greet function like this also

# without decorator

import time


def cal_square(numbers):
    start = time.time()
    result = []
    for num in numbers:
        result.append(num * num)
    end = time.time()
    print("cal_square took " + str((end - start) * 1000) + " mil second")
    return result


def cal_cube(numbers):
    start = time.time()
    result = []
    for num in numbers:
        result.append(num*num*num)
    end = time.time()
    print("cal_cube took " + str((end - start) * 1000) + " mil second")
    return result


# array = range(1, 100000)
# square = cal_square(array)
# cube = cal_cube(array)

# with decorator

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("func_time_took " + str((end - start) * 1000) + " mil second")
        return result
    return wrapper


@time_it
def cal_square(numbers):
    result = []
    for i in numbers:
        result.append(i*i)
    return result

@time_it
def cal_cube(numbers):
    result = []
    for i in numbers:
        result.append(i*i*i)
    return result


# array = range(1, 100000)
# square = cal_square(array)
# cube = cal_cube(array)

def outer(fn):
    def inner(name):
        if name == 'all students':
            print(name, "You are on time")
        else:
            fn(name)
    return inner


@outer
def alter(name):
    print('Hello', name, 'you are late')


# alter('ram')
# alter('all students')
# alter('shyam')

