# Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории
# и выводить результаты в консоль.
# Используйте процессы

import os
from multiprocessing import Process
import time
from pathlib import Path


def count_words(file):
    with open(file, 'r', encoding='utf-8') as f:
        words = len(f.read().split())

    print(f"{file} count {words} words")


processes = []
start_time = time.time()

files = os.listdir('.')

if __name__ == '__main__':
    for file in files:
        f = Path(file)
        if f.is_file():
            process = Process(target=count_words, args=(f,))
            processes.append(process)
            process.start()

    for process in processes:
        process.join()

print(f'{time.time() - start_time:.8f}')
