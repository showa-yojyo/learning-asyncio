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
        # We do not know the timeout when starting, so we pass ``None``.
        async with asyncio.timeout(None) as cm:
            # We know the timeout now, so we reschedule it.
            new_deadline = asyncio.get_running_loop().time() + 10.
            cm.reschedule(new_deadline)

            await long_running_task()
    except TimeoutError:
        pass

    if cm.expired():
        print("Looks like we haven't finished on time.")

asyncio.run(main())
