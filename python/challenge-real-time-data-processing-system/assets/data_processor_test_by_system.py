import sys

sys.path.append("/home/labex/project")

import unittest, threading, random, time
from multiprocessing import Queue, Process, Event
from typing import List, Dict
from unittest.mock import patch

from data_processor import process_stock_data


class TestProcessStockData(unittest.TestCase):
    def create_stock_data(
        self, stock_symbols: List[str], n: int
    ) -> Dict[str, List[float]]:
        data = {}
        for symbol in stock_symbols:
            data[symbol] = [round(random.uniform(50, 200), 2) for _ in range(n)]
        return data

    def test_process_stock_data(self):
        stock_symbols = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]
        n = 5

        data_queue = Queue()
        stop_event = Event()

        stock_data = self.create_stock_data(stock_symbols, n)
        for symbol, prices in stock_data.items():
            for price in prices:
                data_queue.put((symbol, price))

        data_proc_process = Process(
            target=process_stock_data, args=(data_queue, stop_event)
        )
        data_proc_process.start()

        # Let the process run for a while
        time.sleep(2)

        stop_event.set()
        data_proc_process.join()
        self.assertTrue(data_queue.empty())
        self.assertTrue(stop_event.is_set())


if __name__ == "__main__":
    unittest.main()
