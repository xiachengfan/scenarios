import random
import time
import threading
from multiprocessing import Queue
from typing import List


def generate_stock_data(
    stock_symbols: List[str], interval: float, max_updates: int, output_queue: Queue
) -> None:
    """
    Generates random stock price updates for the given stock symbols at the specified interval.

    :param stock_symbols: A list of stock symbols.
    :param interval: The time interval in seconds between price updates.
    :param max_updates: The maximum number of price updates to generate for each stock.
    :param output_queue: A thread-safe Queue to store the generated price updates.
    """
    count = 0
    while count < max_updates:
        symbol = random.choice(stock_symbols)
        price = round(random.uniform(50, 200), 2)
        output_queue.put((symbol, price))
        count += 1
        time.sleep(interval)
