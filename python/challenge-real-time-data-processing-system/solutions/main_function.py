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

    data_gen_thread = threading.Thread(
        target=generate_stock_data,
        args=(stock_symbols, interval, max_updates, data_queue),
    )
    data_proc_process = Process(
        target=process_stock_data, args=(data_queue, stop_event)
    )

    data_gen_thread.start()
    data_proc_process.start()

    try:
        data_gen_thread.join()
        data_proc_process.join()
    except KeyboardInterrupt:
        stop_event.set()

        data_gen_thread.join()
        data_proc_process.terminate()
        data_proc_process.join()

        print("\nStopped gracefully")


if __name__ == "__main__":
    main()
