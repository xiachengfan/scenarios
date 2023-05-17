# Function Runner

In this sub-challenge, you are given a list of functions in `function_runner.py` that need to be executed in sequence. Your task is to create a progress bar that tracks the completion of the functions using the `tqdm` library.

## TODO

1. Modify the `function_runner` function to display a progress bar using the `tqdm` library.
2. Compele `function_runner.py`

## Example

```python
def func1():
    time.sleep(0.5)

def func2():
    time.sleep(0.8)

function_runner([func1, func2])
```

Output:

```python
100%|████████████████████████████████████████| 2/2 [00:01<00:00,  1.52it/s]
```
