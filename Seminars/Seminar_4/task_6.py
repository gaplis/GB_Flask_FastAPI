# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# Используйте асинхронный подход.

import os
import asyncio
import time
from pathlib import Path


async def count_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        words = len(f.read().split())

    print(f"{file} count {words} words")


async def main(files):
    tasks = []
    for file in files:
        f = Path(file)
        if f.is_file():
            task = asyncio.ensure_future(count_words(f))
            tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.time()
    files = os.listdir('.')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(files))

    print(f'{time.time() - start_time}')
