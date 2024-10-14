#!/usr/bin/env python
"""
Sleeping
<https://docs.python.org/3/library/asyncio-task.html#asyncio.sleep>

Features:
- asynio.get_running_loop()
- asynio.sleep()
- asyncio.run()
"""

import asyncio
from datetime import datetime

async def display_date() -> None:
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(f'{datetime.now():%T}')
        if loop.time() + 1.0 >= end_time:
            break

        # Suspend the current task
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.run(display_date())
