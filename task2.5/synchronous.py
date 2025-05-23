from time import time
from data import Data


def find_synchronous(a: list[Data], target_value) -> tuple[Data | None, float]:
    start = time()
    for i in a:
        if i.value == target_value:
            return i, time() - start
    return None, time() - start
