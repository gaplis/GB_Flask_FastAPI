import asyncio
import time

res = 0


async def sum_list(lst):
    global res
    for i in lst:
        res += i


async def main(sep_list):
    tasks = []

    for sep in sep_list:
        aio_task = asyncio.ensure_future(sum_list(sep))
        tasks.append(aio_task)
    await asyncio.gather(*tasks)


def task(lst=None):
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(lst))

    return res, time.time() - start_time
