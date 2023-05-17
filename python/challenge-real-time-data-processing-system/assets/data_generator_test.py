from multiprocessing import Queue

from data_generator import generate_stock_data


def test_generate_stock_data():
    stock_symbols = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]
    interval = 0
    max_updates = 5
    data_queue = Queue()

    generate_stock_data(stock_symbols, interval, max_updates, data_queue)

    while not data_queue.empty():
        print(data_queue.get())


if __name__ == "__main__":
    test_generate_stock_data()
