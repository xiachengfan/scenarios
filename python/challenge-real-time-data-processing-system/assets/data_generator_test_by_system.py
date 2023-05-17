import sys

sys.path.append("/home/labex/project")

import unittest, threading
from multiprocessing import Queue
from typing import List, Dict

from data_generator import generate_stock_data


class TestGenerateStockData(unittest.TestCase):
    def test_generate_stock_data(self):
        stock_symbols = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]
        interval = 0.1
        max_updates = 5

        data_queue = Queue()

        data_gen_thread = threading.Thread(
            target=generate_stock_data,
            args=(stock_symbols, interval, max_updates, data_queue),
        )
        data_gen_thread.start()
        data_gen_thread.join()

        self.assertEqual(data_queue.qsize(), max_updates)

        for _ in range(max_updates):
            symbol, price = data_queue.get()
            self.assertIn(symbol, stock_symbols)
            self.assertTrue(50 <= price <= 200)


if __name__ == "__main__":
    unittest.main()
