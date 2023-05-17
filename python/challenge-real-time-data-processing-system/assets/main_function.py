import threading
from multiprocessing import Queue, Event, Process

from data_generator import generate_stock_data
from data_processor import process_stock_data

def main() -> None:
    """
    Starts the data generator in a separate thread and the data processor in a separate process,
    and implements a mechanism to stop the system gracefully.
    """
    stock_symbols = ["AAPL", "GOOGL", "AMZN", "MSFT", "TSLA"]
    interval = 1
    max_updates = 20

    data_queue = Queue()
    stop_event = Event()

        # TODO

    try:

        # TODO

    except KeyboardInterrupt:
    
        # TODO

        print("\nStopped gracefully")

if __name__ == "__main__":
    main()
