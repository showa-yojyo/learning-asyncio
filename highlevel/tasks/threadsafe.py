#!/usr/bin/env python

"""
Scheduling From Other Threads
<https://docs.python.org/3/library/asyncio-task.html#asyncio.run_coroutine_threadsafe>
"""

import asyncio

async def main() -> None:
    loop = asyncio.get_running_loop()

    # Create a coroutine
    coro = asyncio.sleep(1, result=3)

    # Submit the coroutine to a given loop
    future = asyncio.run_coroutine_threadsafe(coro, loop)
    try:
        timeout = 3
        result = future.result(timeout)
    except TimeoutError:
        print('The coroutine took too long, cancelling the task...')
        future.cancel()
    except Exception as exc:
        print(f'The coroutine raised an exception: {exc!r}')
    else:
        print(f'The coroutine returned: {result!r}')

asyncio.run(main())
