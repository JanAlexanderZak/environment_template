""" Module for decorators.

Reference:
    https://www.youtube.com/watch?v=T8CQwGIsrx4&t=11289s&ab_channel=PyCon2020

TEMPLATE

import functools


def wrapper(func):
    # Template for decorators

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        # The wrapper function replacing the original
        # Do something before calling the function
        value = func(*args, **kwargs)
        # Do something after calling the function
        return value

    return _wrapper
"""

import functools
import time

from typing import Callable


# ************************************ Generic


def wrapper(func: Callable) -> Callable:
    """ Template for decorators.
    - Rename wrapper function, outer "wrapper"
      and underscore inner function
    """
    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        # Some calculation before
        print(f'Before {func.__name__}')

        # Call the function
        value = func(*args, **kwargs)

        # Some calculation after
        print(f'After {func.__name__}')
        print("Altered value from wrapper: ", value + 1)

        # Usually return the value
        return value

    return _wrapper


# ************************************ Count Calls


def count_calls(func: Callable) -> Callable:
    # Implementation as function
    @functools.wraps(func)
    def _count_calls(*args, **kwargs):

        # Before functon
        _count_calls.num_calls += 1

        value = func(*args, **kwargs)
        return value

    # Assign attribute to func, gets executed first"
    _count_calls.num_calls = 0
    return _count_calls


# Implementation as class
class CountCalls:
    def __init__(self, func: Callable) -> None:
        self.func = func
        self.num_calls = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs) -> Callable:
        self.num_calls += 1
        return self.func(*args, **kwargs)


# ************************************ Timer


def timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def _timer(*args, **kwargs):
        tic = time.perf_counter()
        value = func(*args, **kwargs)
        toc = time.perf_counter()
        print(f"Elapsed time: {toc - tic:.2f} seconds")
        return value
    return _timer
