from typing import List, Any


def list_length_updater(lst: List[List[Any]], total_num: int) -> None:
    """
    Updates the length of a list of sublists and displays a progress bar using tqdm.

    Args:
    lst (List[List[Any]]): A list of sublists whose length is to be updated.
    total_num (int): Total number of updates to be performed.

    Returns:
    None
    """
    # TODO
    total = total_num
    for sub_lst in lst:
        pass


lst = [[1, 2, 3], [4, 5]]

list_length_updater(lst, 5)
