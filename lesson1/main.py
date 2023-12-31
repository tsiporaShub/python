from datetime import *

def myDecorator(func):
    def wrapper():
        before = datetime.now()
        func()
        after = datetime.now()
        print(after - before)
    return wrapper

@myDecorator
def func1():
    for i in range(999999999):
        # print(i)
        j = i

func1()
# ------------------------------

d={}
def cache(func):
    def wrapper(x):
        if(x in d):
            return d[x]
        y=func(x)
        d[x]=y
        return y
    return wrapper


@cache
def fib(n):
    if(n==0):
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        return fib(n-1)+fib(n-2)

@myDecorator
def test():
    print(fib(300))
    print(fib(400))
    print(fib(350))

test()
test()