#fib sequence 
#Connor Stomp Assignment 1
from functools import lru_cache
from time import time
import matplotlib.pyplot as pyplot


def timer(func): 
    def wrap_func(*args, **kwargs): 
        num = args
        t1 = time() 
        result = func(*args, **kwargs) 
        t2 = time() 
        print(f'Finished in {(t2-t1):.4f}s : f{(num)}') 
        return result 
    return wrap_func 
  

@lru_cache
@timer 
def fib(n: int)-> int:
    if n <= 1:
        return n
    else:
        return (fib(n-1)+fib(n-2))
    

if __name__ == "__main__":
    fib(100)
    
