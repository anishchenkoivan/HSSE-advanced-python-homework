import asyncio

import matplotlib.pyplot as plt
from test import generate_data
from synchronous import find_synchronous
from multithreaded import find_multithreaded
from multiprocessed import find_multiprocessed
from asynchronous import find_async

a, v = generate_data(1_000_000)

time_elapsed = [
    find_synchronous(a, v)[1],
    find_multithreaded(a, v)[1],
    find_multiprocessed(a, v)[1],
    asyncio.run(find_async(a, v))[1]
]

labels = [
    'Синхронная реализация',
    'Многопоточная реализация',
    'Многопроцессная реализаци',
    'Асинхронная реализация'
]

plt.figure(figsize=(16, 10))
plt.bar(labels, time_elapsed, color=['skyblue', 'salmon', 'lightgreen', 'gold'])

plt.title('Равнение производительности разных подходов для решения ресурсоемкой задачи')
plt.ylabel('Время выполнения, с.')
plt.xlabel('Подход')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
