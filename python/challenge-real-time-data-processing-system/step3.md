# Main Function and Stopping Mechanism

In this sub-challenge, you will create the main function that starts the data generator and data processor and implements a mechanism to stop the system gracefully.

## TODO

- Complete the `main` function in `main_function.py` to start the data generator in a separate thread and the data processor in a separate process.
- Implement a keyboard interrupt handler to catch the `Ctrl+C` signal.
- When the `Ctrl+C` signal is detected, gracefully stop the data generator and data processor.
- Print a summary of the results, such as the total number of price updates generated and processed, and the time taken to complete the task.

## Help

After you finish the `main` function, you can run the `main_function.py` file and its output should be in the following format:

```zsh
$ python3 main_function.py
# Output
Average price of MSFT: 177.74
Average price of TSLA: 148.00
Average price of AMZN: 68.13
Average price of MSFT: 137.38
Average price of TSLA: 137.04
Average price of TSLA: 116.83
Average price of TSLA: 116.83
Average price of GOOGL: 111.05
Average price of MSFT: 134.37
Average price of TSLA: 108.35
Average price of AMZN: 98.89
Average price of AMZN: 91.97
Average price of AMZN: 105.74
Average price of TSLA: 110.30
Average price of AMZN: 106.62
Average price of AAPL: 134.78
Average price of TSLA: 118.44
Average price of AMZN: 101.31
Average price of GOOGL: 117.02
Average price of GOOGL: 121.95
^C # Press Ctrl+C
Stopped gracefully
```
