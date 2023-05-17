from typing import List, Callable
import time


def function_runner(lst: List[Callable]) -> None:
    """
    Runs a list of functions and displays a progress bar using tqdm.

    Args:
    lst (List[Callable]): A list of callable functions to be executed.

    Returns:
    None
    """
    # TODO
    for func in lst:
        func()


def func1():
    time.sleep(0.5)


def func2():
    time.sleep(0.8)


function_runner([func1, func2])
