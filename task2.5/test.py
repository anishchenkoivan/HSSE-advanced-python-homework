import asyncio
from random import randint
from data import Data
from synchronous import find_synchronous
from multithreaded import find_multithreaded
from multiprocessed import find_multiprocessed
from asynchronous import find_async

def generate_data(size):
    data_array = [Data(randint(0, int(1e11))) for _ in range(size)]
    target_value = Data(randint(0, int(1e11)))
    return data_array, target_value


if __name__ == '__main__':
    a, v = generate_data(1_000_000)

    print("Синхронная реализация     ", find_synchronous(a, v))
    print("Многопоточная реализация  ", find_multithreaded(a, v))
    print("Многопроцессная реализация", find_multiprocessed(a, v))
    print("Асинхронная реализация    ", asyncio.run(find_async(a, v)))
