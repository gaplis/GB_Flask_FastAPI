from multiprocessing import Pool
import time


def sum_list(lst):
    res = 0
    for i in lst:
        res += i

    return res


def task(sep_list):
    start_time = time.time()

    pool = Pool(processes=10)
    result = pool.map(sum_list, sep_list)

    return sum(result), time.time() - start_time
