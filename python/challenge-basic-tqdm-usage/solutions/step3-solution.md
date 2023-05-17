# Solution

```python
from tqdm import tqdm, trange

def range_progress(total_num: int) -> None:
    """
    Displays a progress bar while iterating over a range of numbers using trange.

    Args:
    total_num (int): Total number of iterations.

    Returns:
    None
    """
    for _ in trange(total_num):
        pass

range_progress(5)
```
