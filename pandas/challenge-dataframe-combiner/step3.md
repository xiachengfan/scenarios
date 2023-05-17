# Merging DataFrames

In this sub-challenge, you will practice merging DataFrames based on a common column.

## TODO

- Complete the `merging_dataframes` function in the `merging_dataframes.py`.
- Use the `create_dataframe` function to generate two DataFrame, `df3` and `df4`, each containing 3 columns `('A', 'B', 'C')` and `5` rows of random integers.
- Add a common column to both DataFrames called `Key` with the values `['K1', 'K2', 'K3', 'K4', 'K5']`.
- Perform an inner merge of the DataFrames on the `Key` column and return it.

## Example

You can run the `merging_dataframes.py` file to verify the correctness of the code:

```zsh
python3 merging_dataframes.py
# Output:
#    A_x  B_x  C_x Key  A_y  B_y  C_y
# 0   17   67   25  K1   36   87   28
# 1   76   79   42  K2   76   53   47
# 2    0   42   47  K3   21   14    0
# 3   88   45   95  K4    1   15   36
# 4   77   94   57  K5    9   79   21
```
