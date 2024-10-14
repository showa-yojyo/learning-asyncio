#!/usr/bin/env python

"""
Timeouts
<https://docs.python.org/3/library/asyncio-task.html#asyncio.timeout>
"""

import asyncio

async def long_running_task() -> None:
    await asyncio.sleep(50)

async def main() -> None:
    try:
        async with asyncio.timeout(10):
            await long_running_task()
    except TimeoutError:
        print("The long operation timed out, but we've handled it.")

    print("This statement will run regardless.")

asyncio.run(main())
