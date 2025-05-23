import multiprocessing
from concurrent.futures import ThreadPoolExecutor
from time import time
from data import Data


def find_multithreaded(a: list[Data], target_value) -> tuple[Data | None, float]:
    start = time()
    n = multiprocessing.cpu_count()
    single_length = max(len(a) // n, 1)
    slices = [single_length + (1 if i < len(a) % n else 0) for i in range(n)]
    segments = []
    s = 0
    for i in slices:
        segments.append((s, s + i))
        s += i

    with ThreadPoolExecutor(max_workers=n) as executor:
        futures = [executor.submit(_worker, a, target_value, segments[i][0], segments[i][1]) for i in range(n)]
        results = [f.result() for f in futures if f.result is not None]

    return results[0], time() - start


def _worker(a: list[Data], target_value, l, r) -> Data | None:
    for i in range(l, r):
        if a[i].value == target_value:
            return a[i]
