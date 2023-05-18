import time
from multiprocessing import Queue, Event, Process
from typing import Dict, List

from data_generator import generate_stock_data


def process_stock_data(input_queue: Queue, stop_event: Event) -> None:
    """
    Processes the stock price updates from the input_queue and calculates the average price and trends.

    :param input_queue: A thread-safe Queue containing the stock price updates.
    :param stop_event: A multiprocessing Event to signal when to stop processing data.
    """
    stock_data: Dict[str, List[float]] = {}

    while not stop_event.is_set():
        while not input_queue.empty():
            symbol, price = input_queue.get()

            if symbol not in stock_data:
                stock_data[symbol] = []

            stock_data[symbol].append(price)

            avg_price = sum(stock_data[symbol]) / len(stock_data[symbol])
            print(f"Average price of {symbol}: {avg_price:.2f}")

        time.sleep(1)
