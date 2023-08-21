import threading
import time

res = 0


def sum_list(lst):
    global res
    for i in lst:
        res += i


def task(sep_list):
    threads = []
    start_time = time.time()

    for sep in sep_list:
        thread = threading.Thread(target=sum_list, args=[sep])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return res, time.time() - start_time
