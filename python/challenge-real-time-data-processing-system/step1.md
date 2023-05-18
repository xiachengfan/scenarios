# Stock Market Data Generator

The purpose of this sub-challenge is to create a stock market data generator that produces random price updates for a list of stock symbols. The generator should run in a separate thread and generate price updates at regular intervals.

## TODO

- Complete the `generate_stock_data` function in the `data_generator.py`, which receives a list of stock symbols, a time interval in seconds, and the maximum number of price updates to generate for each stock.
- Implement a loop in the function that runs until the maximum number of price updates has been reached.
- For each iteration, a stock symbol is randomly selected and a price in the range between **50** and **200** is generated for it.
- Sleep for the specified time interval between iterations.
- Store the stock symbols and generated prices as a tuple in the queue.

## Help

When you are done with the `generate_stock_data` function, you can test it using the `data_generator_test.py` file we have prepared for you, which has the following format for its output:

```zsh
$ python3 data_generator_test.py
# Output:
('TSLA', 88.32)
('GOOGL', 79.95)
('GOOGL', 186.53)
('AAPL', 90.62)
('TSLA', 131.68)
```
