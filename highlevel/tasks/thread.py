#!/usr/bin/env python

"""
Running in Threads
<https://docs.python.org/3/library/asyncio-task.html#asyncio.to_thread>
"""

import asyncio
import time

def blocking_io() -> None:
    print(f"start blocking_io at {time.strftime('%X')}")
    # Note that time.sleep() can be replaced with any blocking
    # IO-bound operation, such as file operations.
    time.sleep(1)
    print(f"blocking_io complete at {time.strftime('%X')}")

async def main() -> None:
    print(f"started main at {time.strftime('%X')}")

    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(1))

    print(f"finished main at {time.strftime('%X')}")

asyncio.run(main())
