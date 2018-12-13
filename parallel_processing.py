import os
import multiprocessing
from time import time

def f(x):
    for i in range(10):
        x = x * x * x
    return x


if __name__ == '__main__':
    numbers = 10000

    # Using multiprocessing
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    begin_time = time()
    pool.map(f, range(numbers))
    end_time = time()
    print('Multi processing time : {:.0f}'.format(end_time-begin_time))

    # using classic loop
    begin_time = time()
    for number in range(numbers):
        f(number)
    end_time = time()
    print('Classic loop time : {:.0f}'.format(end_time - begin_time))

    # Using explicit lists
    begin_time = time()
    [f(number) for number in range(numbers)]
    end_time = time()
    print('Implicit list time : {:.0f}'.format(end_time - begin_time))