from multiprocessing import Process, Queue, cpu_count
from typing import List
from data import Data
from time import time


def find_multiprocessed(a: List[Data], target_value):
    t = time()

    n = cpu_count()
    q = Queue()

    single_length = len(a) // n
    slices = [single_length + (1 if i < len(a) % n else 0) for i in range(n)]
    segments = []
    s = 0
    for i in slices:
        segments.append((s, s + i))
        s += i

    processes = [Process(target=_worker, args=(a[s[0]:s[1]], target_value, q)) for s in segments]
    for p in processes:
        p.start()


    result = None
    for _ in range(n):
        r = q.get()
        if r is not None:
            result = r
            break

    for p in processes:
        p.terminate()
        p.join()

    return result, time() - t


def _worker(sublist, target_value, q):
    for item in sublist:
        if item.value == target_value:
            q.put(item)
            return
    q.put(None)
