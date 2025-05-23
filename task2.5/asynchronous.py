import asyncio
from time import time
from typing import Optional
from data import Data


async def find_async(a: list[Data], target_value) -> tuple[Optional[Data], float]:
    start = time()
    n = min(10, len(a))
    single_length = max(len(a) // n, 1)
    slices = [single_length + (1 if i < len(a) % n else 0) for i in range(n)]
    segments = []
    s = 0
    for i in slices:
        segments.append((s, s + i))
        s += i

    tasks = [asyncio.create_task(_worker(a, target_value, l, r)) for (l, r) in segments]
    results = await asyncio.gather(*tasks)

    for result in results:
        if result is not None:
            return result, time() - start

    return None, time() - start

async def _worker(a: list[Data], target_value, l, r) -> Optional[Data]:
    for i in range(l, r):
        await asyncio.sleep(0)
        if a[i].value == target_value:
            return a[i]
    return None
