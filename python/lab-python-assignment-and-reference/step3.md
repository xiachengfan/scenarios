# Mutable and Immutable Objects

Python has two types of objects: mutable and immutable.

Mutable objects can be modified after they are created. Lists, dictionaries, and sets are examples of mutable objects.

Immutable objects cannot be modified once they are created. Integers, floats, strings, and tuples are examples of immutable objects.

Let's look at an example that demonstrates the difference between mutable and immutable objects:

```python
# Mutable object example
mutable_list = [1, 2, 3]
another_mutable_list = mutable_list
another_mutable_list.append(4)
print("mutable_list:", mutable_list)
```

Output:

```python
mutable_list: [1, 2, 3, 4]
```

`mutable_list` append a `4` to the end of the list because it's mutable objects, but immutable objects cannot be modified once they are created.

```python
# Immutable object example
immutable_string = "hello"
another_immutable_string = immutable_string
another_immutable_string = another_immutable_string.upper()
print("immutable_string:", immutable_string)
```

Output:

```python
immutable_string: hello
```

It doesn't have any change, and if we want to change the `immutable_string` as follows, Python shell will throws a TypeError:

```python
immutable_string[0] = '1'
```

Output:

```python
TypeError: 'str' object does not support item assignment
```
