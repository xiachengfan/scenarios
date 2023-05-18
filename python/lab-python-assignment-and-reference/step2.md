# Understanding References

In Python, variables are references to objects. When you assign a value to a variable, you're actually creating a reference to the object that represents the value.

Here's an example to illustrate this concept:

```python
# Illustrate Python references.
x = [1, 2, 3]
y = x
y.append(4)

print("x:", x)
print("y:", y)
```

Output:

```python
x: [1, 2, 3, 4]
y: [1, 2, 3, 4]
```

In this example, both `x` and `y` refer to the same list object. When we modify the list through the `y` reference by appending `4`, the change is reflected in both `x` and `y`.
