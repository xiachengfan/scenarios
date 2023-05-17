# Joining DataFrames

In this sub-challenge, you will explore joining DataFrames using index-based joining.

## TODO

- Complete the `joining_dataframes` function in the `joining_dataframes.py`.
- Use the `create_dataframe` function to generate two DataFrame, `df5` and `df6`, each containing 3 columns `('D', 'E', 'F')` and 5 rows of random integers.
- Set the index of both DataFrames to be `['L1', 'L2', 'L3', 'L4', 'L5']`.
- Perform an outer join of the DataFrames using the index and return it.

## Example

You can run the `joining_dataframes.py` file to verify the correctness of the code:

```zsh
python3 joining_dataframes.py
# Output:
#     D_left  E_left  F_left  D_right  E_right  F_right
# L1      70      94       0        3       59       49
# L2      24      98      77       85       53       21
# L3      75      53       6       58       93       42
# L4      20      81      80       63       69       20
# L5      53      27      34       37       97       48
```
