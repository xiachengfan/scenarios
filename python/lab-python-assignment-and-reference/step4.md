# Examples

Let's see a few more examples to reinforce the concepts we've learned:

## Example 1: Function with mutable default argument

Avoid using mutable objects as default arguments in functions:

```python
def bad_append(new_item, a_list=[]):
    a_list.append(new_item)
    return a_list

print(bad_append('one'))
```

Output:

```python
['one']
```

It looks good, but if we call this function again:

```python
print(bad_append('two'))
```

Output:

```python
['one', 'two']
```

The problem here, is that the default value of `a_list` is evaluated at function definition time. So every time you call the function, you get the same default value.The correct way is to create it at run time instead, inside the function.

```python
def append_to_list(item: int, a_list: list = None) -> list:
    """Append an item to a list and return the updated list."""
    if a_list is None:
        a_list = []
    a_list.append(item)
    return a_list

list_a = append_to_list(1, [1, 2, 3])
print(list_a)
```

Output:

```python
[1, 2, 3, 1]
```

## Example 2: Copying mutable objects

Use the `copy` module to create a new object when you want to work with a copy of a mutable object:

```python
import copy

# Demonstrate the use of the copy module.
original_list = [1, 2, 3]
copied_list = copy.copy(original_list)
copied_list.append(4)

print("original_list:", original_list)
print("copied_list:", copied_list)
```

Output:

```python
original_list: [1, 2, 3]
copied_list: [1, 2, 3, 4]
```

In this example, `copied_list` is a new object that is a copy of `original_list`. When we append `4` to `copied_list`, `original_list` remains unchanged.

## Example 3: Deep copying mutable objects

For nested mutable objects, using the `copy` function doesn't work:

```python
# your copy example here
original_nested_list = [[1, 2], [3, 4]]
copied_nested_list = copy.copy(original_nested_list)
copied_nested_list[0].append(5)

print("original_nested_list:", original_nested_list)
print("copied_nested_list:", copied_nested_list)
```

Output:

```python
original_nested_list: [[1, 2, 5], [3, 4]]
copied_nested_list: [[1, 2, 5], [3, 4]]
```

We can see that when we append `5` to `copied_nested_list`, the `original_nested_list` also appends `5`. So you should use the `deepcopy` function instead.:

```python
# your deepcopy example here
original_nested_list = [[1, 2], [3, 4]]
deep_copied_list = copy.deepcopy(original_nested_list)
deep_copied_list[0].append(5)

print("original_nested_list:", original_nested_list)
print("deep_copied_list:", deep_copied_list)
```

Output:

```python
original_nested_list: [[1, 2], [3, 4]]
deep_copied_list: [[1, 2, 5], [3, 4]]
```

In this example, `deepcopy` function copies the `original_nested_list` recursively, while the `copy` function creates a reference object to the first-level data of the `original_nested_list`.
