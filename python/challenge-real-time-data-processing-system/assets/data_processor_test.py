import time
from multiprocessing import Queue, Process, Event

from data_processor import process_stock_data


def test_process_stock_data():
    datas = [
        ("TSLA", 100),
        ("TSLA", 200),
        ("TSLA", 300),
    ]
    stop_event = Event()
    data_queue = Queue()
    for data in datas:
        data_queue.put(data)

    data_proc_process = Process(
        target=process_stock_data, args=(data_queue, stop_event)
    )
    data_proc_process.start()

    time.sleep(1)
    stop_event.set()
    data_proc_process.join()


if __name__ == "__main__":
    test_process_stock_data()
