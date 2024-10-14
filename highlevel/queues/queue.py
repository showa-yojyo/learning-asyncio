#!/usr/bin/env python

"""
Queues
<https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue>
"""

import asyncio
import random
import time


async def worker(name: str, queue: asyncio.Queue[float]) -> None:
    while True:
        # Get a "work item" out of the queue.
        sleep_for = await queue.get()

        # Sleep for the "sleep_for" seconds.
        await asyncio.sleep(sleep_for)

        # Notify the queue that the "work item" has been processed.
        queue.task_done()

        print(f'{name} has slept for {sleep_for:.2f} seconds')


async def main() -> None:
    # Create a queue that we will use to store our "workload".
    queue = asyncio.Queue() # type: asyncio.Queue[float]

    # Generate random timings and put them into the queue.
    total_sleep_time: float = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)

    # Create three worker tasks to process the queue concurrently.
    tasks = [asyncio.create_task(worker(f'worker-{i}', queue)) for i in range(3)]

    # Wait until the queue is fully processed.
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # Cancel our worker tasks.
    for task in tasks:
        task.cancel()
    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)

    print('====')
    print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time: {total_sleep_time:.2f} seconds')

if __name__ == '__main__':
    asyncio.run(main())
